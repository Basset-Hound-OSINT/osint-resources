Apriorit’s top reverse engineering tools
It’s hard to name the best software for reverse engineering. There are quite a few options, and each tackles a specific task in the multistep reversing process.

Static analysis tools allow reverse engineers to disassemble unknown files and examine their code without executing them. This helps them understand the structure of software and detect potential vulnerabilities.
Portable executable (Windows) analysis tools focus on understanding how an application behaves after launch, providing insights into its dependencies, execution flow, and modifications to system resources.
Dynamic analysis tools allow researchers to observe a program in action, tracking its runtime behavior, system interactions, and potential security risks.
Network traffic analysis tools monitor and dissect communication between applications, revealing data exchanges, API calls, and potential vulnerabilities in network protocols.
Below, we overview the main tools used for different reverse engineering tasks by Apriorit researchers:

Table 1. Top reverse engineering tools by category

Category	Tools
Static analysis	IDA Pro
ImHex
Ghidra
Radare2
Portable executable (Windows) analysis	PEiD
Scylla
Relocation Section Editor
CFF Explorer
Dynamic analysis	x64dbg
Frida
API Monitor
Network traffic analysis	Wireshark
Fiddler
Let’s get started.

1. IDA Pro
IDA Pro is one of the best software reverse engineering tools. This interactive disassembler has a built-in command language (IDC) and supports many executable formats for various processors and operating systems. IDA Pro also has a great number of plugins that can extend the functionality even further.

Screenshot 1. IDA Pro interface
Screenshot 1. IDA Pro interface
The main advantage of IDA Pro is that it allows you to interactively change any element of the displayed data in many ways, including:

Giving names to functions, variables, data structures, etc.
Changing how data is represented (as numbers, strings in various encodings, data structures)
Building diagrams and code flow graphs to simplify the understanding of disassembled code
Using type information about function arguments and structure definitions from C++ so that arguments and variables are automatically named
Automatically recognizing and naming standard library functions in assembler code
Aside from the disassembler itself, let’s also look closer at some IDA plugins.

Hex-Rays Decompiler
This IDA plugin can turn native processor code into a more readable C-like version. Hex-Rays Decompiler produces rather accurate C code comparable to that produced by a human reverse engineer. It correctly decompiles code produced by various C++ compilers, no matter the architecture.

However, Hex-Rays Decompiler might have issues with processing complex assembler code, where the original code was specifically modified by adding the inline assembler or manual optimizations were made.

Lighthouse
This plugin enables you to mark the execution path within the disassembler. As a result, you can understand which pieces of code take part in execution and whether they are involved in an algorithm or feature.

Basically, Lighthouse loads reports from code coverage tools into the IDA database and marks pieces of code depending on how many times they were executed. This makes it clear which parts of the code are worth your attention while browsing the disassembly.

ClassInformer
This plugin is intended to be used on binaries built by Visual Studio and searches for RTTI information stored in the data section of the executable file. RTTI information allows the plugin to find class names and virtual methods of C++ classes and name them for the user. Also, ClassInformer can present you with a list of found classes.

BinDiff by zynamix
This tool uses the IDA engine to compare binaries as assembler code instead of a stream of bytes. BinDiff can pinpoint differences in the code of two versions of the same program (down to changes in a specific function) as a list of added, removed, or replaced instructions. Changes can also be represented as code flow graphs.

IDA-Function-Tagger
This plugin analyzes imported functions (and functions that call them). It then groups all of these functions by tags: cryptography-related, registry-related, network-related, etc. Such grouping makes it easier to find the part of the code responsible for specific operations.

ida-x86emu
This plugin emulates the execution of disassembled code without the need to run the application under analysis in a debugger. Using ida-x86emu, you can emulate the result of executing any piece of code without the risk of modifying something in the system. All you need to do is specify the start values of CPU registers. Then you can do a step-by-step execution.

Read also

How to Reverse Engineer Windows Software the Right Way: A Practical Example

Discover how ethical reverse engineering practices can drive innovation of Windows software, enhance product development, and uncover competitive advantages for your business.

windows software reverse engineering
2. ImHex
ImHex is a powerful modern cross-platform tool for inspecting, analyzing, and visualizing binary data. It provides advanced features beyond traditional hex editors, making it useful for programmers, security researchers, and reverse engineers.

This tool also supports:

