import os
import re
import argparse
from typing import List, Dict, Set

def find_markdown_files(directory: str) -> List[str]:
    """Recursively find all markdown files in a directory."""
    markdown_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def extract_urls_from_markdown(content: str) -> Set[str]:
    """Extract all URLs from markdown content."""
    urls = set()
    # Extract links in [text](url) format
    link_matches = re.findall(r'\[.*?\]\((.*?)\)', content)
    urls.update(link_matches)
    
    # Extract raw URLs
    url_matches = re.findall(r'(https?://[^\s<>\)"\']+)', content)
    urls.update(url_matches)
    
    # Clean URLs (remove trailing punctuation and quotes)
    cleaned_urls = set()
    for url in urls:
        clean_url = url.strip().rstrip('.,!?;:"\'')
        cleaned_urls.add(clean_url)
    
    return cleaned_urls

def parse_reference_file(ref_file: str) -> Dict[str, List[str]]:
    """Parse the reference markdown file into sections and links."""
    with open(ref_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    sections = {}
    current_section = None
    
    for line in content.split('\n'):
        # Check for section headers
        section_match = re.match(r'^(#{1,6})\s+(.*)', line)
        if section_match:
            current_section = section_match.group(2).strip()
            sections[current_section] = []
            continue
        
        # Check for links
        link_match = re.match(r'^\s*-\s*\[.*?\]\((.*?)\)', line)
        if link_match and current_section is not None:
            url = link_match.group(1).strip()
            sections[current_section].append((url, line.strip()))
    
    return sections

def check_references(ref_file: str, check_path: str, output_dir: str = None):
    """Main function to check references against other markdown files."""
    # Get all markdown files to check against (from both check_path and output_dir)
    check_files = []
    
    # Add files from check_path
    if os.path.isfile(check_path):
        check_files.append(check_path)
    else:
        check_files.extend(find_markdown_files(check_path))
    
    # Add files from output_dir if specified and different from check_path
    if output_dir and os.path.exists(output_dir):
        output_dir_abs = os.path.abspath(output_dir)
        check_path_abs = os.path.abspath(check_path)
        
        # Only add output_dir files if it's a different directory
        if output_dir_abs != check_path_abs:
            output_files = find_markdown_files(output_dir)
            
            # Skip any files that would be duplicates of our output file
            ref_file_basename = os.path.basename(ref_file)
            output_filename = os.path.splitext(ref_file_basename)[0] + "_ref_checked.md"
            output_path = os.path.join(output_dir, output_filename)
            
            check_files.extend(
                f for f in output_files 
                if os.path.abspath(f) != os.path.abspath(output_path)
            )
    
    # Skip the reference file itself if it's in the check directories
    ref_file_abs = os.path.abspath(ref_file)
    check_files = [f for f in check_files if os.path.abspath(f) != ref_file_abs]
    
    # Extract all URLs from the files to check against
    existing_urls = set()
    for file_path in check_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            existing_urls.update(extract_urls_from_markdown(content))
        except (IOError, UnicodeDecodeError) as e:
            print(f"Warning: Could not read {file_path}: {e}")
    
    # Parse the reference file
    sections = parse_reference_file(ref_file)
    
    # Filter out URLs that exist in other files
    filtered_sections = {}
    for section, links in sections.items():
        filtered_links = []
        for url, line in links:
            clean_url = url.strip().rstrip('.,!?;:"\'')
            if clean_url not in existing_urls:
                filtered_links.append((url, line))
        
        if filtered_links:
            filtered_sections[section] = filtered_links
    
    # Generate the output content
    output_lines = []
    for section, links in filtered_sections.items():
        output_lines.append(f"# {section}\n")
        for _, line in links:
            output_lines.append(line)
        output_lines.append("")
    
    output_content = "\n".join(output_lines).strip()
    
    # Determine output path
    if output_dir is None:
        output_dir = os.path.dirname(ref_file) or "."
    
    os.makedirs(output_dir, exist_ok=True)
    ref_file_basename = os.path.basename(ref_file)
    output_filename = os.path.splitext(ref_file_basename)[0] + "_ref_checked.md"
    output_path = os.path.join(output_dir, output_filename)
    
    # Write the output file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_content)
    
    print(f"\nReference check for: {ref_file}")
    print(f"Checked against {len(check_files)} markdown files")
    print(f"Original references: {sum(len(links) for links in sections.values())}")
    print(f"Remaining references: {sum(len(links) for links in filtered_sections.values())}")
    print(f"Results written to: {output_path}\n")

    # Clean up empty markdown files from the output directory
    #clean_empty_fs(output_dir)

def clean_empty_fs(directory: str):
    """Remove all empty markdown files in the given directory (recursively)."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read().strip()
                    if not content:
                        os.remove(file_path)
                        print(f"Removed empty file: {file_path}")
                except Exception as e:
                    print(f"Error checking/removing {file_path}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Check markdown references against other files.")
    parser.add_argument('-f', '--file', required=True, help="Path to the reference markdown file")
    parser.add_argument('-c', '--check', required=True, 
                       help="Path to a file or directory to check references against")
    parser.add_argument('-o', '--output', help="Output directory (optional)")
    
    args = parser.parse_args()
    
    check_references(args.file, args.check, args.output)

if __name__ == "__main__":
    main()