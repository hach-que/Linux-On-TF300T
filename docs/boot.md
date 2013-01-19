<!-- vim: set syntax=markdown: -->

Boot Process
=====================

Boot Structure
-----------------

There are a varity of flash partitions under Android, such as:

  * boot - The main boot partition containing a kernel and initrd.
  * recovery - The recovery boot partition containing a kernel and initrd.
  * system / cache / data / etc. - Android specific stuff.

The important ones are `boot` and `recovery`.

ClockworkMod Recovery
------------------------
Notably you will most likely (or should have) installed [ClockworkMod Recovery](http://forum.xda-developers.com/wiki/ClockworkMod_Recovery)
to the `recovery` partition.  There is a really good tutorial on [XDA Forums](http://forum.xda-developers.com/showthread.php?t=2041627)
about getting ClockworkMod Recovery installed, however for the purposes of getting
OpenSUSE onto the tablet, you will only want to complete up to the "Installing ClockworkMod Recovery"
(and not perform the "Flashing a custom ROM" step).

What we're going to do
------------------------

We are going to overwrite the `boot` partition with a new kernel and initrd.
**Make sure you have backed up the system with ClockworkMod Recovery before flashing `boot`!**
However, before we can do this, we need to build the Linux kernel and create an
initrd image.  In addition, we will also need to prepare this into a single flashable
image with `mkbootimg`.

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

Getting the kernel source
--------------------------

cb22 has already provided a modified version of the Linux kernel for the TF300T.  This
can be downloaded from `https://bitbucket.org/cb22/tf300tg-kernel-source`.  Use git to
clone this to a directory.

Configuring the kernel
-------------------------

Type the following command to bring up the configuration utility:

```
> make menuconfig
```

Configure the following options:

  * Device Drivers
    * `ASUS GPS` -> include

Build the kernel
-------------------

Now type:

```
> make
```

to build the kernel!  This will take quite some time.

As the kernel is building, you might want to confirm that it's actually building for ARM.  After
it has started building the "kernel/" directory, you can type the following in another terminal
to verify that it's ARM:

```
> file kernel/cpu.o
kernel/cpu.o: ELF 32-bit LSB relocatable, ARM, version 1, not stripped
```
