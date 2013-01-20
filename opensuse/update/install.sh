#!/sbin/sh
mount -t ext4 /dev/block/mmcblk0p8 /data

mkdir -p /data/opensuse
xzcat /tmp/rootfs.tar.xz | tar -xvp -C /data/opensuse -f -

sync

