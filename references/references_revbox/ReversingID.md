# Awesome Software Reverse Engineering

A curated list of awesome reverse engineering resources to make you better!

Managed by Reversing.ID for the reversing community.

## Introduction

`Software Reverse Engineering` focus on code, related data, and architecture which build a complete software.

The goals:

- Recover lost information, or to make documentation.
- Detect side effects (bugs, backdoor, vulnerabilities)
- Synthesis higher abstraction.
- Facilitate reuse.

In most case, the target of Software Reversing is code in compiled form (native or intermediate), either executable or libraries.

## Table of Contents

- Resources
- [Books](#books)
- [White Papers](#hite-papers)
- [Articles](#articles)
- [Courses](#courses)
- [Channels](#channels)
- [Practices](#practices)
- [References](#references)
- Tools
- [Hex Editors](#hex-editors)
- [Binary Format](#binary-format)
- [Bytecode Editor](#bytecode-editors)
- [Disassemblers & Decompilers](#disassemblers--decompilers)
- [Debuggers](#debuggers)
- [Behavior Analysis](#behavior-analysis)
- [Dynamic Binary Instrumentation](#dynamic-binary-instrumentation)
- [Binary Analysis Framework](#binary-analysis-framework)
- [Code Emulators](#code-emulators)
- [Injectors](#injectors)
- [HTTP Intercept Proxy](#http-intercept-proxy)
- [Reconstructors](#reconstructors)
- [Unpackers](#unpackers)
- [Obfuscators](#obfuscators)
- [Deobfuscators](#deobfuscators)
- [Binary Visualization](#binary-visualization)
- [Document Analysis](#document-analysis)
- [Misc](#misc)
- Scripting
- [IDA Pro](#ida-script)
- [Ghidra](#ghidra-script)

- - -

## Books

Reversing Concept

* [Reverse Engineering for Beginners](http://beginners.re/)
* [Practical Reverse Engineering](http://amzn.com/B00IA22R2Y)
* [Reversing: Secrets of Reverse Engineering](http://amzn.com/B007032XZK)
* [Practical Malware Analysis](http://amzn.com/1593272901)

Tools

* [The IDA Pro Book](http://amzn.com/1593272898)

Assembly and languages

* [Assembly Language for Intel-Based Computers (5th Edition) ](http://a.co/4OR6I9U)

Specific topic on Software Reverse Engineering

* [Windows Internals Part 1](http://amzn.com/0735648735) [Part 2](http://amzn.com/0735665877)
* [Inside Windows Debugging](http://amzn.com/0735662789)
* [iOS Reverse Engineering](https://github.com/iosre/iOSAppReverseEngineering)

## White Papers

* [Next Generation debugger for reverse engineering](https://www.blackhat.com/presentations/bh-europe-07/ERSI/Whitepaper/bh-eu-07-ersi-WP-apr19.pdf)
* [Behind Enemy Lines Reverse Engineering C++ in Modern Ages](https://corecppil.github.io/CoreCpp2019/Presentations/Gal_Behind_Enemy_Lines_Reverse_Engineering_Cpp_in_Modern_Ages.pdf)
* [Overcoming Java Vulnerabilities](https://www2.gemalto.com/download/OvercomingJavaVulnerabilities_WP_(A4)_web.pdf)
* [Reverse engineering tools review](https://www.pelock.com/articles/reverse-engineering-tools-review)

## Articles

* [Intercepting DLL libraries calls. API hooking in practice](https://www.pelock.com/articles/intercepting-dll-libraries-calls-api-hooking-in-practice)
* [Windows Hot Patching Mechanism Explained](https://dev.to/pelock/windows-hot-patching-mechanism-explained-2m1f)
* [How to write a CrackMe for a CTF competition](https://www.pelock.com/articles/how-to-write-a-crackme-for-a-ctf-competition)
* [Code of destruction – malware analysis](https://www.pelock.com/articles/code-of-destruction-malware-analysis)
* [Polymorphic Encryption Algorithms](https://www.pelock.com/articles/polymorphic-encryption-algorithms)
* [Reversing reading]() - coming soon.

## Courses

*Reverse Engineering Courses*

* [Lenas Reversing for Newbies](https://tuts4you.com/download.php?list.17)
* [Open Security Training](http://opensecuritytraining.info/Training.html)
* [Dr. Fu's Malware Analysis](http://fumalwareanalysis.blogspot.sg/p/malware-analysis-tutorials-reverse.html)
* [Binary Auditing Course](http://www.binary-auditing.com/)
* [TiGa's Video Tutorials](http://www.woodmann.com/TiGa/)
* [Legend of Random](https://tuts4you.com/download.php?list.97)
* [Practical Malware Analysis](https://samsclass.info/126/126_S17.shtml)
* [Modern Binary Exploitation](http://security.cs.rpi.edu/courses/binexp-spring2015/)
* [RPISEC Malware Course](https://github.com/RPISEC/Malware)
* [begin.re](https://www.begin.re/)
* [RE101](https://securedorg.github.io/RE101/)
* [RE102](https://securedorg.github.io/RE102/)
* [ARM Assembly Basics](https://azeria-labs.com/writing-arm-assembly-part-1/)
* [Offensive and Defensive Android Reversing](https://github.com/rednaga/training/raw/master/DEFCON23/O%26D%20-%20Android%20Reverse%20Engineering.pdf)

## Channels

*Binary Analysis Channels*

* [OALabs](https://www.youtube.com/channel/UC--DwaiMV-jtO-6EvmKOnqg)
* [MalwareTech](https://www.youtube.com/channel/UCLDnEn-TxejaDB8qm2AUhHQ)
* [GynvaelEN](https://www.youtube.com/user/GynvaelEN)
* [VirusBtn](https://www.youtube.com/user/virusbtn)
* [Intro to WinDBG](https://www.youtube.com/playlist?list=PLhx7-txsG6t6n_E2LgDGqgvJtCHPL7UFu)
* [hasherzade](https://www.youtube.com/channel/UCNWVswPNgn5kutPNa5sprkg)
* [Colin Hardy](https://www.youtube.com/channel/UCND1KVdVt8A580SjdaS4cZg)
* [MalwareAnalysisHedgehog](https://www.youtube.com/channel/UCVFXrUwuWxNlm6UNZtBLJ-A)
* [LiveOverflow](https://www.youtube.com/watch?v=iyAyN3GFM7A&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN)

## Practices

*Practice Reverse Engineering*

* [Reversing.ID Crackmes Repository](https://github.com/ReversingID/Crackmes-Repository/)
* [Crackmes.one](http://www.crackmes.one/)
* [OSX Crackmes](https://reverse.put.as/crackmes/)
* [ESET Challenges](http://www.joineset.com/jobs-analyst.html)
* [Flare-on Challenges](http://flare-on.com/)
* [Github CTF Archives](http://github.com/ctfs/)
* [Reverse Engineering Challenges](http://challenges.re/)
* [xorpd Advanced Assembly Exercises](http://www.xorpd.net/pages/xchg_rax/snip_00.html)
* [Virusshare.com](http://virusshare.com/)
* [Contagio](http://contagiodump.blogspot.com/)
* [Malware-Traffic-Analysis](https://malware-traffic-analysis.com/)
* [Malshare](http://malshare.com/)
* [Malware Blacklist](http://www.malwareblacklist.com/showMDL.php)
* [malwr.com](https://malwr.com/)
* [vxvault](http://vxvault.net/)

## References

Learning Assembly

* [Low-level Code Reference](https://github.com/ReversingID/LowLevelCode-Reference)
* [Assembly code size optimization tricks](https://dev.to/pelock/assembly-code-size-optimization-tricks-2abd)
* [When and how to use an assembler. Assembly programming basics](https://www.pelock.com/articles/when-and-how-to-use-an-assembler-assembly-programming-basics)

Intermediate Representation

* [LLVM IR](https://llvm.org/docs/LangRef.html)
* [REIL](https://www.zynamics.com/binnavi/manual/html/reil_language.htm)
* [OpenREIL](https://github.com/Cr4sh/openreil)

- - -

## Hex Editors

Hex editor lets you view/edit the binary data of a file.

Multi/cross platform

* [010 Editor](http://www.sweetscape.com/010editor/)
* [wxHexEditor](https://www.wxhexeditor.org/)

Windows

* [HxD](https://mh-nexus.de/en/hxd/)
* [Hex Workshop](http://www.hexworkshop.com/)
* [Hexinator](https://hexinator.com/)
* [HIEW](http://www.hiew.ru/)

Mac OS X

* [HexFiend](http://ridiculousfish.com/hexfiend/)

## Binary Format

File information and format identifier

* [file](https://linux.die.net/man/1/file)
* [TrID](http://mark0.net/soft-trid-e.html)
* [nm](https://linux.die.net/man/1/nm) - view symbols

Executable detector

* [Detect It Easy](http://ntinfo.biz/)
* [PEiD](https://tuts4you.com/download.php?view.398)

Executable explorer

* [CFF Explorer](http://www.ntcore.com/exsuite.php)
* [Cerbero Profiler](http://cerbero.io/profiler/)  //  [Lite PE Insider](http://cerbero.io/peinsider/)
* [PeStudio](http://www.winitor.com/)
* [PPEE](https://www.mzrst.com/)
* [PE Bear](https://hshrzd.wordpress.com/pe-bear/)
* [MachoView](https://github.com/gdbinit/MachOView)

Dependency check

* [DependencyWalker](http://www.dependencywalker.com/)
* [slid](https://github.com/arvinddoraiswamy/slid) - statically linked library detector.

Format parser and modification

* [ImHex](https://github.com/WerWolv/ImHex) - explore, edit, and represent binary structure with C++-like pattern language.
* [Kaitai Struct](https://kaitai.io) - develop format parsers by declarative approach
* [LIEF](https://lief.quarkslab.com/) - Library to Instrument Executable Formats, easily parse, modify and abstract many file formats.
* [QuickBMS](http://aluigi.altervista.org/quickbms.htm) - easily extract and modify file format with support of encryption, compressions, obfuscation, and other algorithms.

## Bytecode Editors

Java bytecode editor

* [Recaf](https://github.com/Col-E/Recaf)
* [JByteMode](https://github.com/GraxCode/JByteMod-Beta)
* [dirtyJOE](http://dirty-joe.com/)

## Disassemblers & Decompilers

Native code disassembler and decompiler

* [Ghidra](https://ghidra-sre.org/)
* [IDA Pro](https://www.hex-rays.com/products/ida/index.shtml)
* [Binary Ninja](https://binary.ninja/)
* [Relyze Desktop](https://relyze.com)
* [Radare2](http://www.radare.org/r/) // [Cutter](https://cutter.re)
* [Hopper](http://hopperapp.com/)
* [fREedom](https://github.com/cseagle/fREedom)
* [Retdec](https://retdec.com/)
* [Snowman](https://derevenets.com/)
* [objdump](http://linux.die.net/man/1/objdump)
* [Medussa](https://github.com/wisk/medusa)
* [Plasma](https://github.com/joelpx/plasma)
* [Capstone](http://www.capstone-engine.org/) - lightweight multi-platform, multi-architecture disassembly framework based on LLVM.
* [distorm3](https://github.com/gdabah/distorm) - lightweight library for disassembling binary stream.
* [zydis](https://github.com/zyantific/zydis) - fast and lightweight x86/x86-64 disassembler library.

Android application disassembler / decoder

* [JEB2](https://www.pnfsoftware.com/jeb2/) - eclipse-based integrated reverse engineering platform for analyzing various parts of Android application components.

Java decompiler

* [Bytecode Viewer](https://bytecodeviewer.com/) - aggregate of various tools
* [Procyon](https://bitbucket.org/mstrobel/procyon)
* [CFR](http://www.benf.org/other/cfr/)
* [FernFlower](https://github.com/fesh0r/fernflower)
* [Krakatau](https://github.com/Storyyeller/Krakatau)
* [Luyten](https://github.com/deathmarine/Luyten)

.NET decompiler

* [dnSpy](https://github.com/0xd4d/dnSpy)
* [JustDecompile](https://www.telerik.com/products/decompiler.aspx)
* [dotPeek](https://www.jetbrains.com/decompiler/)
* [ILSpy](http://www.ilspy.net/)

Python decompiler

* [uncompyle6](https://pypi.org/project/uncompyle6/)
* [decompile3](https://github.com/rocky/python-decompile3) - reworking and refactoring of `uncompyle6` which focus on Python 3.7+

Flash decompiler

* [JPEXS Flash Decompiler](https://github.com/jindrapetrik/jpexs-decompiler) - open source SWF decompiler and editor, convert SWF to FLA, edit ActionScript, replace resources (images, sounds, texts, fonts).
* [Flare](http://www.nowrap.de/flare.html) - Extract all scripts from SWF.

Delphi decompiler

* [Interactive Delphi Reconstructor](https://github.com/crypto2011/IDR)

Lua decompiler

* [UnLuac](https://sourceforge.net/projects/unluac/) - decompiler for Lua 5.0 - 5.4 and require debugging information (non-stripped).
* [LuaDec](https://github.com/viruscamp/luadec) - decompiler based on luadec 5.0.x and LuaDec51.

AutoIT decompiler

* [myAut2Exe](https://github.com/dzzie/myaut_contrib) - scan and extract the AutoIT script.
* [Exe2Aut](http://domoticx.com/autoit3-decompiler-exe2aut) - extract the AutoIT script by running it.

Ethereum (EVM) Solidity disassembler / decompiler

* [evmdis](https://github.com/Arachnid/evmdis) - EVM disassembler by static analysis on the bytecode.
* [pyevmasm](https://github.com/crytic/pyevmasm) - assembler and disassembler library for EVM (Ethereum Virtual Machine).

## Debuggers

Multi/cross platform

* [GDB](sudo apt install gdb)
* [lldb](http://lldb.llvm.org/)
* [vdb](https://github.com/vivisect/vivisect)

Windows

* [WinDbg](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/debugger-download-tools)
* [x64dbg](http://x64dbg.com/#start)
* [Immunity Debugger](http://debugger.immunityinc.com/)

Linux

* [QIRA](http://qira.me/) - timeless debugger which track all state while program is running.
* [EDB](http://www.codef00.com/projects#debugger)

Virtual Machine Introspection for debugging

* [rVMI](https://github.com/fireeye/rVMI)
* [r2vmi](https://github.com/Wenzel/r2vmi)

Hypervisor debugger

* [HyperDbg](https://github.com/rmusser01/hyperdbg/) - minimalistic hypervisor with hardware-assisted virtualization to debug kernel.

GDB enrichment

* [PEDA](https://github.com/longld/peda)
* [GEF](https://github.com/hugsy/gef)
* [Voltron](https://github.com/snare/voltron) - also available for LLDB, VDB, and WinDbg

OllyDbg variant

* [OllyDbg v1.10](http://www.ollydbg.de/)
* [OllyDbg v2.01](http://www.ollydbg.de/version2.html)
* [OllySnD](https://tuts4you.com/download.php?view.2061)
* [Olly Shadow](https://tuts4you.com/download.php?view.6)
* [Olly CiMs](https://tuts4you.com/download.php?view.1206)

Graphic Debugger

* [RenderDoc](https://renderdoc.org/)
* [PIX](https://blogs.msdn.microsoft.com/pix/download/)

## Behavior Analysis

Network simulation

* [iNetSim](http://www.inetsim.org/)
* [Fakenet](http://practicalmalwareanalysis.com/fakenet/)

Packet Capture

* [SmartSniff](http://www.nirsoft.net/utils/smsniff.html)
* [Wireshark](sudo apt install wiresharkdownload.html)

Process

* [ProcessHacker](https://processhacker.sourceforge.io/)
* [Process Explorer](https://technet.microsoft.com/en-us/sysinternals/processexplorer)
* [Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)

Tracer

* [API Monitor](http://www.rohitab.com/apimonitor)
* [Process Monitor](https://technet.microsoft.com/en-us/sysinternals/processmonitor)
* [SpyStudio](https://www.nektra.com/products/spystudio-api-monitor/)
* [fibratus](https://github.com/rabbitstack/fibratus) - explore and trace windows kernel
* [TCPView](https://docs.microsoft.com/en-us/sysinternals/downloads/tcpview)
* [CDA: Code Dynamic Analysis](http://split-code.com/cda.html)

Sandbox

* [Noriben](https://github.com/Rurik/Noriben)
* [Cuckoo](https://www.cuckoosandbox.org/)

Misc

* [Objective-See Utilities](https://objective-see.com/products.html)
* [XCode Instruments](https://developer.apple.com/xcode/download/) - XCode Instruments for Monitoring Files and Processes [User Guide](https://developer.apple.com/library/watchos/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/index.html)
* [dtrace script for Mac](http://dtrace.org/blogs/brendan/2011/10/10/top-10-dtrace-scripts-for-mac-os-x/) - sudo dtruss = strace [dtrace recipes](http://mfukar.github.io/2014/03/19/dtrace.html)
* [fs_usage](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/fs_usage.1.html) - report system calls and page faults related to filesystem activity in real-time.  File I/O: fs_usage -w -f filesystem
* [dmesg](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man8/dmesg.8.html) - display the system message buffer

## Dynamic Binary Instrumentation

Native

* [DynamoRIO](http://www.dynamorio.org) - runtime code manipulation system that supports code transformation on any part of program.
* [Frida](https://frida.re) - scriptable DBI toolkit for cross-platform target.
* [Pin](https://software.intel.com/en-us/articles/pin-a-dynamic-binary-instrumentation-tool)
* [QBDI](https://qbdi.quarkslab.com/) - modular, cross-platform, and cross-architecture DBI framework backed by LLVM.

.NET

- [Hawkeye2](https://github.com/odalet/Hawkeye2) - view, edit, analyze, and invoke (almost) any object from .net applications.
- [UnityDoorstop](https://github.com/NeighTools/UnityDoorstop) - execute managed assemblies inside Unity as early as possible.

## Binary Analysis Framework

* [Angr](http://angr.io/) - python framework for analyzing binaries, combines both static and dynamic symbolic (concolic) analysis.
* [Triton](https://triton.quarkslab.com) - dynamic binary analysis (DBA) framework.
* [BAP](http://binaryanalysisplatform.github.io/) - suite of utilities and libraries that enable analysis of programs in their machine representations.
* [BitBlaze](http://bitblaze.cs.berkeley.edu/)
* [PANDA](https://github.com/panda-re/panda) - Platform for Architecture-Neutral Dynamic Analysis, built on QEMU system emulator, analyzecode in runtime.
* [BARF](https://github.com/programa-stic/barf-project)
* [S2E](https://s2e.systems/) - platform for in-vivo analysis of software systems.
* [miasm](https://miasm.re/) - analyze / modify / generate binary program with python.
* [soot](https://github.com/soot-oss/soot) - java optimization framework

Symbolic Execution (only)

* [KLEE](https://klee.github.io/) - dynamic symbolic execution engine built on top of the LLVM compiler infrastructure
* [manticore](https://github.com/trailofbits/manticore/) - symbolic execution tool for analysis of smart contracts and binaries.
* [Kite](http://www.cs.ubc.ca/labs/isd/Projects/Kite/) - conflict-driven symbolic execution tool (proof of concept)
* [jCUTE](https://github.com/osl/jcute) - Java Concolic Unit Testing Engine, automatically generate unit tests for Java programs.
* [ExpoSE](https://github.com/ExpoSEJS/ExpoSE) - dynamic symbolic execution engine for JavaScript.
* [ESILSolve](https:/github.com/aemmitt-ns/esilsolve) - python symbolic execution framework using r2 and ESIL.

Binary lifting

* [McSema](https://github.com/lifting-bits/mcsema) - framework for lifting x86, amd64, and aarch64 program binareis to LLVM bitcode.

Theorem prover and solver

* [Z3](https://github.com/Z3Prover/z3) - cross-platform satisfiability modulo theory
* [STP](https://stp.github.io/)
* [CVC4](https://cvc4.github.io/)
* [Boolector](https://boolector.github.io/)

## Code Emulators

* [unicorn](https://github.com/unicorn-engine/unicorn)
* [libemu](http://libemu.carnivore.it)
* [pegasus](https://github.com/imugee/pegasus)

## Injectors

Windows

* [PolyHook](https://github.com/stevemk14ebr/PolyHook)
* [EasyHook](https://easyhook.github.io/)
* [Deviare2](https://github.com/nektra/Deviare2)
* [Xenos](https://github.com/DarthTon/Xenos)

## HTTP Intercept Proxy

* [Fiddler](https://www.telerik.com/fiddler)
* [ZAP](https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project)
* [Charles](https://www.charlesproxy.com/)

## Reconstructors

Import reconstructor

* [ImpRec](http://www.woodmann.com/collaborative/tools/index.php/ImpREC)
* [Scylla](https://github.com/NtQuery/Scylla)
* [LordPE](http://www.woodmann.com/collaborative/tools/images/Bin_LordPE_2010-6-29_3.9_LordPE_1.41_Deluxe_b.zip)

Data-type reconstructor

* [ReClassEx](https://github.com/dude719/ReClassEx)
* [ReClass.NET](https://github.com/KN4CK3R/ReClass.NET) - port of ReClass to .NET

## Unpackers

* [FUU](https://github.com/crackinglandia/fuu) - [F]aster [U]niversal [U]npacker
* [TitanEngine](http://www.reversinglabs.com/products/TitanEngine.php)

## Obfuscators

Native

* [Stunnix](http://stunnix.com/prod/cxxo/)
* [M/o/Vfuscator](https://github.com/xoreaxeaxeax/movfuscator)

AutoIt scripts

* [Assembly Source Code Obfuscator](https://www.pelock.com/products/obfuscator)
* [AutoIt Source Code Obfuscator](https://www.pelock.com/products/autoit-obfuscator)

## Deobfuscators

Native

* [LLVM Deobfuscator](https://github.com/RPISEC/llvm-deobfuscator)
* [SATURN]() - software deobfuscation framework based on LLVM.

Java

* [Java Deobfuscator](https://javadeobfuscator.com/)

.NET

* [de4dot](https://github.com/0xd4d/de4dot)

Javascript

* [de4js](https://github.com/lelinhtinh/de4js)

PHP

* [evalhook](https://github.com/unreturned/evalhook)

String extraction

* [FLOSS](https://github.com/fireeye/flare-floss)
* [NoMoreXOR](https://github.com/hiddenillusion/NoMoreXOR)

## Binary Visualization

See also [Data & Format Reversing](_format.md).

* [Veles](https://codisec.com/veles/)
* [..cantor.dust..](https://sites.google.com/site/xxcantorxdustxx/home)
* [binglide](https://github.com/wapiflapi/binglide)

## Document Analysis

* [Ole Tools](http://www.decalage.info/python/oletools)
* [Didier's PDF Tools](http://blog.didierstevens.com/programs/pdf-tools/)
* [Origami](https://github.com/cogent/origami-pdf)

## Misc

- [bingrep](https://github.com/m4b/bingrep) - grep through binaries

- - -

## IDA Script

* [IDA Python Src](https://github.com/idapython/src) - source code for IDAPython plugin, enable python script running in IDA Pro .

references

* [IDC Functions Doc](https://www.hex-rays.com/products/ida/support/idadoc/162.shtml)
* [Using IDAPython to Make your Life Easier](http://researchcenter.paloaltonetworks.com/tag/idapython/)
* [Introduction to IDA Python](https://tuts4you.com/download.php?view.3229)
* [The Beginner's Guide to IDA Python](https://leanpub.com/IDAPython-Book)
* [IDA Plugin Contest](https://www.hex-rays.com/contests/)

Script collection

* [fireeye/flare-ida](https://github.com/fireeye/flare-ida) - multiple IDA plugins and IDAPython scripts by FLARE team.
* [devttys0/ida](https://github.com/devttys0/ida) - collection of IDAPython plugins/scripts/modules.
* [onehawt IDA Plugin List](https://github.com/onethawt/idaplugins-list) - list of ida scripts (IDC / IDAPython), links to many repository.

## Ghidra Script

Script collection

* [ghidra ninja](https://github.com/ghidraninja/ghidra_scripts)


# Awesome Hardware Reverse Engineering

A curated list of awesome reverse engineering resources to make you better!

Managed by Reversing.ID for the reversing community.

## Introduction

`Hardware Reverse Engineering` focus on circuitry (boards, ICs) and intercomponent relation.

The scope and level of analysis can be vary greatly, some common targets:

- firmware.
- board layout.
- chip circuit design.

Some notable process:

- teardown: product disassembly, component/subsystem identification
- interface: protocol monitoring/analysis/emulation
- firmware: extract/modify code or data
- circuit: silicon modification

## Table of Contents

- Resources
- [Books](#books)
- [Courses](#courses)
- [Channels](#channels)
- [References](#references)
- [Communities](#communities)
- [Protocol List](#protocol-list)
- Hadware Tools
- [Bus Interface](#bus-interface)
- [Programmers & Flashers](#programmers--flashers)
- [Hardware Debuggers](#hardware-debuggers)
- [Protocol Analyzers](#protocol-analyzers)
- [Logic Analyzers](#logic-analyzers)
- [Osciloscopes](#osciloscopes)
- [Dev & Breakout Boards](#dev--breakout-boards)
- [Radio Frequency](#radio-frequency)
- [Magnetic Strip](#magnetic-strip)
- Software Tools
- [EDA](#eda)
- [Firmware Extract](#firmware-extract)
- [Disassemblers & Decompilers](#disassemblers--decompilers)
- [Emulators](#emulators)
- [Software Debuggers](#software-debuggers)
- [Traffic Analysis](#traffic-analysis)
- Software Packages & Libraries
- [RTOS](#rtos)

- - -

## Books

Electronics, VHDL, and circuit design

* [Digital Electronics](https://amzn.com/8125939369)
* [Digital Fundamentals](https://amzn.com/0132737965)
* [Digital Design](https://amzn.com/B00HQ1CYUU)
* [The Art of Electronics](https://amzn.com/0521809266)

Hardware hacking

* [The Hardware Hacker: Advetures in Making and Breaking Hardware](https://amzn.com/159327758X)
* [Hardware Hacking: Have Fun while Voiding your Warranty](https://amzn.com/B001UN2WDY)
* [Hardware Hacking Projects for Geeks](https://amzn.com/0596003145)
* [Game Console Hacking: Xbox, PlayStation, Nintendo, Game Boy, Atari and Sega](https://amzn.com/B001V7U7AE)

PCB (Printed Circuit Boards)

* [The Art of PCB Reverse Engineering: Unravelling the Beauty of the Original Design](https://amzn.com/1499323441)
* [PCB-RE: Real-World Examples](https://amzn.com/B087V4GJ94)

BIOS, UEFI, Firmware

* [BIOS Disassembly Ninjutsu Uncovered](https://amzn.com/1931769605)
* [Beyond BIOS: Developing with the Unified Extensible Firmware Interface](https://amzn.com/1501514784)

## Courses

Electronic

* [Lessons in Electric Circuits](https://www.ibiblio.org/kuphaldt/electricCircuits/) - Free high quality textbooks and worksheets with emphasys on theory, simulation, and the socratic method.
* [Ultimate Electronics: Practical Circuit Design and Analysis](https://ultimateelectronicsbook.com/) - Free online book with interactive schematics & simulations by CircuitLab (under development).
* [Khan Academy - Electrical Engineering](https://www.khanacademy.org/science/electrical-engineering) - Non-profit learning platform with a full course on electrical engineering and related topics.
* [NEETS (Navy Electricity and Electronics Training Series)](https://www.fcctests.com/neets/Neets.htm) - U.S. Navy Non-Resident Training Course Material.
* [Berkeley EECS](http://inst.eecs.berkeley.edu/classes-eecs.html) - Comprehensive EE & CS course website archives.
* [Dr. Jacob Baker](http://cmosedu.com) - Courses and tutorials, professor at The University of Nevada, Las Vegas.
* [Dr. Abraham](https://www.cerc.utexas.edu/~jaa/teaching.html), [Dr. McDermot](http://users.ece.utexas.edu/~mcdermot/), and [Dr. Valvano](http://users.ece.utexas.edu/~valvano/) - Courses materials, professors at UT Austin

Radio Frequency

* [Software Defined Radio with HackRF](https://greatscottgadgets.com/sdr/)

## Channels

YouTube Channel

* [Micah Scott](https://www.youtube.com/user/micahjd) - video logs of Reverse Engineering and repurposing consumer electronics hardware in creative ways.
* [The Signal Path](https://www.youtube.com/user/TheSignalPathBlog) - collections of teardown, repairs, and reviews of lab equipment and prototyping products.
* [GreatScott](https://www.youtube.com/user/greatscottlab)
* [EEVblog](https://www.youtube.com/user/EEVblog)

## References

Learning Assembly


Development Boards

* [Arduino](https://www.arduino.cc/) | based on AVR or ARM
* [NodeMCU](https://www.nodemcu.com) | based on ESP8266
* [Teensy](https://www.pjrc.com/teensy/) | based on ARM
* [MSP430 Launchpad](http://www.ti.com/tool/MSP-EXP430G2ET) | based on TI MSP430
* [STM32 Nucleo](https://www.st.com/en/evaluation-tools/stm32-nucleo-boards.html)

Single-Board Computer (family)

* [Raspberry Pi](https://www.raspberrypi.org/)
* [BeagleBoard](https://beagleboard.org/)
* [Onion Omega](https://onion.io/)
* [Pine64](https://www.pine64.org/)
* [ODROID](https://www.hardkernel.com)

Part Search Engine

* [Octopart](https://octopart.com)
* [Findchips](https://www.findchips.com/)
* [Parts.io](https://parts.io/)
* [AllDataSheet.io](https://www.alldatasheet.com/)

## Protocol List

Inter-circuitry protocol (Internal)

This protocol used for communication between circuit or modules, such as EEPROM, RAM, RTC, sensors, etc.

* SPI: *Serial Peripheral Interface*, synchronous protocol with master-slave design.
* I2C: *Inter-Integrated Circuit*, synchronous protocol with multi-master and multi-slave support.

System communication (External)

This protocol used for communication between modules or external system.

* Wired protocol
- CAN: *Controller Area Network*, device communication popular in vehicle.
- USB: *Universal Serial Bus*
- UART & USART: *Universal Synchronous Asynchronous Receiver-Transmitter*
- RS232
* Wireless protocol
- Bluetooth
- LoRaWAN
- WiFi
- ZigBee

Debugging protocol

* JTAG: *Joint-Test Action Group*
* SWD: *Serial-Wire Debug*, ARM specific protocol

## Communities

* [Kitspace](https://kitspace.org)
* [Hackaday.io](https://hackaday.io)
* [Hackster.io](https://www.hackster.io/)
* [Maker.pro](https://maker.pro)
* [Maker.io](https://www.digikey.com/en/maker)

- - -

## Bus Interface

* [Shikra](https://int3.cc/products/the-shikra) - JTAG, SPI, I2C, UART, GPIO
* [Hydrabus](https://hydrabus.com/) - UART, I2C, USB, smartcard, 2-wire, wiegand, SPI, CAN, SDIO, DAC, 1-wire
* [Xpliot Nano](https://expliot.io/products/expliot-nano)
* [Bus Pirate](http://dangerousprototypes.com/docs/Features_overview) - 1-wire, I2C, SPI, JTAG, UART
* USB to TTL/UART
* [USBtin](https://www.fischl.de/usbtin/) - USB to CAN interface.

OBD adapter

* [ObdDiag](http://www.obddiag.net/) - open source ELM327 OBD adapter, connect to On-Board Diagnostic (OBD) port for connecting to car's self-diagnostic system.
* [M2](https://www.macchina.cc/m2-introduction) -

## Programmers & Flashers

*read/write device which contain memory*

Universal

* [EE Tools](https://eetools.com/product-category/programmers/)

Microcontroller/Microprocessor Specific

* STM32 programmer - enter DFU (Device Firmware Upgrade) mode for programming and debugging
* AVR programmer

## Hardware Debuggers

SWD (Serial Wire Debugger), ARM specific

* [ST-Link](https://www.st.com/en/development-tools/st-link-v2.html)

JTAG (Joint-Test Action Group)

* [JTAGulator](https://github.com/grandideastudio/jtagulator) - scan and identify JTAG pin
* [JTAGEnum](https://github.com/cyphunk/JTAGenum) - using arduino to identify JTAG pin
* [RIFF Box](http://www.riffbox.org/)
* [Bus Blaster](http://dangerousprototypes.com/docs/Bus_Blaster) - JTAG debugger
* [Segger J-Link](https://www.segger.com/products/debug-probes/j-link/)
* Shikra
* ST-Link

## Protocol Analyzers

*real-time, non-intrusive monitoring/capture/decoding of wired communication*

Multi

* [TotalPhase Beagle](https://www.totalphase.com/products/beagle-i2cspi/) - USB/I2C/SPI

USB

* Teledyn [LeCroy Voyager](https://teledynelecroy.com/protocolanalyzer/usb) series
* [OpenVizsla](http://openvizsla.org/)
* [Daisho](https://greatscottgadgets.com/daisho/)

CAN

* [CANtact](https://linklayer.github.io/cantact/) - CAN (Controller Area Network) to USB interface
* [TotalPhase Komodo](https://www.totalphase.com/products/komodo-canduo/) - CAN

## Logic Analyzers

*concurrently capturing, visualizing, and decoding large quantities of digital data*

* [Logic Pirate](http://dangerousprototypes.com/docs/Logic_Pirate) - 8 channels
* [Saleae](https://www.saleae.com/)
* USB Logic Analyzer
* [BeagleBone as Logic Analyzer](https://github.com/abhishek-kakkar/BeagleLogic)

## Osciloscopes

*visual display of electrical signals and how they change over time*

Standalone

* HP/Agilent
* Tektronix
* Rohde & Schwarz
* LeCroy
* Rigol

PC_based

* ProcScope
* USBee
* PicoScope

## Dev & Breakout Boards

* [GoodFET](http://goodfet.sourceforge.net/)
* [GreatFET One](https://greatscottgadgets.com/greatfet/one/)

## Radio Frequency

*Analyze, modify, and replay Radio Frequency signal.*

General-purpose

* [HackRF](https://greatscottgadgets.com/hackrf/) - half duplex, 1 MHz - 6 GHz
* [LimeSDR](https://www.crowdsupply.com/lime-micro/limesdr) - full duplex,
* [RTL-SDR](https://www.rtl-sdr.com/) - RX, 500 kHz - 1766 MHz
* [YARD Stick](https://greatscottgadgets.com/yardstickone/) - half duplex, 300-348 MHz, 391-464 MHz, 782-928 MHz
* [nRF52840 Dongle](https://www.nordicsemi.com/Software-and-tools/Development-Kits/nRF52840-Dongle) - dongle which support Bluetooth 5, Bluetooth mesh, Thread, ZigBee, 802.15.4, ANT, and 2.4 GHz proprietary protocols.

Zigbee

* [ApiMote](https://github.com/riverloopsec/apimote) - IEEE 802.15.4/ZigBee sniffing hardware
* [Freakduino](https://freaklabs.org/documentation/freakduino/)

Bluetooth

* [Ubertooth](https://greatscottgadgets.com/ubertoothone/)
* [Bluefruit LE Snifferluef](https://www.adafruit.com/product/2269)

RFID & NFC

* [Proxmark3](https://proxmark.com/)
* [Chameleon](https://lab401.com/products/chameleon-mini-reve-rebooted) - NFC emulation and manipulation tool
* [HydraNFC](https://hydrabus.com/hydranfc-1-0-specifications/)
* ACR-122U - RFID/NFC reader/writer

## Magnetic Strip

* [MagSpoof](https://samy.pl/magspoof/) - wireless credit card / magnetic stripe spoofer

- - -

## EDA

EDA (Electronic Design Automation) and ECAD (Electronic Computer-Aided Design)

* [Eagle](https://www.autodesk.com/products/eagle/overview)
* [KiCad](https://www.kicad-pcb.org/)
* [Altium](https://www.altium.com/) and free [Altium CircuitMaker](https://circuitmaker.com/)
* [Pulsonix](https://www.pulsonix.com/)
* [DesignSpark PCB](https://www.rs-online.com/designspark/pcb-software)
* [gEDA](http://geda-project.org/)
* [DipTrace](https://diptrace.com/)
* [LibrePCB](https://librepcb.org/)
* [Horizon EDA](https://github.com/horizon-eda/horizon)

## Firmware Extract

* [Binwalk](https://github.com/ReFirmLabs/binwalk)

## Disassemblers & Decompilers

Multi-architecture


## Emulators

Full firmware emulator

* [QEMU](https://www.qemu.org/) - Generic and open source machine emulator and virtualizer.
- [ARM-X](https://github.com/therealsaumil/armx) - Firmware emulation framework based on top of QEMU
- [Firmwadyne](https://github.com/firmadyne/firmadyne) - Platform for emulation and dynamic analysis of Linux-based firmware.
* [Kopycat](https://github.com/inforion/kopycat/) - hardware emulator.

## Software Debuggers

Hardware debugger

* [OpenOCD](http://openocd.org/) - Open On-Chip Debugger, give GDB support.
* [UrJTAG](http://www.urjtag.org) - Universal JTAG Library

Signal Analysis

* [Sigrok](https://sigrok.org/) // [PulseView](https://sigrok.org/wiki/PulseView)
* [Open Bench Logic Sniffer](http://dangerousprototypes.com/docs/Open_Bench_Logic_Sniffer)

Firmware debugger

* [GDB](sudo apt install gdb)

## Traffic Analysis

Communication Protocol

* [I/O Ninja](https://ioninja.com/) - Professional, scriptable, multi-purpose terminal emulator, network sniffer, and IO monitor.
* [Bettercap](https://github.com/bettercap/bettercap) - Swiss-army knife for 802.11, BLE, and ethernet network reconnaissance and MITM attacks.
* CAN (Controller Area Network)
- [CANToolz](https://github.com/CANToolz/CANToolz) - Black-box CAN network analysis framework.
* BLE (Bluetooth Low Energy)
- [btproxy](https://github.com/conorpp/btproxy) - MITM analysis tool for Bluetooth.
- [BtleJuice](https://github.com/DigitalSecurity/btlejuice) - BLE MITM framework.
- [btlejack](https://github.com/virtualabs/btlejack) - BLE swiss-army knife pair with BBC Micro:Bit device.
- Bluez - sdptool, l2ping
* ZigBee
- [KillerBee](https://github.com/riverloopsec/killerbee) - IEEE 802.15.4/ZigBee Security Research Toolkit.

Radio Frequency

* [Universal Radio Hacker](https://github.com/jopohl/urh) - Investigate Wireless Protocols
* [Inspectrum](https://github.com/miek/inspectrum) - Offline radio signal analyser
* [GNU Radio](https://gnuradio.org/) - Software development toolkit for signal processing block to implement Software-Defined Radio and Signal-processing system.

- - -

## RTOS

Free or Open Source RTOS (Real Time Operating System)

* [TinyOS](https://github.com/tinyos/tinyos-main) - A operating system designed for low-power wireless devices, such as those used in sensor networks, ubiquitous computing, personal area networks, smart buildings, and smart meters.
* [ContikiOS](https://github.com/contiki-os/contiki) - A free Operating System with focus to provide standardized low-power wireless communication for a wide range of hardware platforms.
* [FreeRTOS](http://www.freertos.org/) - A free use Real Time Operating system which is widely used and supports a large number of platforms.
* [RIOT](https://github.com/RIOT-OS/)  - A free OS for IoT devices providing foundational trust services. The trust services include device identity, sealing, attestation, and data integrity. The term “Robust” is used because the minimal trusted computing base is tiny, and because RIoT capabilities can remotely re-establish trust in devices that have been compromised by malware.
* [RTEMS](https://www.rtems.org/) - Real-Time Executive for Multiprocessor Systems or RTEMS is an open source Real Time Operating System (RTOS) that supports open standard application programming interfaces (API) such as POSIX. It is used in space flight, medical, networking and many more embedded devices using processor architectures including ARM, PowerPC, Intel, Blackfin, MIPS, Microblaze and more.

Commercial RTOS

* [SafeRTOS](https://www.highintegritysystems.com/safertos/) - Certified version of FreeRTOS by TUEV SUED against IEC 61508 (basic functional safety standard) up to SIL3 (the highest safety integrity level for a single software component), ISO 26262 ASIL D (automotive standard) and EN62304 (medical device standard).
* [INTEGRITY/INTEGRITY-178](http://www.ghs.com/products/rtos/integrity.html#performance) - Two commercial RTOS variants targeting to power embedded systems with total reliability, absolute security, and maximum real-time performance. The variant INTEGRYTY-178 has a lot of safety and security certifications.
* [PikeOS](https://www.sysgo.com/products/pikeos-hypervisor/) - A commercial micro-kernel based operating system with a small footprint and certified for DO-178 (avionics), IEC-61508 (industrial), ISO-26262 (automotive).
* [Rocket](http://www.windriver.com/products/operating-systems/rocket/) - A free embedded operating system specifically designed to quickly and easily build small, intelligent devices in Wind Rivers cloud-based development environment, Wind River Helix™ App Cloud.
* [Nucleus RTOS](https://www.mentor.com/embedded-software/nucleus/) - Commercial, highly scalable micro-kernel based real-time operating system designed for scalability and reliability.
* [uC/os](https://www.micrium.com/rtos/kernels/) - µC/OS-II and µC/OS-III are preemptive, highly portable, and scalable real-time kernels. You can test them out for free, but you must pay to put them into a product.
* [TI-RTOS](www.ti.com/tool/ti-rtos) - A real-time operating system for TI microcontrollers, It Includes TCP/IP and USB stacks, a FAT file system, and device drivers, Most of the TI-RTOS components are released under the BSD License.

# Awesome Data Format Reverse Engineering

A curated list of awesome reverse engineering resources to make you better!

Managed by Reversing.ID for the reversing community.

## Introduction

`Data Format Reverse Engineering` focus on representation and interpretation of structured data in stored or transmitted form.

In some cases, format reversing is done in conjunction with software which generate the data.

## Table of Contents

- Resources
- Tools
- [Hex Editors](#hex-editors)
- [Format Identifier](#format-identifier)
- [Structure Parser](#structure-parser)
- [Binary Visualization](#binary-visualization)
- [String Search](#string-search)
- [Pattern Search](#pattern-search)
- [Bundle Extractor](#bundle-extractor)

- - -

## Hex Editors

Hex editor lets you view/edit the binary data of a file.

Multi/cross platform


Windows


Mac OS X


## Format Identifier


## Structure Parser


## Binary Visualization


## String Search


## Pattern Search

- [YARA](https://github.com/virustotal/yara)

## Bundle Extractor

Game Assets

* [UABE](https://github.com/DerPopo/UABE) - Unity Assets Bundle Extractor
* [DevXUnityUnpacker](http://devxdevelopment.com/UnityUnpacker)
* [MultiEx Commander](http://multiex.xentax.com/) - multiple game resources archive.

# Awesome Database Reverse Engineering

A curated list of awesome reverse engineering resources to make you better!

Managed by Reversing.ID for the reversing community.

## Introduction

`Database Reverse Engineering` focus on collection of structured data (entities) and relationship among them.

The strategy for storing structured data has evolved over time. Different strategy has different characteristic. As of today we can categorize the database into three types:

- Flat-File Database
- Relational Database
- Non-Relational Database

Database Reverse Engineering might used for schema recovery or remodelling.

## Table of Contents

- Resources
- [Books](#books)
- [Courses](#courses)
- [DBMS List](#dbms-list)
- [DB Connections](#db-connections)
- [Relational Database](#relational-database)
- [Database Administration Client](#database-administration-client)
- [Code Generation](#code-generation)
- [Schema Modellers](#schema-modellers)
- [Schema Navigation & Visualization](#schema-navigation--visualization)
- [Non-Relational Database](#non-relational-database)
- [Flat-File Database](#flat-file-database)
- [Hex Editors](#hex-editors)
- [Structure Parsers](#structure-parsers)

- - -

## Books

## Courses

## DBMS List

Some notable DBMS, not a comprehensive list.

Relational Database

* [MariaDB](https://mariadb.org/)
* Microsoft Access - file-based data storage for desktop application.
* Microsoft SQL Server
* [MySQL](https://www.mysql.com/)
* [Oracle Database](https://www.oracle.com/database/)
* [PostgreSQL](https://www.postgresql.org/)
* [SQLite](https://www.sqlite.org/) - small, fast, self-contained, embedded SQL database engine.

Non-Relational Database (NoSQL)

* Column:
- [Apache Cassandra](https://cassandra.apache.org/)
- [Apache HBase](https://hbase.apache.org/)
- [ScyllaDB](https://www.scylladb.com/)
* Document:
- [Apache CouchDB](https://couchdb.apache.org/)
- [ArangoDB](http://arangodb.com/)
- [Couchbase](http://couchbase.com/)
- [MongoDB](https://www.mongodb.com/)
* Graph:
- [Neo4j](https://neo4j.com/)
- [Redis](https://redis.io/)
* Key-Value Store:

## DB Connections

Database Connection is facility to allow client software to talk to database server, whether on the same machine or not. Sending query and receiving result set are done in active connection.

Connections are built by supplying an underlying driver or provider with a `Connection String`, which is a way of addressing a specific database or server. The Connection String is usually a combination of following field in a single statement:

* Server: domain or ip address of database server
* Database: database name
* Uid: username which is granted access to database
* Pwd: password to identify username.

Example:

```
Server=db.internal.reversing.id; Database=identity; Uid=service; Pwd=service_pwd
```

Database connection often wrapped by API. Common used API are:

* JDBC (Java Database Connectivity)
* ODBC (Open Database Connectivity)

- - -

## Relational Database

Database Reverse Engineering for Relational Database focus on tables, models, stored procedure, primary keys, and foreign keys to determine relationship between tables and reconstructing E-R Diagram.

A database is logically made of several tables. Relationship is implemented by keys (primary key, foreign key) to map the tables into `One-to-One`, `One-to-Many`, or `Many-to-Many` relation.

#### Database Administration Client

Desktop

* [DataGrip](https://www.jetbrains.com/datagrip)
* [DBeaver](https://github.com/dbeaver/dbeaver)
* dbForge Studio for [MySQL/MariaDB](https://www.devart.com/dbforge/mysql/studio), [Oracle](https://www.devart.com/dbforge/oracle/studio), [PostgreSQL](https://www.devart.com/dbforge/postgresql/studio), [SQL Server](https://www.devart.com/dbforge/sql/studio)
* [HeidiSQL](https://github.com/HeidiSQL/HeidiSQL)
* [MySQL Workbench](https://www.mysql.com/products/workbench/)
* [Navicat](https://www.navicat.com/en/products#navicat)
* [SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)

Web App

* [Adminer](https://github.com/vrana/adminer)
* [phpLiteAdmin](https://www.phpliteadmin.org/) - SQLite database administration
* [phpMyAdmin](https://github.com/phpmyadmin/phpmyadmin) - MySQL and MariaDB database administration

CLI

* [litecli](https://github.com/dbcli/litecli) - SQLite
* [mssql-cli](https://github.com/dbcli/mssql-cli) - SQL Server
* [mycli](https://github.com/dbcli/mycli) - MySQL and MariaDB
* [pgcli](https://github.com/dbcli/pgcli) - PostgreSQL

#### Code Generation

* [ddl-generator](https://github.com/catherinedevlin/ddl-generator) - Infers SQL DDL (Data Definition Language) from table data.
* [scheme2ddl](https://github.com/qwazer/scheme2ddl) - Command line util for export Oracle schema to set of ddl init scripts with ability to filter undesirable information, separate DDL in different files, pretty format output.

#### Schema Modeller

* [Navicat Data Modeler](https://www.navicat.com/en/products/navicat-data-modeler) - A powerful and cost-effective database design tool which helps you build high-quality conceptual, logical and physical data models.
* [Oracle SQL Developer Data Modeler](http://www.oracle.com/technetwork/developer-tools/datamodeler/overview/index.html) - Oracle SQL Developer Data Modeler is a free graphical tool that enhances productivity and simplifies data modeling tasks.
* [pgmodeler](https://github.com/pgmodeler/pgmodeler) - Data modeling tool designed for PostgreSQL.

#### Schema Navigation & Visualization

* [dbdiagram.io](https://dbdiagram.io) - quick and simple online tool for drawing database relationship diagrams.
* [dbvis](https://www.dbvis.com/) -
* [ERAlchemy](https://github.com/Alexis-benoist/eralchemy) - Entity Relation Diagrams generation tool.
* [SchemaCrawler](https://github.com/schemacrawler/SchemaCrawler) - A free database schema discovery and comprehension tool.
* [Schema Spy](https://github.com/schemaspy/schemaspy) - Generating your database to HTML documentation, including Entity Relationship diagrams.
* [tbls](https://github.com/k1LoW/tbls) - CI-Friendly tool for document a database, written in Go.

- - -

## Non-Relational Database

Database Reverse Engineering for Non-Relational Database focus on models and relationship of each models.

Non-Relational Database refers to storage and retrieval of data which is modeled in means other than tabular relations used in Relational Database.

Non-Relational DBMS might offer a language to query data as alternative to SQL. Some notable query languages are AQL, Cypher, GraphQL, Gremlin, and SPARQL.

There are many types of approaches of NoSQL, such as Column, Document, Graph, Key-Value, and Object.

`Column`-oriented database stores data tables by columns rather than by rows. Unlike Relational Database, the names and format of the columns can vary from row to row in the same table.

`Document`-oriented database store data in the form of document. Document is a general term for encapsulating and encoding data in standard format such as XML, YAML, JSON, and binary format.

`Graph` database use graph structures for semantic queries with nodes, edges, and properties to represent data.

`Key-Value` database use the associative array (also called map or dictionary) as their fundamental data model. In this model, data is represented as a collection of Key-Value pairs.

`Object`-oriented database represent information in the form of objects as used in `Object-Oriented Programming`.

- - -

## Flat-File Database

Database Reverse Engineering for Flat-File Database is based on [File Format Reverse Engineering](_format.md). It focus on files, indexes and keys to determine structure of record and relationships of tables.

In pre-DBMS era, each table is stored as a simple file. Access to data is actually I/O operations. The file can be a plain text file or a binary file. The database is a collection of files which contain structured data and cross-reference to each other.

Records follow a uniform format. The size depends on number and size of fields. There are different conventions for depicting data. Fields and records might be separated by delimiter. If not, parser is responsible to read and interpret each record and field.

Relationship can be inferred from the data. Each record may have `Primary Keys` and `Foreign Keys`.

Iterating all records for locating specific item is inefficient especially when I/O operation involved. To speed up operation, `Indexing` is used. Index consists of two fields: `Search Key` and `Pointer`. Search Key is a copy of `Primary Key` and `Pointer` is offset where record can be found on file. Only selective key appears on Index. Usually the first item in the block of records.

`Index` can appear as internal or external of file. Internal Index implemented as header or trailer of data file. While External Index is implemented as a separate file. Multilayer indexing is possible where two or more Index file used.

## Hex Editors

Hex editor lets you view/edit the binary data of a file.

Multi/cross platform


Windows


Mac OS X


## Structure Parsers



