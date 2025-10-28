# OSINT Resources

## Table of Contents

- [OSINT Resources](#osint-resources)
  - [How to Use This Documentation](#how-to-use-this-documentation)
  - [Structure](#structure)
  - [Integration Into Basset Hound (In Progress)](#integration-into-basset-hound-(in-progress))
  - [ref_formatter.py](#ref_formatter.py)
  - [ref_checker.py](#ref_checker.py)

This documentation is organized by data types and intelligence categories to help you quickly find the right tools for your investigation.

## How to Use This Documentation

1. **Start with what you have**: Navigate to the data type you possess (email, username, IP address, etc.)
2. **Find relevant tools**: Each section contains tools that accept that specific data type as input
3. **Follow the methodology**: Use the Intelligence Management section for workflow guidance
4. **Document your findings**: Use the Reporting section for output generation

## Structure

- **Data Types & Identifiers**: Tools for analyzing personal identifiers you already have
- **Digital Presence**: Social media and online platform investigation tools
- **Technical Identifiers**: Network and infrastructure analysis tools
- **File & Media Analysis**: Tools for analyzing files and media (local processing)
- **Discovery Tools**: Web-based search and discovery tools
- **Public Records**: Official database and records searches
- **Financial Intelligence**: Financial tracking and analysis
- **Breach & Leak Intelligence**: Compromised data sources
- **Cloud & Infrastructure**: Hosting and CDN analysis
- **Specialized Environments**: Dark web and streaming platforms
- **Intelligence Management**: Workflow and automation
- **Reporting**: Documentation and report generation


## Integration Into Basset Hound (In Progress)

The gist for web tools:

1. Add information to a profile in basset-hound
2. Open the osint tab from the profile
3. Modify the autopopulate form from the osint tab
   1. This will change the information that you can select to populate the osint tools webpage with
   2. when you click ***Open*** on a web tool, it will open the webpage
4. Click on the Basset-Hound Autopopulate extension icon
5. Select the information you want to populate
6. Click on the ***Autopopulate*** button
7. The information will be populated in the fields of the webpage 

The gist for command line tools:
1. Add information to a profile in basset-hound
2. Open the osint tab from the profile
3. Modify the autopopulate form from the osint tab
   1. This will change the information that you can select to populate the osint tools command line with
   2. when you click ***Copy*** on a command line tool, it will copy a bash script to the clipboard
4. Open the terminal application, or whatever terminal you use
5. Make a new bash file
6. Paste the copied bash script into the bash file

## ref_formatter.py
> Python script to help format Markdown files with OSINT Resources 

Perform formatting on all markdown file in a given directory.

```
for file in ./references/*.md; do python3 ./references/ref_formatter.py -o ./new_refs/tmp_refs/ -f ${file}; done
```

## ref_checker.py
> Python script to help check that a url has not been mentioned amongst other OSINT Resources

Following the local folder example of **ref_formatter.py** for this repo

```
for file in ./new_refs/tmp_refs/*.md; do python3 ./references/ref_checker.py -c ./src/ -o ./new_refs/tmp_ref_checks/ -f ${file}; done
```