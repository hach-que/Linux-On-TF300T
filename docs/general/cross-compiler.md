<!-- vim: set syntax=markdown: -->

The cross-compiler
=============================

**NOTE:** These instructions are dependent on the host distribution, however there are no instructions here that restrict what distro you can install on the TF300T.

Install cross-compiler
-------------------------

You can install the GCC cross-compiler for ARM from the [OpenSUSE Build Service](http://software.opensuse.org/package/cross-arm-linux-gnueabi-gcc).
Select the version appropriate for your version of OpenSUSE from `home:duwe:crosstools` and install it.

This won't automatically install Glibc for ARM, which is also required.  Install `cross-arm-linux-gnueabi-glibc` and `cross-arm-linux-gnueabi-kernel-headers`
from `home:duwe:crosstools`.  If the repository has been added from installing GCC, you can just type:

```
> zypper in cross-arm-linux-gnueabi-glibc cross-arm-linux-gnueabi-kernel-headers
```

to install them.

Test cross-compiler
--------------------

It's important to make sure the cross-compiler is actually functioning on your system before we use it
to build the kernel.  Create a small C program as follows:

```
int main() { return 0; }
```

Compile it and test with the `file` command; you should get:

```
> /opt/cross/bin/arm-linux-gnueabi-gcc test.c
> file a.out
a.out: ELF 32-bit LSB executable, ARM, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.16, not stripped
```

This indicates we can now produce binaries for the ARM architecture.  There are files in the `cross-compiler/`
directory that you can use to build and compare against.

Configure environment
--------------------------------------

We will need the cross-compiler in our PATH and the correct ARCH and CROSS_COMPILE
variables to be set for building the kernel.  You can set these up with:

```
export PATH=/opt/cross/bin:$PATH
export ARCH=arm
export CROSS_COMPILE="arm-linux-gnueabi-"
```

You will need to do this for each shell you open; alternatively you can add it to your .bashrc
for it to be permanently in your PATH.

Continue onto [building the kernel](kernel.md)...
