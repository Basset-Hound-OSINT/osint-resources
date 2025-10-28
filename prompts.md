I have alot of markdown documentation with links to resources, but it is messy, i am trying to build more structured documentation using mdbook, but i need to transfer the old documentation into new documentation. I basically want to extract the links for all tools in the old documentation, and output into ./tmp directory. i have the following python scripts to extract links from given markdown files, and to check that they are unique. I basically want to combine the reference chekcer script into the reference extractor script (can you just import it?) so that i can give an input directory, and an output directory, and for every file read in the input directory, the urls are extracted, then when they are written to a file that has the equivalent name of the current input file, they are checked for uniques across all files in the output directory. does this make sense? i have uplaoded my pyhton scripts and sample markdown documentation. Again i just want to make lists of links and keep the sections headers so i know what links go to what topic. does this make sense? 



Yes, this makes perfect sense! You want to:

Extract links from markdown files in an input directory
Preserve section headers to maintain context
Check for uniqueness across all already-processed files in the output directory
Write formatted output files with only unique links

I can combine these scripts for you. Here's an integrated solution:Combined Reference Extractor & CheckerCode import os
import re
import argparse
from typing import Set, Dict, List, Tuple

def extract_urls_from_markdown(content: str) -> Set[str]:
    """Extract all URLs from markdown content."""
    urls = set()
    # Extract links in [text](url) format
    Perfect! I've created a combined script that:
Key Features:

Extracts links from markdown files while preserving section headers
Checks for uniqueness across ALL files already in the output directory
Processes files or directories - you can give it a single file or a whole directory
Maintains context by keeping section headers with their associated links
Prevents duplicates both across files and within the same file

Usage:
bash# Process a single file
python combined_script.py -i path/to/Astrosp.md -o ./tmp

# Process an entire directory
python combined_script.py -i path/to/input_dir -o ./tmp
How it works:

Before processing each file, it scans the output directory to find all existing URLs
Extracts links from the input file, organized by section headers
Filters out any URLs that already exist in the output directory
Writes only the unique links to {filename}_refs.md in the output directory
Updates the "existing URLs" set so duplicates within the same file are also avoided

Output format:
markdown# Section Name

- [Link Text](https://example.com)
- [Another Link](https://example2.com)

# Another Section

- [More Links](https://example3.com)
The script will tell you how many new unique links were found in each file. Does this meet your needs?RetryClaude does not have the ability to run the code it generates yet.Dyes, and section headers may be # or ## or ### or even ####, does this make sense?Yes, absolutely! The script already handles all header levels (# through ######).
Looking at the code:
python# Check for section headers (any level)
header_match = re.match(r'^(#{1,6})\s+(.+)$', line)
The regex ^(#{1,6}) matches between 1 and 6 hash marks, so it will capture:

# Main Section
## Subsection
### Sub-subsection
#### Deep nested section
And so on...

However, I should update the output format to preserve the original header level so you maintain the hierarchy. Let me fix that:Combined Reference Extractor & CheckerCode ∙ Version 2 def parse_markdown_with_sections(content: str) -> Dict[str, Tuple[str, List[Tuple[str, str]]]]:
    """
    Parse markdown and organize links by section headers.
    Returns: Dict[section_name] -> (header_level, List[(link_text, url)])
    """
    sePerfect! Now the script preserves the original header level. So if your input has:
markdown## PRODUCTIVITY
- [Link 1](...)

### Subsection
- [Link 2](...)

#### Deep Section
- [Link 3](...)
The output will maintain that hierarchy:
markdown## PRODUCTIVITY

- [Link 1](...)

### Subsection

- [Link 2](...)

#### Deep Section

- [Link 3](...)
This way you keep the full structure and context of your documentation! Does this work better for you?