Custom pattern language — ImHex supports its own data representation language similar to C++/Rust so you can see the binary data in a convenient, structured way. It ships with some popular pattern scripts like PE, pcap, and mach-o, but you also can write your own patterns.
Rich data visualization features — Displaying entropy, bytes distribution, and types as a graph is very useful for analyzing binaries.
Disassembler — Supports popular architectures (x64, x86, ARM, and lots of others).
Powerful advanced searching — Search for strings, byte sequences, regexes, binary patterns, or numbers.
Screenshot 2. ImHex interface
Screenshot 2. ImHex interface
Screenshot 3. ImHex interface
Screenshot 3. ImHex interface
3. Ghidra
Ghidra is an open-source and cross-platform reverse engineering tool that helps users analyze binaries on many platforms (Windows, macOS, Linux). Ghidra supports a lot of popular formats such as PE, COFF, macOS, Mach-O, ELF, and DBG. It can disassemble instructions for x86, x86_64, ARM, AARCH64, and other architectures.

Ghidra interface
Screenshot 4. Ghidra interface
The main features of Ghidra include:

Code browser — Displays and helps you work with a program’s instructions and data.
Debugger — Relies on pluggable connectors for third-party debuggers, enabling Ghidra to be extended and integrated with additional debuggers.
Decompiler — Automatically converts the binary representation of individual functions into a high-level C representation.
Function bit patterns explorer — Discovers patterns in the bytes around function starts and returns.
Ghidra script manager — Allows for rapid development of extended Ghidra functionality.
4. Radare2
The Radare2 disassembler has all the IDA features without being as robust and stable, but it’s free and open-source. Radare2 itself is a console tool, but it has a Iaito front end, which makes it a true alternative to IDA and Ghidra.

Screenshot 5. Radare2 interface
Screenshot 5. Radare2 interface
Screenshot 6. Radare 2 interface
Screenshot 6. Radare2 interface
Alternatively, you can use Rizin, which is a fork of Radare2. Rizin combines the free and open-source nature of Radare2 with its own user-friendly GUI (called Cutter) and an improved decompiler, making it a potentially attractive alternative to commercial options like IDA or even Ghidra.

5. PEiD
PEiD is one of the best reverse engineering tools to detect an application’s packer. By analyzing specific signatures and characteristics, PEiD can detect whether an application is packed and which packer was used.

Screenshot 7. PEiD interface
Screenshot 7. PEiD interface
There are also various useful plugins that help to analyze PE files. For instance, the KANAL (Krypto Analyzer for PEiD) plugin analyzes a PE file for the presence of known encryption algorithms.

Read also

The Evolution of Reverse Engineering: From Manual Reconstruction to Automated Disassembling

Apply ethical reverse engineering to uncover vulnerabilities, enhance security measures, and make your product more reliable and trustworthy.

blog-89-article-5.jpg
6. Scylla
Scylla is a tool for dumping a running application process and restoring the PE import table. With its help, you can get a totally restored PE file that can be run by the operating system.

Screenshot 8. Scylla interface
Screenshot 8. Scylla interface. Image credit: Stack Exchange
This tool is especially useful in reverse engineering tasks where you need to recover a fully functional executable from a running process in memory. Here are some key features and capabilities of Scylla:

PE import table restoration — Restores missing or broken import tables, making the dumped application runnable.
Memory dumping — Dumps the contents of a running application, which is useful for packed or obfuscated executables.
Bypassing the security mechanisms — Helps bypass anti-debugging and anti-tampering mechanisms in applications.
Widely compatible — Scylla supports both 32-bit and 64-bit Windows applications.
At Apriorit, we use Scylla to analyze malware, recover lost executables from running processes, and debug software or analyze its behavior in a running state.

7. Relocation Section Editor
Relocation Section Editor is an application used for editing the relocation table in PE files. The main purpose of this tool is to modify the relocation table in case of patching relocatable pieces of code. But it’s often used to remove the relocation table altogether when restoring a protected file.

Screenshot 9. Relocation Section Editor interface
Screenshot 9. Relocation Section Editor interface
A protected file actually contains the relocation table for the unpacker code only. The relocation table for the real code is usually hidden within the unpacker data. Thus, in case a dump is recovered, there are two ways to restore the missing relocation table for the real code:

