#!/usr/bin/env python3
"""
Markdown Link Checker
Parses all markdown files in the current directory and validates all links.
"""

import os
import re
import requests
from pathlib import Path
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Set, Tuple, List
import time

# Configuration
TIMEOUT = 10  # seconds
MAX_WORKERS = 10  # concurrent requests
RETRY_ATTEMPTS = 2
RETRY_DELAY = 1  # seconds

# User agent to avoid being blocked
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

def extract_links_from_markdown(file_path: str) -> List[Tuple[str, int]]:
    """
    Extract all URLs from a markdown file.
    Returns list of tuples: (url, line_number)
    """
    links = []
    
    # Patterns to match markdown links and bare URLs
    patterns = [
        r'\[([^\]]+)\]\(([^\)]+)\)',  # [text](url)
        r'<(https?://[^>]+)>',         # <url>
        r'(?:^|\s)(https?://\S+)',     # bare URLs
    ]
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                for pattern in patterns:
                    matches = re.finditer(pattern, line)
                    for match in matches:
                        # Extract URL (different groups for different patterns)
                        url = match.group(2) if len(match.groups()) > 1 else match.group(1)
                        url = url.strip()
                        
                        # Skip anchors and local files
                        if url.startswith('#') or not url.startswith('http'):
                            continue
                            
                        links.append((url, line_num))
    
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    return links

def check_link(url: str, retries: int = RETRY_ATTEMPTS) -> Tuple[str, bool, str]:
    """
    Check if a URL is accessible.
    Returns tuple: (url, is_valid, error_message)
    """
    for attempt in range(retries):
        try:
            response = requests.head(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)

            # Some sites block HEAD requests, try GET if HEAD fails
            if response.status_code == 405:
                response = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True, stream=True)

            # Treat 2xx and 3xx as valid
            if response.status_code < 400:
                return (url, True, "")

            # Treat 429 (Too Many Requests) as ignored (not broken)
            if response.status_code == 429:
                return (url, True, "HTTP 429 - Ignored")

            # Other HTTP errors are considered broken
            return (url, False, f"HTTP {response.status_code}")

        except requests.exceptions.Timeout:
            if attempt < retries - 1:
                time.sleep(RETRY_DELAY)
                continue
            return (url, False, "Timeout")

        except requests.exceptions.ConnectionError:
            if attempt < retries - 1:
                time.sleep(RETRY_DELAY)
                continue
            return (url, False, "Connection Error")

        except requests.exceptions.TooManyRedirects:
            return (url, False, "Too Many Redirects")

        except Exception as e:
            return (url, False, str(e))

    return (url, False, "Max retries exceeded")

def get_markdown_files(directory: str = '.') -> List[str]:
    """Get all markdown files in the directory."""
    return [str(f) for f in Path(directory).glob('*.md')]

def write_report(broken_links: List, total_links: int, output_file: str = "errs.md"):
    """Write the broken links report to a markdown file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Broken Links Report\n\n")
        f.write(f"**Generated:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Total Links Checked:** {total_links}\n\n")
        f.write(f"**Broken Links Found:** {len(broken_links)}\n\n")
        
        if broken_links:
            f.write("---\n\n")
            f.write("## Broken Links\n\n")
            
            for url, error_msg, locations in sorted(broken_links):
                f.write(f"### ❌ {url}\n\n")
                f.write(f"**Error:** `{error_msg}`\n\n")
                f.write(f"**Found in:**\n\n")
                for file_path, line_num in locations:
                    f.write(f"- `{file_path}:{line_num}`\n")
                f.write("\n")
        else:
            f.write("---\n\n")
            f.write("## ✅ All Links Valid\n\n")
            f.write("No broken links were found!\n")
        
        f.write("---\n\n")
        f.write(f"**Summary:** {total_links - len(broken_links)}/{total_links} links valid\n")

def main():
    print("=" * 80)
    print("Markdown Link Checker")
    print("=" * 80)
    print()
    
    # Get all markdown files
    md_files = get_markdown_files()
    
    if not md_files:
        print("No markdown files found in current directory.")
        return
    
    print(f"Found {len(md_files)} markdown file(s)")
    print()
    
    # Collect all links from all files
    all_links = {}  # url -> [(file, line_num), ...]
    
    for md_file in md_files:
        print(f"Parsing: {md_file}")
        links = extract_links_from_markdown(md_file)
        
        for url, line_num in links:
            if url not in all_links:
                all_links[url] = []
            all_links[url].append((md_file, line_num))
    
    if not all_links:
        print("\nNo links found in any markdown files.")
        return
    
    print(f"\nFound {len(all_links)} unique URL(s) across all files")
    print(f"Checking links with {MAX_WORKERS} concurrent workers...\n")
    
    # Check all links concurrently
    broken_links = []
    checked = 0
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_url = {executor.submit(check_link, url): url for url in all_links.keys()}
        
        for future in as_completed(future_to_url):
            url, is_valid, error_msg = future.result()
            checked += 1
            
            if not is_valid:
                broken_links.append((url, error_msg, all_links[url]))
            
            # Progress indicator
            if checked % 10 == 0:
                print(f"Checked {checked}/{len(all_links)} links...", end='\r')
    
    print(f"Checked {checked}/{len(all_links)} links...   ")
    print()
    
    # Write report to file
    output_file = "errs.md"
    write_report(broken_links, len(all_links), output_file)
    print(f"Report written to: {output_file}\n")
    
    # Also print summary to console
    if broken_links:
        print("=" * 80)
        print(f"BROKEN LINKS FOUND: {len(broken_links)}")
        print("=" * 80)
        print()
        
        for url, error_msg, locations in sorted(broken_links):
            print(f"❌ {url}")
            print(f"   Error: {error_msg}")
            print(f"   Found in:")
            for file_path, line_num in locations:
                print(f"     - {file_path}:{line_num}")
            print()
    else:
        print("✅ All links are valid!")
    
    print("=" * 80)
    print(f"Summary: {len(all_links) - len(broken_links)}/{len(all_links)} links valid")
    print("=" * 80)

if __name__ == "__main__":
    main()