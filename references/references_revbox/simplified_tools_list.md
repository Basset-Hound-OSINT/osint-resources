# Simplified Reverse Engineering Tools List
## Free & Open Source Tools for All Platforms

---

## I. Software Reverse Engineering (SRE)

### A. Static Analysis & Code Examination

#### Disassemblers & Decompilers
- [**Ghidra**](https://github.com/NationalSecurityAgency/ghidra) - Primary tool for all architectures (Windows, Linux, macOS)
- [**Radare2**](https://github.com/radareorg/radare2) - Command-line alternative with r2dec-js decompiler
- [**Cutter**](https://github.com/rizinorg/cutter) - GUI for Radare2
- [**Jadx**](https://github.com/skylot/jadx) - Android/Java DEX to source
- [**Apktool**](https://github.com/ibotpeaches/apktool) - Android APK disassembly/rebuild
- [**dnSpy**](https://github.com/dnSpy/dnSpy) - .NET assembly editor and debugger
- [**ILSpy**](https://github.com/icsharpcode/ilspy) - .NET decompiler
- [**CFR**](https://github.com/leibnitz27/cfr) - Java decompiler
- [**uncompyle6**](https://github.com/rocky/python-uncompyle6) - Python bytecode decompiler

#### Binary Analysis Frameworks
- [**Angr**](https://github.com/angr/angr) - Symbolic execution and binary analysis
- [**Manticore**](https://github.com/trailofbits/manticore) - Symbolic execution with taint analysis
- [**Triton**](https://github.com/JonathanSalwan/Triton) - Dynamic symbolic execution
- [**BinCAT**](https://github.com/airbus-seclab/bincat) - Static binary code analysis
- [**LIEF**](https://github.com/lief-project/lief) - Library for ELF/PE/MachO manipulation
- [**Capstone**](https://github.com/aquynh/capstone) - Disassembly framework

#### Code Visualization

### B. Dynamic Analysis & Execution

#### Debuggers
- [**GDB**](sudo apt install gdb) - Linux primary debugger
- [**GEF**](https://github.com/hugsy/gef) - GDB Enhanced Features extension
- [**pwndbg**](https://github.com/pwndbg/pwndbg) - GDB plugin for exploit development
- [**x64dbg**](https://github.com/x64dbg/x64dbg) - Windows debugger
- [**lldb**](https://github.com/llvm-mirror/lldb) - macOS/iOS debugger
- [**EDB Debugger**](https://github.com/eteran/edb-debugger) - Linux GUI debugger

#### Dynamic Binary Instrumentation (DBI)
- [**Frida**](https://github.com/frida/frida) - Cross-platform DBI (Windows, Linux, macOS, Android, iOS)
- [**DynamoRIO**](https://github.com/dynamorio/dynamorio) - Process virtualization framework
- [**QBDI**](https://github.com/qbdi/qbdi) - QuarkslaB Dynamic Binary Instrumentation

#### Behavior Analysis / Monitoring
- [**Process Monitor (ProcMon)**](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon) - Windows (Sysinternals)
- [**ProcessHacker**](https://github.com/processhacker/processhacker) - Windows process viewer
- **strace** - Linux system call tracer (built-in)
- **ltrace** - Linux library call tracer (built-in)

### C. Evasion & Counter-Techniques

#### Unpacking & Deobfuscation
- [**UPX**](https://github.com/upx/upx) - Universal unpacker
- [**FLOSS**](https://github.com/mandiant/flare-floss) - Obfuscated string extraction
- [**de4dot**](https://github.com/de4dot/de4dot) - .NET deobfuscator
- [**Simplify**](https://github.com/calebfenton/simplify) - Android bytecode simplification
- [**Unipacker**](https://github.com/unipacker/unipacker) - Automated unpacker

### D. Vulnerability Research & Exploitation
- [**ROPgadget**](https://github.com/jonathansalwan/ropgadget) - ROP gadget finder
- [**angrop**](https://github.com/salls/angrop) - ROP chain builder (part of Angr)
- [**pwntools**](https://github.com/gallopsled/pwntools) - CTF/exploit development framework

---

## II. Hardware Reverse Engineering (HRE)

### Firmware Analysis
- [**binwalk**](https://github.com/rampageX/firmware-mod-kit) - Firmware analysis and extraction

### Bus Interface Analysis
- [**OpenOCD**](https://github.com/openocd-org/openocd) - JTAG debugger
- [**flashrom**](https://github.com/flashrom/flashrom) - Flash chip programmer

---

## III. Data Format Reverse Engineering (DFRE)

### Data Examination & Editing

#### Hex Editors
- [**ImHex**](https://github.com/ImHex/ImHex) - Modern hex editor with patterns
- [**HexFiend**](https://github.com/HexFiend/HexFiend) - macOS hex editor
- [**wxHexEditor**](https://github.com/wxHexEditor/wxHexEditor) - Cross-platform hex editor

#### Format Analysis
- [**Kaitai Struct**](https://github.com/kaitai-io/kaitai_struct) - Binary format parser generator
- **file** - File type identification (built-in on Unix systems)
- [**TrID**](https://mark0.net/soft-trid-e.html) - File identifier
- [**Detect It Easy (DIE)**](https://github.com/horsicq/Detect-It-Easy) - PE/ELF/Mach-O analyzer
- [**YARA**](https://github.com/VirusTotal/yara) - Pattern matching tool

### Document Analysis
- [**oletools**](https://github.com/decalage2/oletools) - Microsoft Office analysis
- [**pdfid/pdf-parser**](https://github.com/DidierStevens/DidierStevensSuite) - PDF analysis (Didier Stevens)
- [**peepdf**](https://github.com/jesparza/peepdf) - PDF analysis and exploitation

---

## IV. Database Reverse Engineering (DBRE)

### Database Tools
- [**DBeaver**](https://github.com/dbeaver/dbeaver) - Universal database client
- [**ddl-generator**](https://github.com/ddl-generator) - Schema generation from data

---

## V. Platform-Specific Analysis

### A. Windows Ecosystem

#### PE Analysis
- [**PE-bear**](https://github.com/hasherezade/pe-bear) - PE file analyzer
- [**pestudio**](https://www.winitor.com/tools/pestudio/current/pestudio.zip) - PE malware analysis
- [**pefile**](https://github.com/erocarrera/pefile) - Python library for PE analysis

#### .NET Analysis

#### Windows Internals
- [**Sysinternals Suite**](https://docs.microsoft.com/en-us/sysinternals/) - Process Monitor, Process Explorer, Autoruns, etc.
- **API Monitor** - API call monitoring

### B. Linux Ecosystem

#### System Analysis
- **strace** - System call tracing (built-in)
- **ltrace** - Library call tracing (built-in)
- **ftrace** - Kernel function tracing (built-in)

### C. Android Ecosystem

#### APK Analysis
- [**Mobile-Security-Framework (MobSF)**](https://github.com/mobsf/mobile-security-framework-mobsf) - Automated security analysis
- [**objection**](https://github.com/sensepost/objection) - Frida-based runtime exploration

#### Android Testing
- [**Drozer**](https://github.com/fsecurelabs/drozer) - Security assessment framework
- [**QARK**](https://github.com/linkedin/qark) - Vulnerability scanner

### D. Apple Ecosystem (macOS/iOS)

#### Mach-O Analysis
- [**class-dump**](https://github.com/nygard/class-dump) - Objective-C runtime extraction
- **otool** - Mach-O analyzer (built-in on macOS)
- **jtool2** - Mach-O analysis

#### iOS Analysis
- **iFunbox** - iOS file manager
- **ideviceinstaller** - iOS app management

---

## VI. Auxiliary & Cross-Domain Analysis

### A. Network Analysis

#### Packet Analysis
- [**Wireshark**](sudo apt install wireshark) - Network protocol analyzer
- **tcpdump** - Command-line packet capture (built-in on Unix systems)
- [**Zeek (Bro)**](https://github.com/zeek/zeek) - Network security monitor
- [**mitmproxy**](https://github.com/mitmproxy/mitmproxy) - Interactive HTTPS proxy
- [**Burp Suite Community**](sudo apt install burpsuite) - Web security testing

### B. Memory Analysis

#### Memory Forensics
- [**Volatility 3**](https://github.com/volatilityfoundation/volatility3) - Memory forensics framework
- [**Rekall**](https://github.com/google/rekall) - Memory analysis framework
- [**MemProcFS**](https://github.com/ufrisk/MemProcFS) - Memory file system

#### Memory Debugging
- [**Valgrind**](sudo apt install valgrind) - Memory debugging (Linux)
- [**DrMemory**](https://github.com/dynamorio/drmemory) - Memory debugging (Windows)

### C. Cryptography & Encoding
- [**CyberChef**](https://gchq.github.io/CyberChef/) - Data encoding/decoding web tool
- [**hashcat**](sudo apt install hashcat hashcat-utils) - Password cracking
- [**John the Ripper**](sudo apt install john) - Password cracking

### D. Environment Setup & Isolation

#### Sandboxes
- [**Cuckoo Sandbox**](https://github.com/cuckoosandbox/cuckoo) - Automated malware analysis
- [**CAPE Sandbox**](https://github.com/kevoreilly/CAPEv2) - Config and payload extraction
- [**ANY.RUN**](https://app.any.run/) - Interactive malware sandbox (free tier)

#### Emulators
- [**QEMU**](https://github.com/qemu/qemu) - CPU emulator
- [**Unicorn**](https://github.com/unicorn-engine/unicorn) - CPU emulator framework
- [**Qiling**](https://github.com/qilingframework/qiling) - Advanced binary emulation

### E. Scripting & Automation

#### Scripting Frameworks

#### Python Libraries
- [**pyelftools**](https://github.com/eliben/pyelftools) - ELF file parsing
- [**Capstone**](https://github.com/capstone-engine/capstone) - Disassembly library

```bash
pip install pefile pyelftools capstone unicorn angr
```

---

## VII. Specialized Tools

### Malware Analysis

### Graphics/Game Debugging
- [**RenderDoc**](https://github.com/baldurk/renderdoc) - Graphics debugger
- [**apitrace**](https://github.com/apitrace/apitrace) - OpenGL/DirectX tracing

### Exploit Development
- **mona.py** - Exploit development (Immunity Debugger plugin)

### Docker Images Summary

Here are useful pre-built Docker images:

**Analysis Environments**

- [remnux/remnux-distro](https://hub.docker.com/r/remnux/remnux-distro)
- [blacktop/yara](https://hub.docker.com/r/blacktop/yara)
- [blacktop/volatility](https://hub.docker.com/r/blacktop/volatility)
- [radare/radare2](https://hub.docker.com/r/radare/radare2)

**Sandboxes**

- [blacktop/cuckoo](https://hub.docker.com/r/blacktop/cuckoo)
- [capesandbox/cape](https://hub.docker.com/r/capesandbox/cape)

**Mobile**

- [opensecurity/mobile-security-framework-mobsf](https://hub.docker.com/r/opensecurity/mobile-security-framework-mobsf)

**Network**

- [zeek/zeek](https://hub.docker.com/r/zeek/zeek)
- [sysdig/sysdig](https://hub.docker.com/r/sysdig/sysdig)

**Specialized**

- [blacktop/pe-tools](https://hub.docker.com/r/blacktop/pe-tools)
- [remnux/peepdf](https://hub.docker.com/r/remnux/peepdf)


---

**Platform-Specific Additions:**

**Workflow Tools:**

---

## Installation Priority

### Tier 1 (Essential - Install First)
4. [Wireshark](sudo apt install wireshark)
5. Python 3 + pip

### Tier 2 (Important - Install as Needed)
5. [Burp Suite Community](sudo apt install burpsuite)

### Tier 3 (Specialized - Install for Specific Tasks)
5. Platform-specific tools as needed

## Notes

- **Ghidra** is prioritized over IDA Pro (not free) and Binary Ninja (not free) as the primary disassembler
- **Radare2** provides command-line alternative for those who prefer terminal workflows
- **Frida** is cross-platform and works on Windows, Linux, macOS, Android, and iOS
- All listed tools are free and open source (or have free community editions)
- Tools are selected for active maintenance and strong community support
- Focus on learning one tool deeply before moving to alternatives