Force the application to be loaded at two different base addresses, then compare the dumps to see which parts of the code are patched and make a new relocation table.
Remove the relocation table completely and specify in the PE file header that the file is not relocatable.
8. CFF Explorer
CFF Explorer is a suite of tools for PE editing that includes:

PE and HEX editors
Resource editor
Import editor
Signature scanner
Address converter
Disassembler
Dependency analyzer
And more
Screenshot 10. CFF Explorer interface
Screenshot 10. CFF Explorer interface
CFF Explorer streamlines tasks like editing PE files, debugging software, and ensuring compatibility across different systems. At Apriorit, we use it to inspect, modify, and understand executable files.

9. x64dbg
x64dbg is an open-source debugger for Windows, designed for analyzing, reverse engineering, and debugging x86 (32-bit) and x64 (64-bit) applications. It is commonly used for analyzing malware, cracking software, and understanding how applications work at a low level.

Screenshot 11. x64dbg interface
Screenshot 11. x64dbg interface
Key features of x64dbg include:

A simple and user-friendly yet powerful debugging interface
Ability to debug DLLs without needing to load them into a process by yourself
Support for plugins
10. Frida
Frida is a dynamic instrumentation toolkit that allows you to hook into and modify the behavior of software at runtime. It is widely used for reverse engineering, security research, debugging, and application testing. You can use JavaScript and Python scripts to control the runtime of the instrumented process.

Screenshot 12. Frida interface
Screenshot 12. Frida interface
Frida allows you to:

Hook into a running process, tracing system API calls without patching application code. This allows you to trace:
File system
Network
Registry
Other system API calls
Modify the behavior of called functions (for example, change the arguments or hijack returned values)
Bypass some limitations on mobile applications (such as SSL pinning when analyzing traffic for an application)
Frida allows you to hook into applications running on Windows, macOS, Linux, iOS, and Android.

11. API Monitor
API Monitor is designed to intercept API function calls made by applications and services. It allows you to view both the input parameters and output data of these calls, making it an invaluable resource for reverse engineering API calls.

Screenshot 13. API Monitor’s API Capture Filter interface
Screenshot 13. API Monitor’s API Capture Filter interface
By default, API Monitor contains definitions for over 13,000 API functions and more than 1,300 COM interface methods, which makes it an extensive and powerful tool for analyzing and debugging software interactions with the Windows API and COM-based components.

Read also

How to Reverse Engineer an iOS App and macOS Software

Explore how reverse engineering can enhance the security and reliability of your macOS or iOS solution and ensure compliance with strict security standards.

blog-article-how-to-reverse-engineer-os-x-and-ios-software
12. Wireshark
Wireshark is a network analysis tool that allows you to capture, inspect, and analyze network traffic in real time. It also lets you work with already captured traffic (pcap files) and may help you with low-level protocol reverse engineering by capturing and analyzing traffic of an application, virtual machine, or any device that routes traffic through your machine.

Screenshot 14. Wireshark interface
Screenshot 14. Wireshark interface
Wireshark supports:

Capturing live packets/frames from different sources, such as Wi-Fi, Ethernet, Bluetooth, and USB.
Displaying detailed packet information, including headers and payload
Hundreds of network protocols, such as TCP, UDP, HTTP, DNS, TLS, and IEEE802.11.
Checksum verification
Powerful display filtering capabilities
Export to pcap files to work with captured traffic later
13. Fiddler
Fiddler is a proxy that you can use to intercept, monitor, and analyze HTTP/HTTPS traffic going between your application and external services or servers. Fiddler can intercept HTTP/HTTPS traffic system-wide. You can also add plugins (such as wbxml view, which can decode wbxml) and display requests/responses in different views.

Screenshot 15. Fiddler interface
Screenshot 15. Fiddler interface
Fiddler has a built-in hex editor and can generate new requests based on a selected request or create a custom request. In addition, the Request to Code plugin allows you to get ready code that executes requests in C#, Visual Basic, or Python.

These are the tools that reverse engineers at Apriorit often turn to when working on Windows reversing projects. As you can see, each piece of reverse engineering software tackles a specific set of tasks. In the next section, we provide practical examples of the role and importance of each of these tools in Windows reversing.

Related project

Improving a SaaS Cybersecurity Platform with Competitive Features and Quality Maintenance

Explore how Apriorit’s skilled reverse engineers helped our client analyze and improve their complex software.

