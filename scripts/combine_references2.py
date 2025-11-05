#!/usr/bin/env python3
"""
=====================================================================
 📘 Markdown Link Extraction & Comparison Pipeline
=====================================================================

Simple 3-step process with detailed statistics:

1. Recursively walks ./references → extracts all links → makes unique
2. Recursively walks ./src → extracts all links → makes unique  
3. Compares unique references vs unique src → writes diff to ./tmp

---------------------------------------------------------------------
🗂️ Directory Structure

./src/                  → Your docs source (recursively scanned)
./references/           → Reference files (recursively scanned)
./tmp/                  → Output (mirrors ./references structure)

---------------------------------------------------------------------
🚀 Usage

    python combine_references2.py

---------------------------------------------------------------------
Notes
- All comparisons are CASE-INSENSITIVE
- URLs are normalized (trailing slashes, http/https, www variants)
- Global deduplication happens before comparison
- Detailed statistics track reductions at each stage
- Only writes files that have unique links not found in ./src
=====================================================================
"""

import os
import re
from collections import defaultdict
from urllib.parse import urlparse, urlunparse

# Fixed paths
SRC_DIR = "./src"
REF_DIR = "./references"
TMP_DIR = "./tmp"

# ============================================================
# Helpers
# ============================================================

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


def normalize_url(url: str) -> str:
    """
    Normalize URL for comparison:
    - Lowercase the entire URL
    - Remove trailing slashes from path
    - Normalize http/https (treat as same)
    - Remove fragment (#anchors)
    - Keep ALL subdomains intact (tool1.google.com ≠ tool2.google.com)
    """
    url = url.strip().lower()
    
    # Parse the URL
    try:
        parsed = urlparse(url)
    except:
        # If URL parsing fails, just return lowercase version
        return url
    
    # Normalize scheme (treat http and https as same)
    scheme = 'https' if parsed.scheme in ('http', 'https') else parsed.scheme
    
    # Keep domain exactly as-is (preserve all subdomains)
    domain = parsed.netloc
    
    # Normalize path (remove all trailing slashes, treat empty and / as same)
    path = parsed.path.rstrip('/')
    # Empty path means root, so both '' and '/' should normalize to ''
    if not path:
        path = ''
    
    # Remove fragment (anchors)
    fragment = ''
    
    # Keep query params as-is (could sort them for stricter matching)
    query = parsed.query
    
    # Reconstruct normalized URL
    normalized = urlunparse((scheme, domain, path, parsed.params, query, fragment))
    
    return normalized


def normalize_link_format(line: str) -> str:
    """
    Normalize any markdown link into bullet format "- [text](url)".
    """
    match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", line)
    if not match:
        return ""
    text, url = match.groups()
    return f"- [{text.strip()}]({url.strip()})"


def url_to_key(link: str) -> str:
    """
    Extract URL from markdown link and normalize it for comparison.
    This is the KEY function that ensures URLs match correctly.
    """
    match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", link)
    if not match:
        return normalize_url(link)
    
    url = match.group(2).strip()
    return normalize_url(url)


def extract_sections(md_text: str):
    """Extract sections and normalize all links to bullet format."""
    sections = defaultdict(list)
    current = "Uncategorized"  # Default section if no header found
    
    for line in md_text.splitlines():
        header = re.match(r"^#{1,6}\s+(.*)", line)
        link = re.search(r"\[([^\]]+)\]\(([^)]+)\)", line)
        
        if header:
            current = header.group(1).strip()
        elif link:
            normalized = normalize_link_format(line)
            if normalized:
                sections[current].append(normalized)
    
    return dict(sections)


def write_sections(filepath: str, sections: dict):
    """Write sections and links to markdown file."""
    with open(filepath, "w", encoding="utf-8") as f:
        for header in sorted(sections.keys()):
            links = sections[header]
            if links:  # Only write sections with links
                f.write(f"## {header}\n\n")
                for link in sorted(links):
                    f.write(f"{link}\n")
                f.write("\n")


