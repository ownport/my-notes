# strace

[strace](http://sourceforge.net/projects/strace/) is a debugging utility for Linux and some other Unix-like systems to monitor the system calls used by a program and all the signals it receives, similar to "truss" utility in other Unix systems. 

## Usage 

The most common usage is to start a program using strace, which prints a list of system calls made by the program. This is useful if the program continually crashes, or does not behave as expected; for example using strace may reveal that the program is attempting to access a file which does not exist or cannot be read.

An alternative application is to use the -p flag to attach to a running process. This is useful if a process has stopped responding, and might reveal, for example, that the process is blocking whilst attempting to make a network connection.

As strace only details system calls it cannot be used to detect as many problems as a code debugger such as GNU Debugger (gdb). It is, however, easier to use than a code debugger, and is an extremely useful tool for system administrators.


