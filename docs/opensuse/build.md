<!-- vim: set syntax=markdown: -->

Building OpenSUSE
=================================

To build the `update.zip` that we will deploy to the device, you can run the `buildos`
script in the `opensuse` directory, like so:

```
./buildos
```

The first time you run this, the script will download the OpenSUSE 12.2 ARM base image
and chroot into it, where you can configure the system before deployment.  It is recommended
that you install some graphical desktop as the framebuffer console is reported not to work.

Future calls to `buildos` will not chroot into the environment; it will just rebuild the
update.zip.  If you want to modify the disk image, you can use the `edisk` command, like so:

```
sudo ./edisk
```

This command handles setting up the environment and chrooting.  It is actually what is used
during `buildos` in the initial build.

**If all goes according to plan, you should now have an `update.zip` file in the `build` folder.

Continue onto [deployment](deployment.md)...