Improving a SaaS Cybersecurity Platform with Competitive Features and Quality Maintenance
Practical example of working with non-AI reverse engineering software
Let’s see how we can use each of these tools to research a Windows application. As an example, we are going to use a test application [.exe] that you can download and analyze on your own.

1. Open the executable to be researched with IDA Pro
When we load our test application in IDA Pro, we receive the following message:

Screenshot 16. Error message displayed by IDA Pro
Screenshot 16. Error message displayed by IDA Pro
This means that something has gone wrong with the application: its import table can’t be found. At this point, we only need to choose OK. Once we do that, IDA Pro provides us with the following results of application analysis:

Screenshot 17. Application analysis results in IDA Pro
Screenshot 17. Application analysis results in IDA Pro
Screenshot 18. Test application’s import table
Screenshot 18. Test application’s import table
As you can see, the import table is almost empty. Its upper part shows that it was possible to detect a small piece of code (the blue part), and the left part shows which functions were detected (in our case, very few).

There is also a set of undetected bytes above the start function. We suppose that the application is packed by means of some packer. PEiD will help us determine which packer was used.

2. Get information about the packer with PEiD
Now, we need to load our application in PEiD.

Screenshot 19. Application info displayed in PEiD
Screenshot 19. Application info displayed in PEiD
In Screenshot 19 above, you can see that the Entry Point is located in the UPX1 section. However, this fact alone doesn’t really tell us much, so we need to run a scan.

To start the scanning process, go to Options, choose Hardcore Scan, then choose Save:

Screenshot 20. Configuring the scanning process in PEiD
Screenshot 20. Configuring the scanning process in PEiD
Next, select the folder where the application is located. After scanning is complete, we receive the following result:

Screenshot 21. The result of application scanning with PEiD
Screenshot 21. The result of application scanning with PEiD
As you can see from Screenshot 21, the application is packed using the UPX tool. To unpack it, we will use CFF Explorer.

3. Unpack the application with CFF Explorer
To unpack our sample application with CFF Explorer, we need to go to the UPX Utility page in the main menu of CFF Explorer and choose Unpack:

Screenshot 22. Unpacking the application in CFF Explorer
Screenshot 22. Unpacking the application in CFF Explorer
After that, we can upload the unpacked application to IDA Pro and restore the assembler code.

When we upload our application to IDA Pro once more, the system asks us whether we want to upload symbols from the server, and we agree. Here is the result of application analysis in IDA Pro:

Results of IDA Pro analysis for the unpacked application
Screenshot 23. Results of IDA Pro analysis for the unpacked application
Screenshot 24. The import table of the unpacked application
Screenshot 24. The import table of the unpacked application
You can see in Screenshot 23 that we now have some readable code, more detected functions, and an import table (Screenshot 24). At this point, we can run the application and debug it in IDA Pro. In the disassembler, we choose Debugger > Select Debugger > Local Win32 debugger and then press F9. After that, we receive the following warning message:

Debugger detection message
Screenshot 25. Debugger detection message
Our tested application detected that it was being debugged. To continue with our analysis, we need to disable debugger detection.

See the import table:

Screenshot 26. The NtQueryInformationProcess function
Screenshot 26. The NtQueryInformationProcess function
Right away, we notice the NtQueryInformationProcess function. After clicking on it, we get the following list of xref functions:

Screenshot 27. xref functions of the NtQueryInformationProcess function
Screenshot 27. xref functions of the NtQueryInformationProcess function
By clicking on the function, we can see where it’s called. The third parameter is an output parameter. If it equals 1, then a debugger is attached to the application; if it equals 0, there’s no debugger attached.

Let’s see where the result of this function is written:

Screenshot 28. Analysis of the NtQueryInformationProcess function
Screenshot 28. Analysis of the NtQueryInformationProcess function
As we can see in Screenshot 28, the third parameter contains the address of the local variable (var_8). After a function call, the result of the function is checked (test eax, eax). Then the value of var_8 is checked, and if it’s not 0, the value is written to the byte_131443C variable.

Let’s check if byte_131443C is used somewhere else in this function:

Screenshot 29. Checking where else the byte_131443C variable is used
Screenshot 29. Checking where else the byte_131443C variable is used
We’ll start from the end. This value contains the result from al (lower bytes). Before that, the esi result is written to eax, and 1 is written to esi. Above, we see the condition for writing 1 to esi: if ecx + 2 does not equal 0. The value in ecx is large fs:30h (+ 2). It verifies that a debugger’s presence has bypassed the IsDebuggerPresent function (a field of undocumented PEB structure).

