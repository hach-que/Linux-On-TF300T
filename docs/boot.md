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

Getting the kernel source
--------------------------

cb22 has already provided a modified version of the Linux kernel for the TF300T.  This
can be downloaded from `https://bitbucket.org/cb22/tf300tg-kernel-source`.  Use git to
clone this to a directory.


