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

Additional Packages
--------------------------

You will need to install the following packages when inside the chroot:

  * NetworkManager
  * NetworkManager-kde4-libs
  * wget

Cooking Additional Packages
------------------------------

There are TF300T-specific packages that need to be built.  You can build them by using
the `cook` command, like so:

```
sudo ./cook
```

You will need rpmbuild installed for this to work.  After the packages have been built they
will be residing in the `build` directory.  Copy them to the `disk` folder and use `edisk`
to chroot in.  Then `zypper in <path to RPM>` for each of the RPMs built to install them.
Usually it's fine if there are missing dependencies; this just happens to be RPMBUILD not
doing a very good job of detecting what's available (they're all just binary copies anyway).

Rebuild OS
--------------

Remember that once you have done the above, you need to re-run the `buildos` command to
produce the new `rootfs.tar.xz` and `update.zip` files.

**If all goes according to plan, you should now have an `update.zip` file in the `build` folder.**

Continue onto [deployment](deploy.md)...
