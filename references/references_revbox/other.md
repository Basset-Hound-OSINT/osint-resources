1. Ghidra
Ghidra burst onto the scene when the NSA released it as open-source in 2019, and it’s quickly become a favorite. It’s packed with features, and the best part? It’s completely free.


GHIDRA
‍

Pros:
Ghidra handles multiple architectures (x86, ARM, MIPS, etc.) and comes with a built-in decompiler.
It’s got a clean, user-friendly interface and even supports collaboration, so teams can work on the same project.
Cross-platform, so it works on Windows, macOS, and Linux.
‍

Cons:
While it’s powerful, the decompiler isn’t quite as polished as IDA Pro’s.
The learning curve can be a bit steep, especially if you’re new to reverse engineering.
‍

Why People Like It:
It’s open-source, so you don’t have to drop thousands of dollars. The collaboration feature is also a huge win for teams.
‍

2. IDA Pro
Ask any reverse engineer about top-tier tools, and IDA Pro (How to install IDA on Linux) is probably the first thing they’ll mention. It’s been around for years and is known for its industry-leading decompiler and wide range of architecture support.

‍


IDA-PRO
‍

Pros:
IDA Pro supports a vast range of file formats and architectures.
Its Hex-Rays decompiler is second to none in terms of accuracy.
A huge plugin ecosystem makes it even more powerful.
Excellent visualization tools (like graphs) make it easier to follow the flow of code.
‍

Cons:
The price is a big drawback. IDA Pro isn’t cheap, and adding the decompiler plugin makes it even pricier.
It’s also not open-source, so you’re locked into a proprietary system.
‍

Why People Like It:
The decompiler is simply the best. Plus, with the massive plugin support and huge community, you can pretty much do anything with IDA Pro.
‍

Reverse Engineering
If you're looking for a hands-on reverse engineering course to use these tools, you can check these:

‍


Hands-on reverse engineering course
‍


Malware analysis learning path
‍

3. OllyDbg
OllyDbg has been around for a long time and is a staple for those analyzing Windows executables. It’s a simple, free, 32-bit debugger that’s loved for its ease of use and simplicity.

‍


OllyDbg
‍

Pros:
It’s free and very easy to use. OllyDbg’s interface is clean and approachable, even for beginners.
Great for Windows PE files and malware analysis.
Supports plugins to extend its functionality.
‍

Cons:
It’s 32-bit only, so it’s limited to older binaries. There are unofficial plugins for 64-bit support, but it’s not ideal.
Windows-only tool.
‍

Why People Like It:
For quick and dirty Windows debugging, especially for malware analysis, OllyDbg is a solid choice. It's lightweight and gets the job done.
‍

4. Radare2 (R2)
Radare2 is for the hardcore reverse engineers who don’t mind getting their hands dirty. It’s free, open-source, and has support for multiple architectures, but it’s not the most user-friendly tool out there.

‍


Radare2
‍

Pros:
Radare2 is highly customizable and supports a ton of architectures and file formats.
It’s incredibly flexible, with lots of utilities (like r2pipe, rabin2, and ragg2).
Cross-platform, so it works on Windows, macOS, Linux, and BSD.
‍

Cons:
The learning curve is steep, mainly because it’s heavily command-line-driven.
It doesn’t have a built-in decompiler, though Cutter (a Radare2 GUI) helps by integrating some decompilation features.
‍

Why People Like It:
If you need something flexible and powerful (and don’t mind putting in the time to learn it), Radare2 is an incredible tool. Plus, it’s free and open-source.
‍

5. Immunity Debugger
Immunity Debugger is another Windows-based debugger, but it’s got a bit more going on than OllyDbg. With built-in Python scripting, it’s a great tool for vulnerability research and exploit development.

‍


Immunity Debugger
‍

Pros:
Python scripting support is huge. You can automate tasks or build custom tools with ease.
It’s free and lightweight.
Often used for exploit development thanks to its flexibility.
‍

Cons:
It’s limited to 32-bit binaries and Windows only.
Development updates have slowed down, and some features are becoming a bit outdated.
‍

