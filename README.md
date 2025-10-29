# OSINT Resources

## Table of Contents

- [OSINT Resources](#osint-resources)
  - [How to Use This Documentation](#how-to-use-this-documentation)
  - [Structure](#structure)
  - [Integration Into Basset Hound (In Progress)](#integration-into-basset-hound-(in-progress))

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

1. Add information to a profile in basset-hound
2. For every piece of PII, be able to run OSINT tools against it
   1. Command line tools, ideally automated with docker
   2. Web based tools, ideally automated with a browser extension
3. Be able to configure/select what tools to run agains select PII

## combine_references.py
> Python script to help digest links in Markdown files 