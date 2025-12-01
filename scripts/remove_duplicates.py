#!/usr/bin/env python3
import os
import re
import argparse

# Match markdown links: [text](url)
LINK_RE = re.compile(r"\[.*?\]\((https?://[^)]+)\)", re.IGNORECASE)

def get_url(line: str):
    """Extract URL from markdown link line."""
    m = LINK_RE.search(line)
    return m.group(1).strip() if m else None


def process_file(path: str, erase=False):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    seen_urls = set()
    new_lines = []
    removed = []

    for line in lines:
        stripped = line.strip()
        url = get_url(stripped)

        # If it's a markdown link
        if url:
            if url.lower() in seen_urls:
                removed.append(stripped)
                continue
            seen_urls.add(url.lower())
            new_lines.append(stripped + "\n")
        else:
            # Keep non-link lines unchanged (normalized)
            new_lines.append(stripped + "\n")

    changed = (new_lines != lines)

    if changed:
        print(f"▶ {path}")
        for dup in removed:
            print(f"   removed duplicate: {dup}")

    if erase and changed:
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

    return changed


def walk(root=".", erase=False):
    changed_count = 0

    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            if not fname.lower().endswith(".md"):
                continue
            full = os.path.join(dirpath, fname)
            if process_file(full, erase=erase):
                changed_count += 1

    if not erase:
        print("\nDry run complete. Use --erase to apply changes.")
    else:
        print(f"\nDone. Cleaned {changed_count} files.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Remove duplicate markdown links by URL.")
    ap.add_argument("--erase", action="store_true", help="Apply changes instead of dry-run.")
    args = ap.parse_args()

    walk(".", erase=args.erase)
