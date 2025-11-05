# Malware Analysis Toolkit - Directory Structure

## Overview

This document describes the complete directory structure for the malware analysis toolkit.

## Main Toolkit Directory Structure

```
malware-analysis-toolkit/
├── static-analysis/           # Static analysis tools
│   ├── yara/
│   ├── DIE/
│   ├── floss/
│   ├── pe-bear/
│   ├── oletools/
│   ├── DidierStevensSuite/
│   ├── peepdf/
│   └── CyberChef/
│
├── dynamic-analysis/          # Dynamic analysis tools
│   ├── Noriben/
│   ├── flare-fakenet-ng/
│   └── SysinternalsSuite/     # Windows only
│
├── memory-analysis/           # Memory forensics tools
│   └── volatility3/
│
├── network-analysis/          # Network monitoring tools
│   ├── wireshark/
│   └── zeek/
│
├── debuggers/                 # Debugging tools
│   ├── gdb-gef/
│   ├── radare2/
│   └── x64dbg/               # Windows only
│
├── unpacking/                 # Unpacking and deobfuscation
│   ├── upx/
│   └── de4dot/
│
├── specialized/               # Specialized analysis tools
│   ├── jadx/                 # Android
│   ├── Mobile-Security-Framework-MobSF/
│   └── malwoverview/
│
├── automation-scripts/        # Helper scripts
│   ├── quick_triage.py
│   ├── bulk_hash.py
│   └── ioc_extractor.py
│
└── TOOLS_INVENTORY.md        # Complete tool list

```

## Per-Analysis Workspace Structure

When you run `setup_malware_analysis.sh`, it creates the following structure:

```
[analysis-name]/
│
├── 1-sample-info/
│   ├── sample_info.txt                    # Basic sample metadata
│   ├── [sample-name].malz                 # Malware sample (read-only)
│   └── README.md
│
├── 2-static-analysis/
│   ├── strings/
│   │   ├── all_strings.txt
│   │   ├── interesting_strings.txt
│   │   ├── urls.txt
│   │   ├── ips.txt
│   │   └── README.md
│   ├── pe-analysis/                       # For Windows executables
│   │   ├── pe_structure.txt
│   │   ├── imports.txt
│   │   ├── exports.txt
│   │   ├── sections.txt
│   │   └── README.md
│   ├── signatures/
│   │   ├── yara_matches.txt
│   │   ├── antivirus_results.txt
│   │   └── README.md
│   ├── disassembly/
│   │   ├── main_disasm.asm
│   │   ├── functions_list.txt
│   │   └── README.md
│   ├── decompilation/
│   │   ├── decompiled_code/
│   │   └── README.md
│   ├── resources/
│   │   ├── extracted_resources/
│   │   ├── icons/
│   │   └── README.md
│   └── README.md
│
├── 3-dynamic-analysis/
│   ├── behavioral/
│   │   ├── execution_log.txt
│   │   ├── behavioral_indicators.txt
│   │   └── README.md
│   ├── process-monitoring/
│   │   ├── process_tree.txt
│   │   ├── child_processes.txt
│   │   ├── procmon_log.csv              # Windows
│   │   └── README.md
│   ├── file-system/
│   │   ├── files_created.txt
│   │   ├── files_modified.txt
│   │   ├── files_deleted.txt
│   │   └── README.md
│   ├── registry/                         # Windows only
│   │   ├── registry_changes.txt
│   │   ├── persistence_keys.txt
│   │   └── README.md
│   ├── api-calls/
│   │   ├── api_monitor_log.txt
│   │   ├── suspicious_calls.txt
│   │   └── README.md
│   └── README.md
│
├── 4-memory-analysis/
│   ├── dumps/
│   │   └── memory_dump.raw
│   ├── volatility-output/
│   │   ├── pslist.txt
│   │   ├── pstree.txt
│   │   ├── netscan.txt
│   │   ├── malfind.txt
│   │   └── cmdline.txt
│   └── README.md
│
├── 5-network-analysis/
│   ├── pcap/
│   │   ├── capture.pcap
│   │   └── filtered_traffic.pcap
│   ├── dns-queries/
│   │   ├── dns_requests.txt
│   │   └── suspicious_domains.txt
│   ├── http-traffic/
│   │   ├── http_requests.txt
│   │   ├── downloaded_payloads/
│   │   └── README.md
│   ├── indicators/
│   │   ├── c2_servers.txt
│   │   ├── contacted_ips.txt
│   │   └── README.md
│   └── README.md
│
├── 6-extracted-artifacts/
│   ├── configs/                          # Extracted configurations
│   ├── payloads/                         # Dropped payloads
│   ├── decrypted/                        # Decrypted strings/files
│   ├── embedded-files/                   # Embedded executables
│   └── README.md
│
├── 7-reports/
│   ├── [analysis-name]_report.md         # Main report
│   ├── [analysis-name]_iocs.txt          # Indicators of Compromise
│   ├── [analysis-name]_timeline.txt      # Event timeline
│   └── README.md
│
├── 8-automation-scripts/
│   ├── pe_analyzer.py
│   ├── string_analyzer.py
│   ├── dynamic_monitor.py
│   ├── memory_analyzer.py
│   ├── network_parser.py
│   ├── ioc_extractor.py
│   └── report_generator.py
│
├── 9-notes-references/
│   ├── analysis_notes.md
│   ├── similar_samples.md
│   ├── threat_intel.md
│   └── references.md
│
├── set_analysis_env.sh                   # Environment configuration
├── QUICK_START.md                        # Quick reference guide
└── README.md

```

