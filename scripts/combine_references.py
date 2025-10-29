import os
import re
import argparse
from typing import Set, Dict, List, Tuple

def extract_urls_from_markdown(content: str) -> Set[str]:
    """Extract all URLs from markdown content."""
    urls = set()
    # Extract links in [text](url) and ![text](url) format
    link_matches = re.findall(r'(?:!?\[.*?\])\((.*?)\)', content)
    urls.update(link_matches)
    
    # Extract raw URLs
    url_matches = re.findall(r'(https?://[^\s<>\)"\']+)', content)
    urls.update(url_matches)
    
    # Clean and normalize URLs
    cleaned_urls = set()
    for url in urls:
        # First clean basic punctuation
        clean_url = url.strip().rstrip('.,!?;:"\'')
        
        # Normalize protocol (convert http:// to https://)
        if clean_url.startswith('http://'):
            clean_url = 'https://' + clean_url[7:]
            
        # Remove trailing slash while preserving subdomains and path
        clean_url = clean_url.rstrip('/')
        
        cleaned_urls.add(clean_url)
    
    return cleaned_urls

def parse_markdown_with_sections(content: str) -> Dict[str, Tuple[str, List[Tuple[str, str]]]]:
    """
    Parse markdown and organize links by section headers.
    Returns: Dict[section_name] -> (header_level, List[(link_text, url)])
    """
    sections = {}
    current_section = "Uncategorized"
    current_level = "#"
    sections[current_section] = (current_level, [])
    
    lines = content.split('\n')
    
    for line in lines:
        # Check for section headers (any level)
        header_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if header_match:
            # Save the header level (e.g., "##" or "###")
            current_level = header_match.group(1)
            # Clean the header text
            header_text = header_match.group(2).strip()
            # Remove any existing links from header
            header_text = re.sub(r'\[.*?\]\(.*?\)', '', header_text)
            header_text = header_text.strip()
            current_section = header_text
            if current_section not in sections:
                sections[current_section] = (current_level, [])
            continue
        
        # Extract markdown-style links [text](url) and ![text](url)
        markdown_links = re.findall(r'(?:!?\[([^\]]+)\]\(([^)]+)\))', line)
        for link_text, url in markdown_links:
            # Clean and normalize URL
            clean_url = url.strip().rstrip('.,!?;:"\'')
            if clean_url.startswith('http://'):
                clean_url = 'https://' + clean_url[7:]
            clean_url = clean_url.rstrip('/')
            
            clean_text = link_text.strip().rstrip('.,!?;:"\'')
            if clean_url.startswith(('http://', 'https://')):
                sections[current_section][1].append((clean_text, clean_url))
        
        # Extract raw URLs
        raw_urls = re.findall(r'(https?://[^\s<>\)"\']+)', line)
        for url in raw_urls:
            # Skip if already captured in markdown link
            if not any(url in link[1] for link in sections[current_section][1]):
                # Clean and normalize URL
                clean_url = url.strip().rstrip('.,!?;:"\'')
                if clean_url.startswith('http://'):
                    clean_url = 'https://' + clean_url[7:]
                clean_url = clean_url.rstrip('/')
                sections[current_section][1].append((clean_url, clean_url))
    
    # Remove empty sections
    sections = {k: v for k, v in sections.items() if v[1]}
    
    return sections