Let’s rename this variable. To do so, press N, or right-click on the function and select Rename.

Now we need to check if the g_isDebbugerPresent variable is used anywhere else:

Screenshot 30. Details of the g_isDebbugerPresent variable
Screenshot 30. Details of the g_isDebbugerPresent variable
We see “…” at the end, so this variable is used in more than one place. Hover the cursor over the variable and click X, or right-click and select Jump to xref to operand:

Screenshot 31. Places where the g_isDebbugerPresent variable is used
Screenshot 31. Places where the g_isDebuggerPresent variable is used
We already know the first four places where this variable is used, but not the last. Let’s find it:

Details of IsDebuggerPresent function’s use
Screenshot 32. Details of IsDebuggerPresent function’s use
In Screenshot 32, we see that the variable checks if esi equals 0, and if it doesn’t, we receive the message that there is a debugger.

Luckily, this verification can be removed.

It’s noteworthy that IDA Pro also allows for patching memory and code. In order to quickly find the necessary piece of code, we’ll run the Rebase program in IDA Pro to get the same offset as in Ghidra. In IDA Pro, select Edit > Segments > Rebase program and enter the value 0x400000 in the opened window:

The Rebase program in IDA Pro
Screenshot 33. The Rebase program in IDA Pro
Let’s get the address of the code that performs the comparison. As you can see from Screenshot 34 below, the address is 0х4012F0:

Screenshot 34. Finding the instruction address
Screenshot 34. Finding the instruction address
We need to write down this address, as we are going to use it later in Ghidra.

Read also

How to Reverse Engineer a Proprietary File Format: A Brief Guide with Practical Examples

Want to enhance your product’s interoperability? Discover how to reverse engineer proprietary file formats in our comprehensive guide.

reverse-engineer-a-proprietary-file-format.jpg
4. Modify the executed statements in Ghidra
Now we need to load our application in Ghidra. Create a project by choosing File → New Project…

Then, choose the green dragon icon in Tool Chest, which represents Ghidra’s CodeBrowser.

Screenshot 35. Project view in Ghidra
Screenshot 35. Project view in Ghidra
Press I to import the executable into the workspace. After that, Ghidra will suggest analyzing the executable. Choose Analyze.

Now, let’s proceed to examine our address 0x4012F0. Press G and type the address 0x4012F0 into the box:

Screenshot 36. Using Ghidra navigation
Screenshot 36. Using Ghidra navigation
Screenshot 37. Code for comparing the g_isDebbugerPresent variable
Screenshot 37. Code for comparing the g_isDebbugerPresent variable
Now, we can replace this code with, say, jmp to jump to a specific address so that this condition is never satisfied. (In most cases, it can jump to the code we want to be executed next.)

Let’s jump to the address 0x40130E.

Screenshot 38. Instruction at address 0x40130E
Screenshot 38. Instruction at address 0x40130E
Right-click on this instruction address and select Patch Instruction.

Screenshot 39. Patch instruction menu in Ghidra
Screenshot 39. Patch instruction menu in Ghidra
Screenshot 40. Changing the code for the g_isDebbugerPresent variable
Screenshot 40. Changing the code for the g_isDebbugerPresent variable
After patching it, we see some leftover bytes because the instruction length has been decreased.

Screenshot 41. Leftover bytes
Screenshot 41. Leftover bytes
Patching a longer instruction with a shorter one is not a problem because we can create padding with NOP instructions. Let’s patch the leftover bytes:

Screenshot 42. Result
Screenshot 42. Result
If we try to run our test application now, it crashes. When looking at the assembler code, we see that the new jmp will call ESI further down the code, and ESI will contain garbage instead of the MessageBox function address. Since we’re jumping over the address 0x004012F8, we’re skipping mov esi, dword ptr [→USER32.DLL::MessageBoxA]. Thus, ESI will not be initialized, and the application will crash at 0x0040130E.

Screenshot 43. The part of the code where the application crashes
Screenshot 43. The part of the code where the application crashes
Therefore, let’s be creative and jump to 0x004012F7 to move the MessageBoxA function address to ESI. This way, we also don’t skip the PUSH ESI command to avoid stack corruption (we have the POP ESI command at 0x0040132B). After that, let’s jmp to 0x00401317, the control flow branch where the application is considered to be registered, and replace 0x003D131E with NOPs.

