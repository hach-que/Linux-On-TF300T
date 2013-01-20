<!-- vim: set syntax=markdown: -->

Preparing OpenSUSE
=================================

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

You should end up with a `kernel.blob` file in the `opensuse/build` folder.  This is the kernel
and initrd that will be flashed to the device.

Continue onto [building OpenSUSE](build.md)...

