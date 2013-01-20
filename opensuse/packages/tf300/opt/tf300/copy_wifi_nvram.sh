#!/bin/sh
if [ -e "/lib/firmware/brcm/brcmfmac-sdio.txt" ]; then
	exit 0
fi

mount -o ro /dev/mmcblk0p1 /mnt
mkdir -p /lib/firmware/brcm
cp /mnt/etc/nvram_*.txt /lib/firmware/brcm/brcmfmac-sdio.txt
umount /mnt

rmmod cardhu_wifi
modprobe cardhu_wifi
rmmod brcmfmac
modprobe brcmfmac
