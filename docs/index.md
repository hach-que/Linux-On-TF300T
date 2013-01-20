<!-- vim: set syntax=markdown: -->

Building OpenSUSE on TF300T
=============================

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

cb22 also provides a configuration setup for building a kernel for the TF300T.  You can
automatically get the required configuration by typing

```
> make cb22_defconfig
```

<!--

Type the following command to bring up the configuration utility:

```
> make menuconfig
```

Configure the following options:

  * Device Drivers
    * ASUS GPS -> include (not module)
    * Input device support
      * Generic input layer
        * Touchscreens
          * Atmel mXT I2C Touchscreen -> include (not module)
    * Graphics support
      * Tegra graphics host driver -> include (not module)
      * Tegra Display Controller -> include (not module)
  * System Type
    * ARM system type -> "NVIDIA Tegra" (scroll down)
    * Tegra 3 family SOC -> enable
    * Cardhu board -> enable
      * Cardhu wifi activator -> include (not module)
  * Kernel features
    * Symmetric Multi-Processing -> enable
    * Support for hot-pluggable CPUs -> enable (should be by default)

-->

Apply kexec-hardboot patch
-----------------------------

If you want to multiboot the TF300T, you need to add support for kexec-hardboot.  The
patch to add this functionality is located in the `linux` folder and can be applied
like so:

```
> cd kernel-tf300t
> git am ../kexec-hardboot.patch
```

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

Build Android tools
---------------------

We need to have the `mkbootimg` program so that we can prepare the final image for flashing.
Under the `android` directory of the repository, a small subset of the Android system/core
source code is present that contains the required code.

You can prepare the required tools by typing in that directory:

```
./prepare
```

Create initrd and boot image
---------------------------------

Now we're going to create the initrd and the boot image.  This will contain both the kernel
and the initrd, which we can flash to the TF300T.

The initrd is a set of files stored in CPIO format, then GZIPd.  In the case of Android, we
use BusyBox to get this done since it's statically linked and very simple to use.  All we're
doing in the case of OpenSUSE is using it to mount devices and then calling `switch\_root` to
start the systemd boot.

For OpenSUSE, there is a directory called `opensuse` in the repository containing a script
which will prepare the initrd information and create the final image.

Enter that directory and then type:

```
./prepare
```

You should end up with a `kernel.blob` file in the `opensuse/build` folder.  This is what will
be flashed to the device.