Why People Like It:
For those focused on exploit dev or vulnerability research, Immunity Debugger’s Python integration is a game-changer. It’s also free and lightweight, making it a great OllyDbg alternative.
‍

6. Frida
Frida is a dynamic instrumentation tool, and it’s a bit different from the others on this list. Instead of focusing on static analysis, Frida shines when you need to inject code into a running process and modify its behavior on the fly.

‍


FRIDA
‍

Pros:
Frida supports Windows, macOS, Linux, Android, and iOS. If you’re reverse engineering mobile apps, this is one of the best tools out there.
It’s flexible, scriptable with JavaScript, and great for dynamic analysis.
Perfect for real-time code injection and function hooking.
‍

Cons:
It’s not as beginner-friendly as other tools and requires decent scripting skills.
Mostly focused on dynamic analysis, so not the best for static analysis tasks.
‍

Why People Like It:
If you’re working on mobile apps or want to mess with a process in real-time, Frida is a must-have. The ability to hook functions and change behavior dynamically is incredibly powerful.
‍

7. JaDx
JaDx is a go-to tool for anyone working with Android apps. It’s an open-source decompiler that converts APK files into readable Java code, making it easier to understand what an Android app is doing.

‍


JaDx
‍

Pros:
It’s free, open-source, and very easy to use.
The GUI is simple, and it’s great for decompiling Android APKs into readable Java.
Works cross-platform since it’s Java-based.
‍

Cons:
It’s limited to Android applications, so if you need something for other platforms, you’re out of luck.
Decompilation isn’t always perfect, especially with obfuscated code.
No dynamic analysis capabilities.
‍

Why People Like It:
JaDx is a fantastic tool for Android malware analysis or just inspecting how Android apps work. The interface is easy, and it gets the job done quickly.
‍

Conclusion
Each tool on this list caters to different aspects of reverse engineering, from disassembling and decompiling to dynamic analysis and debugging. Here's a quick summary of their most important use cases:

Ghidra and IDA Pro: Best for comprehensive binary analysis, with Ghidra being open-source and IDA Pro leading in decompilation accuracy.
OllyDbg and Immunity Debugger: Great for Windows-focused debugging and malware analysis.
Radare2: A highly customizable, command-line heavy tool ideal for users needing flexibility and support for multiple architectures.
Frida: Excellent for dynamic analysis and real-time process manipulation, especially in mobile app research.
JaDx: Specifically useful for Android reverse engineering, converting APKs to readable Java code.
‍

Recommended tools:

Ghidra

radare2

x64dbg

Cutter

Binary Ninja

Malcat

Apktool:
Apktool is a tool third party tool for reverse engineering that can decode resources to nearly original form and recreate them after making some adjustments. It allows debugging smali code step by step and also it allows working with app easier due to its project-like files structure and automation of some repetitive tasks like building apk, etc.

Apktool features:

decoding resources to nearly original form (including resources.arsc, XMLs and 9.png files) and rebuilding them
smali debugging
helping with some repetitive tasks
dex2jar:
Dex2jar is a lightweight API designed to read the Dalvik Executable (.dex/.odex) format. It is used to work with Android and Java .class files. dex2jar contains following components:

dex-reader is designed to read the Dalvik Executable (.dex/.odex) format. It has a lightweight API similar with ASM.
dex-translator is designed to do the convert job. It reads the dex instruction to dex-ir format, after some optimize, convert to ASM format.
dex-ir used by dex-translator is designed to represent the dex instruction
dex-tools tools to work with .class files. here are examples: Modify an apk, DeObfuscate a jar
d2j-smali [To be published] disassemble dex to smali files and assemble dex from smali files. different implementation to smali/baksmali, same syntax, but we support escape in type desc "Lcom/dex2jartu1234;"
dex-writer [To be published] write dex same way as dex-reader.
diStorm3:
diStorm is a lightweight, easy-to-use and a fast decomposer library. It disassembles instructions in 16, 32 and 64-bit modes. It is also the fastest disassembler library. The source code is very clean, readable, portable and platform independent (supports both little and big endianity). diStorm solely depends on the C library. Therefore it can be used in embedded or kernel modules.

