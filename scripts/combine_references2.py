#!/usr/bin/env python3
"""
=====================================================================
 📘 Markdown Link Extraction & Comparison Pipeline
=====================================================================

This script automates multi-stage link processing for a markdown project.

It scans all reference folders, extracts links, deduplicates them, and
compares them against your mdBook source content.

---------------------------------------------------------------------
🗂️ Directory Structure (before running)

./src/                → Your mdBook content folder (used for comparison)
./references_01/      → Reference markdown folder #1 (input)
./references_02/      → Reference markdown folder #2 (input)
... (any folder starting with "references")

---------------------------------------------------------------------
📦 Output Directory (auto-generated)

./tmp_references/
├── links/          → Raw extracted links (normalized as "- [text](url)")
├── unique_refs/    → Deduplicated links (unique across all references)
├── unique_srcs/    → Links not found in ./src (new or missing content)
└── stats/          → CSV logs showing per-file line reduction

---------------------------------------------------------------------
⚙️ How it works (3 stages)

1️⃣ Extract:  Collect and normalize links from `references_*` → ./tmp_references/links/
2️⃣ Dedupe:   Combine and deduplicate all links → ./tmp_references/unique_refs/
3️⃣ Compare:  Compare unique refs vs ./src links → ./tmp_references/unique_srcs/

---------------------------------------------------------------------
🚀 Usage

    python extract_links_pipeline.py --src ./src --tmp ./tmp_references

---------------------------------------------------------------------
Notes
- All extracted links are normalized into bullet format: "- [title](url)"
- Original reference folders are never modified.
- Section headers are preserved for context and later sorting.
- A CSV report of line reductions is written to ./tmp_references/stats/
=====================================================================
"""

import os
import re
import argparse
import csv
from datetime import datetime

# ============================================================
# Helpers
# ============================================================

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


def normalize_link_format(line: str) -> str:
    """
    Normalize any markdown link into bullet format "- [text](url)".
    Removes numbering or other leading characters.
    """
    match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", line)
    if not match:
        return ""
    text, url = match.groups()
    return f"- [{text.strip()}]({url.strip()})"


def extract_sections(md_text: str):
    """Extract sections and normalize all links to bullet format."""
    sections = {}
    current = None
    for line in md_text.splitlines():
        header = re.match(r"^#{1,6}\s+(.*)", line)
        link = re.search(r"\[([^\]]+)\]\(([^)]+)\)", line)
        if header:
            current = header.group(1).strip()
            sections[current] = []
        elif link and current:
            normalized = normalize_link_format(line)
            if normalized:
                sections[current].append(normalized)
    return sections


def merge_sections(sections_list):
    """Merge multiple section dicts into one, deduplicating links."""
    merged = {}
    for sections in sections_list:
        for header, links in sections.items():
            merged.setdefault(header, set()).update(links)
    return {h: sorted(list(links)) for h, links in merged.items()}


def write_sections(filepath: str, sections: dict):
    """Write sections and links to markdown file."""
    with open(filepath, "w", encoding="utf-8") as f:
        for header, links in sections.items():
            f.write(f"## {header}\n\n")
            for link in sorted(links):
                f.write(f"{link}\n")
            f.write("\n")


# ============================================================
# Metrics Tracking
# ============================================================

