<!-- vim: set syntax=markdown: -->

Creating OpenSUSE base image
=============================

Create temporary folder
--------------------------

Create a temporary folder in which to build the image.

Add ARM repository
------------------------

```
zypper -R $(pwd) -c $(pwd)/etc/zypp/zypp.conf ar http://download.opensuse.org/ports/armv7hl/distribution/12.2/repo/oss/ repo-oss
```

Reconfigure architecture
----------------------------

Copy the base file from `/etc/products.d/baseproduct` into the new area.  Modify the contents of this file
to state that the architecture and target OS are `armv7hl` instead of `x86(\_64)`.

Refresh repository
---------------------

```
zypper -R $(pwd) -c $(pwd)/etc/zypp/zypp.conf ref
```

