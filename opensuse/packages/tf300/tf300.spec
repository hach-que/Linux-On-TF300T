# This is the spec file for tf300 package.
Name:           tf300
Version:        1.0
Release:        1%{?dist}
Summary:        Provides supporting modules and scripts for the TF300.
Source0:        tf300.tar.gz

License:        Proprietary / Apache 2
URL:            http://github.com/hach-que/Linux-On-TF300T

%description
This package provides additional drivers (such as Wifi / 3G) and supporting
scripts for running OpenSUSE on the tf300.

%install
mkdir %{buildroot} || true
tar -xf %_sourcedir/tf300.tar.gz -C %{buildroot}

%files
/etc/modules-load.d/brcmfmac.conf
/etc/modules-load.d/cardhu_wifi.conf
/lib/firmware/brcm/brcmfmac-sdio.bin
/lib/modules/3.1.10-g74e5e9f/brcmfmac.ko
/lib/modules/3.1.10-g74e5e9f/brcmutil.ko
/lib/modules/3.1.10-g74e5e9f/cardhu_wifi.ko
/lib/modules/3.1.10-g74e5e9f/cfg80211.ko
/lib/modules/3.1.10-g74e5e9f/compat.ko
/lib/modules/3.1.10-g74e5e9f/lib80211.ko
/lib/modules/3.1.10-g74e5e9f/lib80211_crypt_ccmp.ko
/lib/modules/3.1.10-g74e5e9f/lib80211_crypt_tkip.ko
/lib/modules/3.1.10-g74e5e9f/lib80211_crypt_wep.ko
/lib/modules/3.1.10-g74e5e9f/mac80211.ko
/lib/modules/3.1.10-g74e5e9f/modules.alias
/lib/modules/3.1.10-g74e5e9f/modules.alias.bin
/lib/modules/3.1.10-g74e5e9f/modules.builtin.bin
/lib/modules/3.1.10-g74e5e9f/modules.dep
/lib/modules/3.1.10-g74e5e9f/modules.dep.bin
/lib/modules/3.1.10-g74e5e9f/modules.devname
/lib/modules/3.1.10-g74e5e9f/modules.softdep
/lib/modules/3.1.10-g74e5e9f/modules.symbols
/lib/modules/3.1.10-g74e5e9f/modules.symbols.bin
/lib/modules/3.1.10-g74e5e9f/sch_codel.ko
/lib/modules/3.1.10-g74e5e9f/sch_fq_codel.ko
/lib/systemd/system/tf300-cpu.service
/lib/systemd/system/tf300-wifi.service
/opt/tf300/copy_wifi_nvram.sh
/opt/tf300/cpu.sh