def get_existing_urls_from_output(output_dir: str) -> Set[str]:
    """Get all URLs that already exist in the unique output directory."""
    existing_urls = set()
    
    unique_dir = os.path.join(output_dir, 'unique')
    if not os.path.exists(unique_dir):
        return existing_urls
    
    for filename in os.listdir(unique_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(unique_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    existing_urls.update(extract_urls_from_markdown(content))
            except Exception as e:
                print(f"Warning: Could not read {filepath}: {e}")
    
    return existing_urls

def write_output_file(filepath: str, sections: Dict[str, Tuple[str, List[Tuple[str, str]]]]):
    """Write sections to an output file."""
    output_lines = []
    for section, (header_level, links) in sections.items():
        output_lines.append(f"{header_level} {section}\n")
        for link_text, url in links:
            # Ensure clean link text and URL
            clean_link_text = link_text.strip()
            clean_url = url.strip()
            output_lines.append(f"- [{clean_link_text}]({clean_url})")
        output_lines.append("")  # Empty line between sections
    
    output_content = "\n".join(output_lines).strip() + "\n"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(output_content)

def process_markdown_file(input_file: str, output_dir: str):
    """Process a single markdown file and extract links."""
    
    # Read input file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {input_file}: {e}")
        return
    
    # Parse the markdown file
    sections = parse_markdown_with_sections(content)
    
    if not sections:
        print(f"No links found in {input_file}")
        return
    
    # Create output directories
    os.makedirs(output_dir, exist_ok=True)
    unique_dir = os.path.join(output_dir, 'unique')
    os.makedirs(unique_dir, exist_ok=True)
    
    # Determine output filename
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    raw_output_file = os.path.join(output_dir, f"{base_name}_refs.md")
    unique_output_file = os.path.join(unique_dir, f"{base_name}_refs.md")
    
    # Write raw output (all links from this file)
    total_links = sum(len(links) for _, links in sections.values())
    write_output_file(raw_output_file, sections)
    
    # Get existing URLs from unique directory
    existing_urls = get_existing_urls_from_output(output_dir)
    
    # Filter out URLs that already exist for unique output
    unique_sections = {}
    new_urls_count = 0
    
    for section, (header_level, links) in sections.items():
        unique_links = []
        for link_text, url in links:
            # Normalize URL for comparison
            clean_url = url.strip().rstrip('.,!?;:"\'')
            if clean_url.startswith('http://'):
                clean_url = 'https://' + clean_url[7:]
            clean_url = clean_url.rstrip('/')
            
            # Only add if URL doesn't exist in any unique output file
            if clean_url not in existing_urls:
                unique_links.append((link_text, url))
                existing_urls.add(clean_url)  # Prevent duplicates within this file
                new_urls_count += 1
        
        if unique_links:
            unique_sections[section] = (header_level, unique_links)
    
    # Write unique output (only new links)
    if unique_sections:
        write_output_file(unique_output_file, unique_sections)
    
    # Print summary
    print(f"Processed: {input_file}")
    print(f"  Raw output: {raw_output_file} ({total_links} links)")
    if unique_sections:
        print(f"  Unique output: {unique_output_file} ({new_urls_count} new links)")
    else:
        print(f"  Unique output: No new unique links")
    print()

def process_directory(input_dir: str, output_dir: str):
    """Process all markdown files in a directory."""
    if not os.path.exists(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist")
        return
    
    markdown_files = [f for f in os.listdir(input_dir) if f.endswith('.md')]
    
    if not markdown_files:
        print(f"No markdown files found in {input_dir}")
        return
    
    print(f"Processing {len(markdown_files)} markdown file(s)...\n")
    
    for filename in markdown_files:
        input_file = os.path.join(input_dir, filename)
        process_markdown_file(input_file, output_dir)

def main():
    parser = argparse.ArgumentParser(
        description="Extract links from markdown files. Creates both raw output (all links) "
                    "and unique output (deduplicated links in 'unique/' subdirectory)."
    )
    parser.add_argument(
        '-i', '--input',
        required=True,
        help="Input file or directory containing markdown files"
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help="Output directory for extracted links"
    )
    
    args = parser.parse_args()
    
    if os.path.isfile(args.input):
        # Process single file
        process_markdown_file(args.input, args.output)
    elif os.path.isdir(args.input):
        # Process directory
        process_directory(args.input, args.output)
    else:
        print(f"Error: '{args.input}' is not a valid file or directory")

if __name__ == "__main__":
    main()