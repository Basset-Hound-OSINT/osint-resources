import sys
import re

def process_markdown(input_filename):
    # Read the input file
    with open(input_filename, 'r') as file:
        content = file.read()

    # List of content to remove without the "- " prefix
    content_to_remove = [
        r"\[↑\]\(#-content\)",  # Remove "[↑](#-content)"
        r"\[⇧ Top\]\(#index\)",  # Remove "[⇧ Top](#index)"
        r"\[Top\]\(#index\)",  # Remove "[Top](#index)"
    ]

    # List of content to prepend "- "
    content_to_remove_prepend = [f"- {item}" for item in content_to_remove]

    # Combine both lists into one (original without "- " and prepended with "- ")
    all_content_to_remove = content_to_remove + content_to_remove_prepend

    # Remove unwanted content from the entire file **before** processing
    for pattern in all_content_to_remove:
        content = re.sub(pattern, "", content)

    # Regular expression to match any header level (# to #####, followed by the heading text)
    pattern = r"^(#{2,5})\s*(.*?)\n"
    matches = re.findall(pattern, content, re.MULTILINE)

    # Create the output content with the required format
    output_content = ""
    
    # Position in the content
    last_position = 0

    # Now process each header block
    for i, (heading, category) in enumerate(matches):
        # Extract the section content between this header and the next header (if any)
        start_index = content.find(heading + " " + category, last_position)
        if i + 1 < len(matches):
            next_header = matches[i + 1][0] + " " + matches[i + 1][1]
            end_index = content.find(next_header, start_index)
            section_content = content[start_index:end_index]
        else:
            # If it's the last section, take everything till the end of the file
            section_content = content[start_index:]

        # Collect links first from the section content
        link_pattern = r"\[([^\]]+)\]\(([^)]+)\)"
        links_found = re.findall(link_pattern, section_content)

        # Preserve the header as it is for now (we will modify it later)
        if re.match(r"^\[\]\(#.*\)\s*(.*)", category):
            # Remove the markdown link part like [](#social-media-and-photos)
            category = re.sub(r"\[\]\(#.*\)", "", category).strip()

        # Add the heading with the same number of #'s (preserve the header)
        output_content += f"{heading} {category.strip()}\n\n"

        # Only add links if found in the section
        if links_found:
            for link_text, link_url in links_found:
                output_content += f"- [{link_text.strip()}]({link_url.strip()})\n"

        output_content += "\n"  # Add a newline after each category

        # Update the position for the next category
        last_position = start_index

    # Replace double spaces with a single space in the final output
    output_content = re.sub(r"  +", " ", output_content)

    # Generate the new filename
    output_filename = input_filename.replace('.md', '_new.md')

    # Write the new content to the new file
    with open(output_filename, 'w') as new_file:
        new_file.write(output_content)

    print(f"New file saved as {output_filename}")

# Entry point for the script
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: script.py [FILENAME].md")
        sys.exit(1)

    input_filename = sys.argv[1]

    # Ensure the file ends with .md
    if not input_filename.endswith(".md"):
        print("The input file must have a .md extension.")
        sys.exit(1)

    process_markdown(input_filename)