def collect_all_links_from_dir(directory: str):
    """
    Recursively walk directory and collect all links with metadata.
    Returns: 
        - all_links_raw: list of ALL links found (with duplicates)
        - unique_links: dict mapping normalized URL key -> (link_text, url, source_file, header)
        - file_stats: dict mapping file -> link count for debugging
    """
    all_links_raw = []
    unique_links = {}  # normalized_url_key -> (full_link, source_file, header)
    file_stats = {}
    
    if not os.path.exists(directory):
        print(f"⚠️  Directory not found: {directory}")
        return all_links_raw, unique_links, file_stats
    
    for root, _, files in os.walk(directory):
        for file in files:
            if not file.endswith(".md"):
                continue
            
            path = os.path.join(root, file)
            rel_path = os.path.relpath(path, directory)
            
            try:
                content = open(path, encoding="utf-8").read()
                sections = extract_sections(content)
                
                file_link_count = 0
                for header, links in sections.items():
                    for link in links:
                        all_links_raw.append(link)
                        file_link_count += 1
                        
                        # CRITICAL: Use normalized URL as key
                        url_key = url_to_key(link)
                        
                        # Store first occurrence of each unique URL
                        if url_key not in unique_links:
                            unique_links[url_key] = (link, rel_path, header)
                
                file_stats[rel_path] = file_link_count
                            
            except Exception as e:
                print(f"⚠️  Error reading {path}: {e}")
    
    return all_links_raw, unique_links, file_stats


def print_percentage(label, value, total):
    """Helper to print a value with percentage."""
    if total > 0:
        pct = (value / total) * 100
        return f"{label}: {value:,} ({pct:.1f}%)"
    return f"{label}: {value:,}"


# ============================================================
# Main Pipeline
# ============================================================

