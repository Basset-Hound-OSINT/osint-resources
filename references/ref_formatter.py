import re
import os
import sys
import argparse
from functools import reduce

content_to_remove = [
    "[↑](#-table-of-contents)",
    "[↑](#-content)",
    "[](#table-of-contents)"
]

patterns_to_replace = {
    "[![": "["
}

def header_regex_cipher_387(header_text):
    cleaned = re.sub(r'^\s*\[.*?\]\(.*?\)\s*', '', header_text)
    return cleaned.strip()

def process_markdown(input_filename):
    with open(input_filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Clean unwanted lines
    patterns_to_remove = [
        r"\[↑\]\(#-content\)",
        r"\[⇧ Top\]\(#index\)",
        r"\[Top\]\(#index\)",
    ]
    for pattern in patterns_to_remove:
        content = re.sub(rf"^-?\s*{pattern}\s*$", "", content, flags=re.MULTILINE)

    header_regex = r'^(#{1,6})\s+(.*)$'
    headers = list(re.finditer(header_regex, content, re.MULTILINE))

    output = []

    # Handle case: file has NO headers at all
    if not headers:
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        links += [(url, url) for url in re.findall(r'(https?://[^\s]+)', content)]
        if links:
            output.append("# Uncategorized\n")
            for text, url in links:
                clean_url = url.strip().rstrip('.,!?;:')
                clean_text = text.strip().rstrip('.,!?;:')
                if clean_url.startswith(('http://', 'https://')):
                    output.append(f"- [{clean_text}]({clean_url})")
            output.append("")
        return "\n".join(output)

    # If headers exist, extract links before first header
    pre_header_text = content[:headers[0].start()]
    pre_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', pre_header_text)
    pre_links += [(url, url) for url in re.findall(r'(https?://[^\s]+)', pre_header_text)]
    if pre_links:
        output.append("# Uncategorized\n")
        for text, url in pre_links:
            clean_url = url.strip().rstrip('.,!?;:')
            clean_text = text.strip().rstrip('.,!?;:')
            if clean_url.startswith(('http://', 'https://')):
                output.append(f"- [{clean_text}]({clean_url})")
        output.append("")

    # Process each header section
    for i, match in enumerate(headers):
        header_level = match.group(1)
        original_header = match.group(2).strip()

        header_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', original_header)
        header_links += [(url, url) for url in re.findall(r'(https?://[^\s]+)', original_header)]

        cleaned_header = re.sub(r'\[.*?\]\(.*?\)', '', original_header)
        cleaned_header = re.sub(r'https?://[^\s]+', '', cleaned_header)
        cleaned_header = header_regex_cipher_387(cleaned_header)

        start = match.end()
        end = headers[i+1].start() if i+1 < len(headers) else len(content)
        section_body = content[start:end]

        body_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', section_body)
        body_links += [(url, url) for url in re.findall(r'(https?://[^\s]+)', section_body)]

        all_links = header_links + body_links
        output.append(f"{header_level} {cleaned_header}\n")
        if all_links:
            for text, url in all_links:
                clean_url = url.strip().rstrip('.,!?;:')
                clean_text = text.strip().rstrip('.,!?;:')
                if clean_url.startswith(('http://', 'https://')):
                    output.append(f"- [{clean_text}]({clean_url})")
        output.append("")

    return "\n".join(output)


def remove_unwanted_content(file_path, content_to_remove, patterns_to_replace):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cleaned_lines = []
    for line in lines:
        line = reduce(lambda l, c: l.replace(c, ""), content_to_remove, line)
        for old, new in patterns_to_replace.items():
            line = line.replace(old, new)
        cleaned_lines.append(line)

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(cleaned_lines)

def double_check(filename):
    """Remove empty sections (headers with no following links) and fix double parentheses"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # First fix double parentheses
    content = content.replace('))', ')')

    # Split content into sections
    sections = []
    current_section = []
    header_pattern = re.compile(r'^(#{1,6})\s+.*$')
    link_pattern = re.compile(r'^\s*-\s*\[.*?\]\(.*?\)\s*$')

    lines = content.split('\n')
    for line in lines:
        if header_pattern.match(line):
            if current_section:
                sections.append(current_section)
                current_section = []
        current_section.append(line)
    
    if current_section:
        sections.append(current_section)

    # Process sections
    cleaned_sections = []
    for section in sections:
        has_links = any(link_pattern.match(line) for line in section)
        is_uncategorized = any(line.strip().startswith('# Uncategorized') for line in section)
        
        # Keep section if it has links or is the only section (to prevent empty file)
        if has_links or (is_uncategorized and len(sections) == 1):
            cleaned_sections.append(section)
        elif not is_uncategorized and len(section) > 0 and header_pattern.match(section[0]):
            # Check if this is the only section with content (besides possibly Uncategorized)
            other_sections_have_content = any(
                any(link_pattern.match(line) for line in s) 
                for s in sections 
                if s != section
            )
            if not other_sections_have_content and any(link_pattern.match(line) for line in section):
                cleaned_sections.append(section)

    # Rebuild content
    cleaned_content = '\n'.join(
        '\n'.join(line for line in section if line.strip() != '')
        for section in cleaned_sections
    )

    # Remove multiple consecutive empty lines
    cleaned_content = re.sub(r'\n{3,}', '\n\n', cleaned_content).strip()

    # Write back to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(cleaned_content + '\n')
def format_file(input_file, output_dir):
    result = process_markdown(input_file)
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    new_file = os.path.join(output_dir, f"{base_name}_new.md")
    with open(new_file, "w", encoding="utf-8") as f:
        f.write(result)
    remove_unwanted_content(new_file, content_to_remove, patterns_to_replace)
    double_check(new_file)  # Run the double check after all other processing
    print(f"Formatted: {input_file} -> {new_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Format markdown files.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', help="Path to a single markdown file")
    group.add_argument('-d', '--dir', help="Path to a directory with .md files")
    parser.add_argument('-o', '--output', help="Output directory (optional, defaults to input location)")

    args = parser.parse_args()

    if args.file:
        output_dir = args.output or os.path.dirname(args.file) or "."
        os.makedirs(output_dir, exist_ok=True)
        format_file(args.file, output_dir)

    elif args.dir:
        output_dir = args.output or args.dir
        os.makedirs(output_dir, exist_ok=True)
        for filename in os.listdir(args.dir):
            if filename.endswith(".md"):
                input_path = os.path.join(args.dir, filename)
                format_file(input_path, output_dir)