def log_reduction_stats(log_dir: str, filename: str, original_lines: int, new_lines: int):
    """Record reduction statistics for each processed file."""
    ensure_dir(log_dir)
    log_path = os.path.join(log_dir, "reduction_log.csv")

    reduction = original_lines - new_lines
    percent = (reduction / original_lines * 100) if original_lines > 0 else 0.0

    with open(log_path, "a", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        # Write header if file is empty
        if csvfile.tell() == 0:
            writer.writerow(["timestamp", "file", "original_lines", "new_lines", "reduction", "percent_reduction"])
        writer.writerow([
            datetime.now().isoformat(timespec='seconds'),
            filename, original_lines, new_lines, reduction, f"{percent:.2f}%"
        ])

    print(f"  ↳ Reduced {filename}: {original_lines} → {new_lines} lines ({percent:.2f}% smaller)")


# ============================================================
# Core Pipeline Stages
# ============================================================

def process_references_dirs(ref_dirs, tmp_dir):
    """Stage 1: Extract and normalize links from all reference directories."""
    out_dir = os.path.join(tmp_dir, "links")
    ensure_dir(out_dir)

    for ref_dir in ref_dirs:
        for root, _, files in os.walk(ref_dir):
            for file in files:
                if not file.endswith(".md"):
                    continue

                path = os.path.join(root, file)
                content = open(path, encoding="utf-8").read()
                sections = extract_sections(content)

                out_file = os.path.join(out_dir, file)
                write_sections(out_file, sections)

                # Log line reduction
                content_lines = len(content.splitlines())
                new_lines = sum(len(links) for _, links in sections.items()) + len(sections)
                log_reduction_stats(os.path.join(tmp_dir, "stats"), file, content_lines, new_lines)


def build_unique_refs(tmp_dir):
    """Stage 2: Merge and deduplicate all extracted links."""
    links_dir = os.path.join(tmp_dir, "links")
    out_dir = os.path.join(tmp_dir, "unique_refs")
    ensure_dir(out_dir)

    for file in os.listdir(links_dir):
        if not file.endswith(".md"):
            continue

        path = os.path.join(links_dir, file)
        sections = extract_sections(open(path, encoding="utf-8").read())
        unique_sections = merge_sections([sections])

        out_file = os.path.join(out_dir, file)
        write_sections(out_file, unique_sections)

        # Log reduction vs original
        orig_content = open(path, encoding='utf-8').read()
        orig_lines = len(orig_content.splitlines())
        new_lines = sum(len(links) for _, links in unique_sections.items()) + len(unique_sections)
        log_reduction_stats(os.path.join(tmp_dir, "stats"), file, orig_lines, new_lines)


def compare_with_src(src_dir, tmp_dir):
    """Stage 3: Identify links in unique_refs not found in src."""
    refs_dir = os.path.join(tmp_dir, "unique_refs")
    out_dir = os.path.join(tmp_dir, "unique_srcs")
    ensure_dir(out_dir)

    # Gather all src links
    src_links = set()
    for root, _, files in os.walk(src_dir):
        for file in files:
            if not file.endswith(".md"):
                continue
            text = open(os.path.join(root, file), encoding="utf-8").read()
            for match in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", text):
                src_links.add(f"- [{match.group(1).strip()}]({match.group(2).strip()})")

    # Compare each unique_ref
    for file in os.listdir(refs_dir):
        if not file.endswith(".md"):
            continue

        path = os.path.join(refs_dir, file)
        content = open(path, encoding="utf-8").read()
        sections = extract_sections(content)

        filtered = {header: [l for l in links if l not in src_links] for header, links in sections.items()}
        out_file = os.path.join(out_dir, file)
        write_sections(out_file, filtered)

        # Log reduction (only if some links removed)
        orig_lines = len(content.splitlines())
        new_lines = sum(len(links) for _, links in filtered.items()) + len(filtered)
        log_reduction_stats(os.path.join(tmp_dir, "stats"), f"{file} (compare)", orig_lines, new_lines)


# ============================================================
# Main
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Extract and compare markdown links.")
    parser.add_argument("--src", required=True, help="Path to mdBook source folder.")
    parser.add_argument("--tmp", required=True, help="Path to temp working directory.")
    args = parser.parse_args()

    ensure_dir(args.tmp)

    ref_dirs = [d for d in os.listdir(".") if d.startswith("references_") and os.path.isdir(d)]
    if not ref_dirs:
        print("⚠️ No reference directories found (expected ./references_*)")
        return

    print("🔹 Stage 1: Extracting and normalizing links...")
    process_references_dirs(ref_dirs, args.tmp)

    print("\n🔹 Stage 2: Building unique reference sets...")
    build_unique_refs(args.tmp)

    print("\n🔹 Stage 3: Comparing against source content...")
    compare_with_src(args.src, args.tmp)

    print("\n✅ Pipeline complete! Results are in:")
    print(f"  {os.path.join(args.tmp, 'links/')}")
    print(f"  {os.path.join(args.tmp, 'unique_refs/')}")
    print(f"  {os.path.join(args.tmp, 'unique_srcs/')}")
    print(f"  {os.path.join(args.tmp, 'stats/reduction_log.csv')}")


if __name__ == "__main__":
    main()