Screenshot 44. Patched instructions
Screenshot 44. Patched instructions
This is what we get:

Screenshot 45. cmp data in IDA Pro
Screenshot 45. cmp data in IDA Pro
The cmp command is double-byte, starting with 12F0, and the address starts with 12F2. We can see that jmp is a one-byte command and that its 05 address is relative, meaning it shouldn’t be in the relocation table.

Screenshot 46. jmp data in IDA Pro
Screenshot 46. jmp data in IDA Pro
To remove the 12F2 value from the relocation table, we need to open the current version of our test application with the Relocation Section Editor.

5. Delete a value from the relocation table with Relocation Section Editor
We start by loading the test application and finding the target value: 0x004012F2.

Screenshot 47. Application values displayed in the Relocation Section Editor
Screenshot 47. Application values displayed in the Relocation Section Editor
Next, we remove the target value and save the test application.

Screenshot 48. Result
Screenshot 48. Result
Related project

Developing and Supporting a CRM System for a Medical Transportation Company

Explore how Apriorit enhanced our client’s customer interactions and streamlined workflows through building a custom CRM solution and support system.

Developing and Supporting a CRM System for a Medical Transportation Company
6. Modify values in the relocation table with CFF Explorer
Now, it’s time to open our test application in CFF Explorer. We have found the value — 1332 — on which delta for MessageBox used to be added.

Screenshot 49. Value for adding MessageBox delta
Screenshot 49. Value for adding MessageBox delta
Let’s replace the value 1332 with the value 132B, the new offset by which MessageBox can be found. If we run the test application now, it won’t crash or show a warning message about a detected debugger.

Next, we move to working with the MessageBox function calls.

7. Monitor the application with API Monitor
This program can monitor a number of known API functions out of the box. You can also add your own functions to API Monitor and use this tool to monitor network function calls and research passed parameters (of course, if traffic is not encrypted).

Let’s monitor our application. We’ll try to find the call for the MessageBox function:

Screenshot 50. MessageBox function calls
Screenshot 50. MessageBox function calls
We’re interested only in the API functions that can show a message window. So we select only them in User32.dll.

In API Monitor, select File > Monitor New Process and set the path to our file. After running our process, we see the list of called functions. Let’s try to find MessageBox:

The MessageBox function in API Monitor analysis results
Screenshot 51. The MessageBox function in API Monitor analysis results
API Monitor shows which parameters were passed to the MessageBox function. We can also set different breakpoints for a function:

Screenshot 52. Function breakpoint options in API Monitor
Screenshot 52. Function breakpoint options in API Monitor
If we run monitoring of our file, we’ll get the following results:

Screenshot 53. Results of application monitoring in API Monitor
Screenshot 53. Results of application monitoring in API Monitor
Screenshot 53 also shows the parameters passed to the MessageBox function.

Read also

Reverse Engineering in Cybersecurity: Apriorit’s Best Practices

Uncover vulnerabilities and enhance your software protection with reversing! Learn about reverse engineering best practices you can add to your cybersecurity strategy.

Reverse Engineering in Cybersecurity
8. Determine a binary type with ImHex
Now, we move to working with binaries so we can find the code that we previously detected with IDA Pro and API Monitor. But before exploring a binary, we need to determine its type with a hex editor. In our example, we use ImHex.

Open the file with ImHex:

Screenshot 54. Application data in ImHex
Screenshot 54. Application data in ImHex
The MZ signature at the zero offset corresponds to PE format files (executables or shared libraries), so this is an .exe or .dll file.

Most file formats have unique signatures. For example, here’s what a dump file looks like in ImHex:

Screenshot 55. Example of a dump file processed by ImHex
Screenshot 55. Example of a dump file processed by ImHex
9. Recover the original executable with Scylla
To show you how to work with Scylla, we will once again use a packed application, but we won’t unpack it this time. Instead, we’ll dump its memory and try to run it.

To do that, we open the packed executable file in IDA Pro. This time, we need to find the original entry point (OEP) of the application rather than the entry point of the packer.

Screenshot 56. Searching for the application’s original entry point with IDA Pro
Screenshot 56. Searching for the application’s original entry point with IDA Pro
The pusha command saves general-purpose registers to the stack. In the end, there should be the popa command which pushes the stored register values. After the popa command, there is a jmp to the original point of entry. You can use the Search for text option by pressing Alt + T and look for the popa command.

