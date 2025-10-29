#!/bin/bash

# Output file
OUTPUT="tools.md"

# Clear output file if it exists
> "$OUTPUT"

# Function to extract domain/service name from URL
get_service_name() {
    local url="$1"
    # Extract domain and clean it up for display
    echo "$url" | sed -E 's|https?://||; s|www\.||; s|/.*||' | awk -F. '{print toupper(substr($1,1,1)) tolower(substr($1,2))}'
}

# Function to process a single HTML file
process_file() {
    local file="$1"
    local basename=$(basename "$file" .html)
    
    echo "## $basename" >> "$OUTPUT"
    echo "" >> "$OUTPUT"
    
    # Temporary files for collecting URLs
    temp_urls=$(mktemp)
    temp_normalized=$(mktemp)
    
    # Extract window.open URLs
    grep -oP "window\.open\('\K[^']+" "$file" 2>/dev/null | while read -r url; do
        # Remove everything after the first single quote if present
        clean_url=$(echo "$url" | cut -d"'" -f1)
        # Skip if it contains variable concatenation patterns
        if [[ ! "$clean_url" =~ \+|Search[0-9] ]]; then
            echo "$clean_url" >> "$temp_urls"
        else
            # Extract base URL for parameterized searches
            base_url=$(echo "$clean_url" | sed -E "s/'.*//; s/ \+ .*//")
            echo "$base_url" >> "$temp_urls"
        fi
    done
    
    # Extract source URLs (for video tags)
    grep -oP '<source\s+src="\K[^"]+' "$file" 2>/dev/null | while read -r url; do
        echo "$url" >> "$temp_urls"
    done
    
    # Normalize URLs: remove trailing slash and force https
    while read -r url; do
        # Remove trailing slash
        url=$(echo "$url" | sed 's:/$::')
        # Convert http:// to https://
        url=$(echo "$url" | sed 's|^http://|https://|')
        echo "$url"
    done < "$temp_urls" | sort -u > "$temp_normalized"
    
    # Format as markdown
    while read -r url; do
        service=$(get_service_name "$url")
        echo "* [$service]($url)" >> "$OUTPUT"
    done < "$temp_normalized"
    
    rm -f "$temp_urls" "$temp_normalized"
    
    echo "" >> "$OUTPUT"
}

# Find all HTML files and process them
find . -name "*.html" -type f | sort | while read -r file; do
    echo "Processing $file..."
    process_file "$file"
done

echo "Markdown file created: $OUTPUT"