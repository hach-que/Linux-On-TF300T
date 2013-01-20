<!-- vim: set syntax=markdown: -->

Building the kernel
=============================

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

Continue onto [building the Android tools](android-tools.md)...