Screenshot 57. The popa command
Screenshot 57. The popa command
Below the popa command is jmp 40A191, which will eventually move to the original entry point.

Let’s put a breakpoint in jmp and run the debugger, then try to follow jmp. As a result, IDA Pro displays another warning message:

Screenshot 58. No code warning message in IDA Pro
Screenshot 58. No code warning message in IDA Pro
This message means that there is no code at the point we’re going to. Therefore, IDA will create instructions in disassembled listings on the basis of bytes pointed to by the Extended Instruction Pointer (EIP).

Screenshot 59. The address of the application’s original entry point
Screenshot 59. The address of the application’s original entry point
0x00971A91 is the address of the original entry point after unpacking the application into memory.

Read also

Web Application Penetration Testing: Minimum Checklist Based on the OWASP Testing Guide

Identify vulnerabilities before hackers do to safeguard your software from cyber threats with our comprehensive guide to penetration testing using the OWASP checklist.

v1-1 -blog-article-Update-Anti-Debugging-Protection-Techniques-with-Examples-cover
Now, without closing IDA Pro, open Scylla in order to create the application’s dump and restore the application’s import table from it.

In the process list, choose our application and put the OEP address into the field. Then choose IAT Autosearch > Get imports. As a result, Scylla will show that the import table has been found.

Screenshot 60. Processing a test application with Scylla
Screenshot 60. Processing a test application with Scylla
Let’s make an application dump: choose Dump, save the dump, then choose Fix Dump and select the previously saved application.

If we run our application now, it will crash, so we need to remove the relocation table. To do so, open the modified dump file (it has the _SCY prefix) in CFF Explorer.

Screenshot 61. Working with the modified application dump file in CFF Explorer
Screenshot 61. Working with the modified application dump file in CFF Explorer
Set 0 in the Relocation Directory RVA field.

Next, we need to check whether the ImageBase is the same as the application loaded into memory.

Screenshot 62. Application’s ImageBase data in CFF Explorer
Screenshot 62. Application’s ImageBase data in CFF Explorer
You can find the ImageBase value in IDA Pro by going to Edit > Segments > Rebase program.

Screenshot 63. Configuring IDA Pro for ImageBase analysis
Screenshot 63. Configuring IDA Pro for ImageBase analysis
Let’s save and run the test application. Now, it will run as if it were packed, and we’ll be able to see how the program works without any protection or obfuscation.

In the next section, our experts show where AI can bring practical benefits and how it integrates with existing tools. We also provide a concrete example of integrating AI in reverse engineering.

AI-assisted software reverse engineering
Given the ease of integrating AI into existing reversing frameworks, AI-assisted reverse engineering is no longer a theoretical concept. Reverse engineering often involves repetitive work with decompiled code, which requires significant manual effort. Recent advances in large language models (LLMs) show that they can handle such tasks effectively, as decompiled code, like natural language, follows patterns and depends on context.

You can already use today’s general-purpose models to assist with many tasks — and they require relatively little setup. However, it’s worth noting that AI for reverse engineering should be treated as an assistant rather than an authoritative source. Each suggestion still requires human verification to avoid mistakes or misleading results.

Approaches to using AI for reverse engineering tasks
There are several practical ways to introduce AI into reverse engineering workflows:

Ad-hoc use. The simplest approach is copying decompiler output into an AI assistant and asking for explanations or suggestions. This method works for quick checks but is inefficient for large projects.
IDE or plugin integration. Some decompilers and editors support plugins that send code fragments directly to AI models and return annotations within the interface. This reduces context switching and is more scalable.
Programmatic agent integration. Using frameworks such as the Model Context Protocol (MCP), AI agents can interact directly with the decompiler’s database. This allows agents to list functions or classes, run decompilation, rename items, and follow cross-references. Essentially, it automates sequences of operations that engineers usually perform manually.
These approaches vary in maturity, but even basic integrations can already reduce routine effort and accelerate early analysis.

Note: MCP-based AI integrations are still in early development. Simple queries like asking about a single function usually work well, while complex requests (for example, bulk renaming or large-scale decompilation) often fail or only partially succeed. Always be ready to rephrase prompts and verify results.