diStorm3 is backward compatible with the interface of diStorm64. However, make sure you use the new header files.

edb-debugger:
edb debugger is a Linux equivalent of the famous "Olly debugger" on the Windows platform. One of the main goals of this debugger is modularity. Some of its features are:

Intuitive GUI interface
The usual debugging operations (step-into/step-over/run/break)
Conditional breakpoints
Debugging core is implemented as a plugin so people can have drop-in replacements. Of course, if a given platform has several debugging APIs available, then you may have a plugin that implements any of them.
Basic instruction analysis
View/Dump memory regions
Effective address inspection
The data dump view is tabbed, allowing you to have several views of memory open at the same time and quickly switch between them.
Importing and generation of symbol maps
Various plugins
Jad Debugger:
Jad has been the most popular Java decompiler ever written. It is a command line utility written in C++. Several graphical shells are available that execute this program behind the scenes while providing the user with a more comfortable interface for source browsing, project management, etc. It is available in Kali Linux for debugging Java applications for reverse engineering and many other purposes.

Javasnoop:
JavaSnoop is an Aspect Security tool that allows security testers to test the security of Java applications easily. JavaSnoop is an example of how Aspect is leading the industry in providing Verification Services, and not just for your web applications.

JavaSnoop allows you to attach an existing process (like a debugger) and instantly begin tampering with method calls, run custom code, or just watch what's happening on the system.

OllyDbg:
OllyDbg is a 32-bit assembler level analyzing debugger for Microsoft Windows. Emphasis on binary code analysis makes it particularly useful in cases where the source is unavailable.

Features:

Intuitive user interface, no cryptic commands
Code analysis – traces registers, recognizes procedures, loops, API calls, switches, tables, constants, and strings
Directly loads and debugs DLLs
Object file scanning – locates routines from object files and libraries
Allows for user-defined labels, comments and function descriptions
Understands debugging information in Borland® format
Saves patches between sessions, writes them back to executable file and updates fixups
Open architecture – many third-party plugins are available
No installation – no trash in registry or system directories
Debugs multithread applications
Attaches to running programs
Configurable disassembler supports both MASM and IDEAL formats
MMX, 3DNow! and SSE data types and instructions, including Athlon extensions
Full UNICODE support
Dynamically recognizes ASCII and UNICODE strings – also in Delphi format!
Recognizes complex code constructs, like call to jump to procedure
Decodes calls to more than 1900 standard API and 400 C functions
Gives context-sensitive help on API functions from external help file
Sets conditional, logging, memory and hardware breakpoints
Traces program execution, logs arguments of known functions
Shows fixups
Dynamically traces stack frames
Searches for imprecise commands and masked binary sequences
Searches whole allocated memory
Finds references to constant or address range
Examines and modifies memory, sets breakpoints and pauses program on-the-fly
Assembles commands into the shortest binary form

Reverse Engineering Malware — Main A
Valgrind:
Valgrind is a suite for debugging and profiling Linux programs. With its tool, we can automatically identify memory management and threading bugs, by eliminating hours of provoking bug-hunting and make programs more stable. We can also perform detailed profiling to help speed up program's processes and use Valgrind to build new tools. The Valgrind distribution currently includes six production-quality tools:

a memory error detector (Memcheck)
two thread error detectors (Helgrind and DRD)
a cache and branch-prediction profiler (Cachegrind)
a call-graph generating cache and branch-prediction profiler (Callgrind)
a heap profiler (Massif)
It also includes three experimental tools:

a stack/global array overrun detector (SGCheck)
a second heap profiler that examines how heap blocks are used (DHAT)
a SimPoint basic block vector generator (BBV)
Manufacturers look at reverse engineering as an important means to sustain competition, or some may take it as a tool to understand flaws in the design and re-work for the same. However, Kali Linux provides us with some great and well known reverse engineering tools to perform such activities. Moreover, there are many other reverse engineering tools as well, but these tools are already built-in and come out of the box with Kali Linux.
