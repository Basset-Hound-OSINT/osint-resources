# Simplified Reverse Engineering Tools List
## Free & Open Source Tools for All Platforms

---

## I. Software Reverse Engineering (SRE)

### A. Static Analysis & Code Examination

#### Disassemblers & Decompilers
- **Ghidra** - Primary tool for all architectures (Windows, Linux, macOS)
- **Radare2** - Command-line alternative with r2dec-js decompiler
- **Cutter** - GUI for Radare2
- **Jadx** - Android/Java DEX to source
- **Apktool** - Android APK disassembly/rebuild
- **dnSpy** - .NET assembly editor and debugger
- **ILSpy** - .NET decompiler
- **CFR** - Java decompiler
- **uncompyle6** - Python bytecode decompiler

#### Binary Analysis Frameworks
- **Angr** - Symbolic execution and binary analysis
- **Manticore** - Symbolic execution with taint analysis
- **Triton** - Dynamic symbolic execution
- **BinCAT** - Static binary code analysis
- **LIEF** - Library for ELF/PE/MachO manipulation
- **Capstone** - Disassembly framework

#### Code Visualization
- **Ghidra** - Built-in graph visualization

### B. Dynamic Analysis & Execution

#### Debuggers
- **GDB** - Linux primary debugger
- **GEF** - GDB Enhanced Features extension
- **pwndbg** - GDB plugin for exploit development
- **x64dbg** - Windows debugger
- **lldb** - macOS/iOS debugger
- **EDB Debugger** - Linux GUI debugger

#### Dynamic Binary Instrumentation (DBI)
- **Frida** - Cross-platform DBI (Windows, Linux, macOS, Android, iOS)
- **DynamoRIO** - Process virtualization framework
- **QBDI** - QuarkslaB Dynamic Binary Instrumentation

#### Behavior Analysis / Monitoring
- **Process Monitor (ProcMon)** - Windows (Sysinternals)
- **ProcessHacker** - Windows process viewer
- **strace** - Linux system call tracer
- **ltrace** - Linux library call tracer

### C. Evasion & Counter-Techniques

#### Unpacking & Deobfuscation
- **UPX** - Universal unpacker
- **FLOSS** - Obfuscated string extraction
- **de4dot** - .NET deobfuscator
- **Simplify** - Android bytecode simplification
- **Unipacker** - Automated unpacker

### D. Vulnerability Research & Exploitation
- **ROPgadget** - ROP gadget finder
- **angrop** - ROP chain builder (part of Angr)
- **pwntools** - CTF/exploit development framework

---

## II. Hardware Reverse Engineering (HRE)

### Firmware Analysis
- **binwalk** - Firmware analysis and extraction
- **Ghidra** - Firmware disassembly

### Bus Interface Analysis
- **OpenOCD** - JTAG debugger
- **flashrom** - Flash chip programmer

---

## III. Data Format Reverse Engineering (DFRE)

### Data Examination & Editing

#### Hex Editors
- **ImHex** - Modern hex editor with patterns
- **HexFiend** - macOS hex editor
- **wxHexEditor** - Cross-platform hex editor

#### Format Analysis
- **Kaitai Struct** - Binary format parser generator
- **file** - File type identification
- **TrID** - File identifier
- **Detect It Easy (DIE)** - PE/ELF/Mach-O analyzer
- **YARA** - Pattern matching tool

### Document Analysis
- **oletools** - Microsoft Office analysis
- **pdfid/pdf-parser** - PDF analysis (Didier Stevens)
- **peepdf** - PDF analysis and exploitation

---

## IV. Database Reverse Engineering (DBRE)

### Database Tools
- **DBeaver** - Universal database client
- **ddl-generator** - Schema generation from data

---

## V. Platform-Specific Analysis

### A. Windows Ecosystem

#### PE Analysis
- **PE-bear** - PE file analyzer
- **pestudio** - PE malware analysis
- **pefile** - Python library for PE analysis

#### .NET Analysis
- **dnSpy** - .NET debugger and editor
- **ILSpy** - .NET decompiler
- **de4dot** - .NET deobfuscator

#### Windows Internals
- **Sysinternals Suite** - Process Monitor, Process Explorer, Autoruns, etc.
- **API Monitor** - API call monitoring

### B. Linux Ecosystem

#### System Analysis
- **strace** - System call tracing
- **ltrace** - Library call tracing
- **ftrace** - Kernel function tracing
- **LIEF** - ELF manipulation

### C. Android Ecosystem

#### APK Analysis
- **Apktool** - APK decompilation/rebuild
- **Jadx** - DEX to Java decompiler
- **Mobile-Security-Framework (MobSF)** - Automated security analysis
- **Frida** - Dynamic instrumentation
- **objection** - Frida-based runtime exploration

#### Android Testing
- **Drozer** - Security assessment framework
- **QARK** - Vulnerability scanner

### D. Apple Ecosystem (macOS/iOS)

