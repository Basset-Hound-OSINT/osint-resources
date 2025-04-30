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

def process_markdown(input_filename):
    with open(input_filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Clean unwanted content
    patterns_to_remove = [
        r"\[↑\]\(#-content\)",
        r"\[⇧ Top\]\(#index\)",
        r"\[Top\]\(#index\)",
    ]
    for pattern in patterns_to_remove:
        content = re.sub(rf"^-?\s*{pattern}\s*$", "", content, flags=re.MULTILINE)

    # Find all headers and their positions
    header_regex = r'^(#{1,6})\s+(.*)$'
    headers = list(re.finditer(header_regex, content, re.MULTILINE))

    # Process each header and its content block
    output = []
    for i, match in enumerate(headers):
        header_level = match.group(1)
        header_text = match.group(2).strip()
        start = match.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(content)
        section_body = content[start:end]

        # Extract links from this section
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', section_body)

        # Format output
        output.append(f"{header_level} {header_text}\n")
        if links:
            for text, url in links:
                output.append(f"- [{text.strip()}]({url.strip()})")
        output.append("")  # Add a blank line

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

def format_file(input_file, output_dir):
    result = process_markdown(input_file)
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    new_file = os.path.join(output_dir, f"{base_name}_new.md")
    with open(new_file, "w", encoding="utf-8") as f:
        f.write(result)
    remove_unwanted_content(new_file, content_to_remove, patterns_to_replace)
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