def main():
    print("=" * 70)
    print("🔹 Step 1: Extracting all links from ./references (recursively)...")
    print("=" * 70)
    
    ref_links_raw, ref_unique_links, ref_file_stats = collect_all_links_from_dir(REF_DIR)
    
    print(f"\n📊 Raw extraction statistics:")
    print(f"  • Total links found (with duplicates): {len(ref_links_raw):,}")
    print(f"  • Files processed: {len(ref_file_stats)}")
    
    print(f"\n📄 Per-file breakdown:")
    for file, count in sorted(ref_file_stats.items()):
        print(f"    {file}: {count} links")
    
    print("\n🔹 Step 1.5: Making references list unique (case-insensitive + URL normalization)...")
    print(f"\n📊 Deduplication statistics:")
    print(f"  • Before: {len(ref_links_raw):,} total links")
    print(f"  • After:  {len(ref_unique_links):,} unique URLs")
    
    duplicates_removed = len(ref_links_raw) - len(ref_unique_links)
    if len(ref_links_raw) > 0:
        dup_pct = (duplicates_removed / len(ref_links_raw)) * 100
        print(f"  • Duplicates removed: {duplicates_removed:,} ({dup_pct:.1f}%)")
    
    print("\n" + "=" * 70)
    print("🔹 Step 2: Extracting all links from ./src (recursively)...")
    print("=" * 70)
    
    src_links_raw, src_unique_links, src_file_stats = collect_all_links_from_dir(SRC_DIR)
    
    print(f"\n📊 Raw extraction statistics:")
    print(f"  • Total links found (with duplicates): {len(src_links_raw):,}")
    print(f"  • Files processed: {len(src_file_stats)}")
    
    print("\n🔹 Step 2.5: Making src list unique (case-insensitive + URL normalization)...")
    print(f"\n📊 Deduplication statistics:")
    print(f"  • Before: {len(src_links_raw):,} total links")
    print(f"  • After:  {len(src_unique_links):,} unique URLs")
    
    src_duplicates_removed = len(src_links_raw) - len(src_unique_links)
    if len(src_links_raw) > 0:
        src_dup_pct = (src_duplicates_removed / len(src_links_raw)) * 100
        print(f"  • Duplicates removed: {src_duplicates_removed:,} ({src_dup_pct:.1f}%)")
    
    print("\n" + "=" * 70)
    print("🔹 Step 3: Comparing unique references vs unique src...")
    print("=" * 70)
    
    # Get the normalized URL keys
    ref_url_keys = set(ref_unique_links.keys())
    src_url_keys = set(src_unique_links.keys())
    
    print(f"\n📊 Comparison statistics:")
    print(f"  • Unique URLs in references: {len(ref_url_keys):,}")
    print(f"  • Unique URLs in src: {len(src_url_keys):,}")
    
    # Find URLs in references that are NOT in src
    unique_to_refs = ref_url_keys - src_url_keys
    already_in_src = ref_url_keys & src_url_keys
    
    if len(ref_url_keys) > 0:
        print(f"  • URLs already in src: {len(already_in_src):,} ({len(already_in_src)/len(ref_url_keys)*100:.1f}%)")
        print(f"  • URLs unique to references: {len(unique_to_refs):,} ({len(unique_to_refs)/len(ref_url_keys)*100:.1f}%)")
    
    if not unique_to_refs:
        print("\n✅ No unique links found! All reference links already exist in ./src")
        return
    
    print(f"\n🔍 Sample of URLs already in src (first 5):")
    for i, url_key in enumerate(list(already_in_src)[:5]):
        print(f"    {i+1}. {url_key}")
    
    print(f"\n🔍 Sample of URLs unique to references (first 5):")
    for i, url_key in enumerate(list(unique_to_refs)[:5]):
        print(f"    {i+1}. {url_key}")
    
    # Organize unique links by their original file and section
    file_sections = defaultdict(lambda: defaultdict(list))
    
    for url_key in unique_to_refs:
        if url_key in ref_unique_links:
            link, source_file, header = ref_unique_links[url_key]
            file_sections[source_file][header].append(link)
    
    # Write to ./tmp mirroring the structure
    ensure_dir(TMP_DIR)
    files_written = 0
    files_skipped = 0
    
    print("\n" + "=" * 70)
    print("🔹 Writing unique links to ./tmp (mirroring structure)...")
    print("=" * 70)
    
    for source_file, sections in sorted(file_sections.items()):
        link_count = sum(len(links) for links in sections.values())
        
        # Skip files with no unique links
        if link_count == 0:
            files_skipped += 1
            print(f"  ⊘ {source_file}: No unique links (skipped)")
            continue
        
        tmp_path = os.path.join(TMP_DIR, source_file)
        ensure_dir(os.path.dirname(tmp_path))
        
        write_sections(tmp_path, sections)
        
        original_count = ref_file_stats.get(source_file, 0)
        
        files_written += 1
        
        if original_count > 0:
            reduction_pct = ((original_count - link_count) / original_count) * 100
            print(f"  ✓ {source_file}:")
            print(f"      Original: {original_count} links")
            print(f"      Unique:   {link_count} links")
            print(f"      Reduced:  {reduction_pct:.1f}%")
        else:
            print(f"  ✓ {source_file}: {link_count} unique links")
    
    print("\n" + "=" * 70)
    print("✅ Pipeline complete!")
    print("=" * 70)
    print(f"\n📊 Final Summary:")
    print(f"  • Total reference links (raw): {len(ref_links_raw):,}")
    print(f"  • Unique reference URLs: {len(ref_unique_links):,}")
    if len(ref_links_raw) > 0:
        print(f"  • Duplicates in references: {duplicates_removed:,} ({dup_pct:.1f}%)")
    print(f"  • Total src links (raw): {len(src_links_raw):,}")
    print(f"  • Unique src URLs: {len(src_unique_links):,}")
    print(f"  • URLs already in src: {len(already_in_src):,}")
    print(f"  • URLs unique to references: {len(unique_to_refs):,}")
    if len(ref_links_raw) > 0:
        print(f"  • Reduction from raw to final: {(len(ref_links_raw) - len(unique_to_refs)) / len(ref_links_raw) * 100:.1f}%")
    print(f"  • Files written to ./tmp: {files_written}")
    print(f"  • Files skipped (no unique links): {files_skipped}")
    print(f"\n🔍 Results: {TMP_DIR}/ (mirrors {REF_DIR}/ structure)")


if __name__ == "__main__":
    main()