#### Mach-O Analysis
- **class-dump** - Objective-C runtime extraction
- **otool** - Mach-O analyzer (built-in)
- **jtool2** - Mach-O analysis

#### iOS Analysis
- **Frida** - Dynamic instrumentation
- **objection** - Frida-based exploration
- **iFunbox** - iOS file manager
- **ideviceinstaller** - iOS app management

---

## VI. Auxiliary & Cross-Domain Analysis

### A. Network Analysis

#### Packet Analysis
- **Wireshark** - Network protocol analyzer
- **tcpdump** - Command-line packet capture
- **Zeek (Bro)** - Network security monitor
- **mitmproxy** - Interactive HTTPS proxy
- **Burp Suite Community** - Web security testing

### B. Memory Analysis

#### Memory Forensics
- **Volatility 3** - Memory forensics framework
- **Rekall** - Memory analysis framework
- **MemProcFS** - Memory file system

#### Memory Debugging
- **Valgrind** - Memory debugging (Linux)
- **DrMemory** - Memory debugging (Windows)

### C. Cryptography & Encoding
- **CyberChef** - Data encoding/decoding web tool
- **hashcat** - Password cracking
- **John the Ripper** - Password cracking

### D. Environment Setup & Isolation

#### Sandboxes
- **Cuckoo Sandbox** - Automated malware analysis
- **CAPE Sandbox** - Config and payload extraction
- **ANY.RUN** - Interactive malware sandbox (free tier)

#### Emulators
- **QEMU** - CPU emulator
- **Unicorn** - CPU emulator framework
- **Qiling** - Advanced binary emulation

### E. Scripting & Automation

#### Scripting Frameworks
- **Ghidra** - Python/Java scripting
- **Radare2** - r2pipe for multiple languages
- **Frida** - JavaScript instrumentation
- **pwntools** - Python exploit development

#### Python Libraries
- **pefile** - PE file analysis
- **pyelftools** - ELF file parsing
- **Capstone** - Disassembly library
- **Unicorn** - Emulation library
- **angr** - Binary analysis platform

---

## VII. Specialized Tools

### Malware Analysis
- **YARA** - Malware pattern matching
- **Cuckoo Sandbox** - Automated analysis
- **FLOSS** - String extraction
- **Volatility** - Memory forensics

### Graphics/Game Debugging
- **RenderDoc** - Graphics debugger
- **apitrace** - OpenGL/DirectX tracing

### Exploit Development
- **pwntools** - CTF framework
- **ROPgadget** - ROP chain construction
- **mona.py** - Exploit development (Immunity Debugger plugin)

---

## VIII. Learning & Practice Resources

### Practice Platforms
- **crackmes.one** - Reverse engineering challenges
- **CTFtime** - CTF competition tracker
- **Hack The Box** - Penetration testing labs
- **TryHackMe** - Cybersecurity training

### Documentation & References
- **Ghidra Documentation** - Official NSA docs
- **OSDev Wiki** - Operating system development
- **Awesome Reverse Engineering** - GitHub curated list
- **Reversing.ID** - Reverse engineering knowledge base

---

## Tool Selection Philosophy

**Primary Tools (Learn These First):**
1. **Ghidra** - Universal disassembler/decompiler
2. **GDB + GEF** - Linux debugging
3. **x64dbg** - Windows debugging
4. **Frida** - Dynamic instrumentation
5. **Wireshark** - Network analysis
6. **Volatility 3** - Memory forensics
7. **Radare2/Cutter** - Command-line alternative to Ghidra

**Platform-Specific Additions:**
- **Android**: Jadx, Apktool, MobSF, objection
- **iOS**: class-dump, objection, Frida
- **.NET**: dnSpy, ILSpy, de4dot
- **Java**: CFR, Jadx
- **Python**: uncompyle6

**Workflow Tools:**
- **YARA** - Pattern matching across all platforms
- **CyberChef** - Data transformation
- **pwntools** - Automation and exploitation

---

## Installation Priority

### Tier 1 (Essential - Install First)
1. Ghidra
2. GDB + GEF (Linux) or x64dbg (Windows)
3. Frida
4. Wireshark
5. Python 3 + pip

### Tier 2 (Important - Install as Needed)
1. Radare2 + Cutter
2. Volatility 3
3. Jadx (if analyzing Android)
4. dnSpy (if analyzing .NET)
5. Burp Suite Community
6. QEMU/Unicorn

### Tier 3 (Specialized - Install for Specific Tasks)
1. Cuckoo Sandbox
2. Angr
3. ROPgadget
4. ImHex
5. Platform-specific tools as needed

---

## Notes

- **Ghidra** is prioritized over IDA Pro (not free) and Binary Ninja (not free) as the primary disassembler
- **Radare2** provides command-line alternative for those who prefer terminal workflows
- **Frida** is cross-platform and works on Windows, Linux, macOS, Android, and iOS
- All listed tools are free and open source (or have free community editions)
- Tools are selected for active maintenance and strong community support
- Focus on learning one tool deeply before moving to alternatives
