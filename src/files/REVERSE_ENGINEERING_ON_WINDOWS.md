# Windows-Only Reverse Engineering Tools
## Free & Open Source Tools for Windows

---

## I. Software Reverse Engineering (SRE)

### A. Static Analysis & Code Examination

#### PE Analysis
- [**PE-bear**](https://github.com/hasherezade/pe-bear) - PE file analyzer
- [**pestudio**](https://www.winitor.com/tools/pestudio/current/pestudio.zip) - PE malware analysis
- [**pefile**](https://github.com/erocarrera/pefile) - Python library for PE analysis

#### .NET Analysis
- [**dnSpy**](https://github.com/dnSpy/dnSpy) - .NET debugger and assembly editor (Windows-only WPF application)
- [**de4dot**](https://github.com/de4dot/de4dot) - .NET deobfuscator

#### Format Analysis
- [**TrID**](https://mark0.net/download/trid_win64.zip) - File identifier

### B. Dynamic Analysis & Execution

#### Debuggers
- [**x64dbg**](https://github.com/x64dbg/x64dbg) - Windows debugger (x86/x64)

#### Behavior Analysis / Monitoring
- [**Process Monitor (ProcMon)**](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon) - Windows (Sysinternals)
- [**ProcessHacker**](https://github.com/processhacker/processhacker) - Windows process viewer

### C. Windows Internals
- [**Sysinternals Suite**](https://docs.microsoft.com/en-us/sysinternals/) - Process Monitor, Process Explorer, Autoruns, etc.
- **API Monitor** - API call monitoring

### IOS

- [**iFunbox**](http://dl.i-funbox.com/ifunbox_setup.exe?7/8/2015.exe)
---

## II. Memory Analysis

### Memory Debugging
- [**DynamoRIO**](https://github.com/DynamoRIO/dynamorio) - Dynamic Instrumentation Tool Platform
- [**DrMemory**](https://github.com/dynamorio/drmemory) - Memory debugging for Windows

---

## Installation Priority

### Tier 1 (Essential - Install First)

### Tier 2 (Important - Install as Needed)

### Tier 3 (Specialized - Install for Specific Tasks)
2. API Monitor

---

## Notes

- **x64dbg** is the primary Windows debugger for reverse engineering
- **Sysinternals Suite** is essential for Windows system analysis
- **dnSpy** is Windows-only but extremely powerful for .NET analysis
- All listed tools are specifically designed for Windows and do not have native Linux/macOS versions
- For cross-platform reverse engineering, see the main tools.md file