Both IDA and Ghidra now offer MCP-compatible servers, making them good candidates for experimenting with AI-assisted workflows. While MCP is not yet fully mature, it provides a promising foundation for building more robust automation in reverse engineering.

Practical example of AI-assisted reverse engineering using Ghidra with MCP
Our engineers use MCP, as it enables structured interactions between AI agents and reverse engineering tools. To illustrate the scope of MCP’s capabilities, we set up the following environment:

Ghidra 11.3.2
Ghidra MCP 1.4 server
5ire MCP client
OpenAI GPT 4.1 mini
After connecting the tools and providing an API key, we loaded a test application [.exe] (an unpacked sample that we used earlier in another example) and began experimenting with AI-assisted analysis.

Step 1. Renaming functions
The binary contained a number of unnamed functions with automatically generated labels in the form of FUN_*. As you can see in screenshot 64 below, these generic names make navigation unmanageable.

Examples of unnamed functions in a test application [.exe]
Screenshot 64. Examples of unnamed functions in a test application [.exe]
With the help of an AI agent, we requested more descriptive function names. Here is what the prompt and the output look like.

Prompt for giving descriptive names to unnamed functions
Screenshot 65. Prompt for giving descriptive names to unnamed functions
The output provided clearer identifiers that improved the readability of the codebase.

Step 2. Preparing a TLS callback for analysis
Next, we examined a TLS callback function suspected of checking for the presence of a debugger. Before analyzing its logic, we asked the AI agent to rename the function’s variables for clarity.

Prompt for renaming variables in a function
Screenshot 66. Prompt for renaming variables in a function
After making these changes, we then requested a plain-language summary of the function’s purpose.

Prompt for defining the purpose of the TLS callback
Screenshot 67. Prompt for defining the purpose of the TLS callback
The result aligned with our earlier manual conclusions, confirming that the callback includes anti-debugging behavior.

Step 3. Analyzing a more complex algorithm
Since the first sample of a test application [.exe] offered a limited variety, we turned to a second test case: a note-taking application. In this program, we identified a moderately complex function that manipulated arrays. For readability, we transferred the C-like decompiled output into Visual Studio Code.

An example algorithm working with arrays
Screenshot 68. An example algorithm working with arrays
After prompting the AI, we received a structured explanation of the function’s behavior, which helped clarify its role in the broader logic of the application.

AI agent’s explanation of the previously shown function
Screenshot 69. AI agent’s explanation of the previously shown function
Step 4. Renaming variables and parameters
Finally, we asked the AI agent to rename all remaining parameters and variables in the insertOrUpdatePairInArray function. If this function call leads to calling other functions, the agent should rename them as well. We trimmed the verbose AI output for review:

AI agent’s attempt at renaming all objects in the function
Screenshot 70. AI agent’s attempt at renaming all objects in the function
Although we could still see some inconsistencies, the changes improved overall code readability.

This short experiment shows how AI can reduce time spent on repetitive renaming and documentation tasks while also providing quick insights into specific functions. However, the results still need careful manual review. For now, using AI for reverse engineering should be treated as a supportive tool rather than a replacement for manual analysis.

How Apriorit can help you with reverse engineering
Apriorit’s reverse engineering team has been helping businesses dissect software to optimize it, find vulnerabilities, or plan its modernization for over 20 years.

We specialize in non-trivial challenges and can deconstruct even the most complex systems. Our team has successfully reversed various types of projects, from cybersecurity solutions and legacy applications to proprietary protocols and obfuscated software.

Apriorit reverse engineering services
We strictly adhere to legal and ethical standards, conducting only lawful reverse engineering for purposes such as security analysis, system integration, and performance optimization. Before taking on a project, we carefully evaluate its legal aspects.

When you work with us, you get:

Clear insights into your software – Get a detailed breakdown to fill in the gaps in your documentation and allow your team to work with your software further depending on your specific goal.
A detailed report on your software’s current state – At the end of the project, you’ll get a detailed report outlining our research, methodologies, and findings. This helps you address security risks, recover lost functionality, and make informed decisions about further development.
A roadmap to solving your challenges – Along with the report, you’ll also get a list of recommendations on how to mitigate blockers that prevent you from migrating, securing, or integrating your software. Our team can also follow these recommendations to help you get a ready solution for your needs.
Apriorit is a trusted partner with the expertise to handle complex reverse engineering tasks using the best reverse engineering software.