## Script Templates Directory

This is where you store your command templates before running setup:

```
script-directory/
├── setup_malware_analysis.sh
├── download_malware_tools.sh
│
├── Analysis_Templates/
│   ├── 2-static-analysis/
│   │   ├── strings/
│   │   │   └── README.md
│   │   ├── pe-analysis/
│   │   │   └── README.md
│   │   ├── signatures/
│   │   │   └── README.md
│   │   └── README.md
│   ├── 3-dynamic-analysis/
│   │   ├── behavioral/
│   │   │   └── README.md
│   │   └── README.md
│   ├── 5-network-analysis/
│   │   └── README.md
│   └── 7-reports/
│       └── report_template.md
│
└── Automation_Scripts/
    ├── pe_analyzer.py
    ├── string_analyzer.py
    ├── dynamic_monitor.py
    ├── memory_analyzer.py
    ├── network_parser.py
    ├── ioc_extractor.py
    └── report_generator.py
```

## Environment Variables

After running `setup_malware_analysis.sh`, the following environment variables are available:

```bash
# Sample Information
SAMPLE_FILE          # Path to malware sample in workspace
SAMPLE_ORIGINAL      # Original path to sample
SAMPLE_NAME          # Filename of the sample
SAMPLE_HASH          # SHA256 hash
SAMPLE_TYPE          # File type (exe, dll, pdf, etc.)

# Analysis Information
ANALYSIS_DIR         # Root of analysis workspace
ANALYSIS_OS          # Operating system (linux/windows)
ANALYSIS_DATE        # Timestamp of analysis start

# Tool Directories
MALWARE_TOOLKIT_DIR  # Root of toolkit installation
STATIC_TOOLS_DIR     # Static analysis tools
DYNAMIC_TOOLS_DIR    # Dynamic analysis tools
MEMORY_TOOLS_DIR     # Memory analysis tools

# Output Directories
STATIC_OUTPUT        # Static analysis output
DYNAMIC_OUTPUT       # Dynamic analysis output
MEMORY_OUTPUT        # Memory analysis output
NETWORK_OUTPUT       # Network analysis output
ARTIFACTS_DIR        # Extracted artifacts
REPORTS_DIR          # Final reports
```

## Usage Example

```bash
# 1. Download and install tools
./download_malware_tools.sh

# 2. Create analysis workspace
./setup_malware_analysis.sh -f /path/to/malware.exe -n "wannacry_analysis" -t exe

# 3. Enter workspace and load environment
cd wannacry_analysis
source set_analysis_env.sh

# 4. Now all commands can use environment variables
echo $SAMPLE_FILE
# Output: /home/user/wannacry_analysis/1-sample-info/malware.exe.malz

# 5. Run analysis scripts
python3 8-automation-scripts/pe_analyzer.py
python3 8-automation-scripts/string_analyzer.py

# 6. All outputs go to proper directories automatically
```

## Template Placeholders

In your markdown templates, use these placeholders (they'll be replaced automatically):

- `${ANALYSIS_NAME}` - Name of the analysis
- `${SAMPLE_FILE}` - Path to sample in workspace
- `${SAMPLE_NAME}` - Filename of sample
- `${SAMPLE_HASH}` - SHA256 hash
- `${ANALYSIS_DATE}` - Date/time of analysis
- `${ANALYSIS_DIR}` - Workspace directory
- `${STATIC_OUTPUT}` - Static analysis output directory
- `${DYNAMIC_OUTPUT}` - Dynamic analysis output directory
- `${MEMORY_OUTPUT}` - Memory analysis output directory
- `${NETWORK_OUTPUT}` - Network analysis output directory
- `${ARTIFACTS_DIR}` - Artifacts directory
- `${REPORTS_DIR}` - Reports directory

## Benefits of This Structure

1. **Consistent Organization** - Every analysis follows the same structure
2. **Environment Variables** - Scripts can reference files without hardcoding paths
3. **Portable** - Copy entire analysis directory to share with team
4. **Automated** - Templates are copied and configured automatically
5. **Safe** - Malware samples are isolated and marked clearly
6. **Scalable** - Easy to analyze multiple samples simultaneously
7. **Documented** - README files in every directory explain purpose