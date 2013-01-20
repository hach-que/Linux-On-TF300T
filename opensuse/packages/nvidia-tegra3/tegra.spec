# This is the spec file for nvidia-tegra3 package.
Name:           nvidia-tegra3
Version:        1.0
Release:        1%{?dist}
Summary:        Provides NVIDIA Tegra 3 display drivers for TF300T on OpenSUSE.
Source0:        nvidia-tegra3.tar.gz

License:        Proprietary
URL:            http://github.com/hach-que/Linux-On-TF300T

%description
This package provides the display drivers for NVIDIA Tegra 3 under OpenSUSE.

%install
mkdir %{buildroot} || true
tar -xf %_sourcedir/nvidia-tegra3.tar.gz -C %{buildroot}

%files
/etc/X11/xorg.conf.d/10-tegra.conf
/etc/nv_tegra_release
/usr/bin/nvgstcapture
/usr/bin/nvgstplayer
/usr/lib/firmware/nvavp_os_0ff00000.bin
/usr/lib/firmware/nvavp_os_eff00000.bin
/usr/lib/firmware/nvavp_vid_ucode_alt.bin
/usr/lib/firmware/nvmm_aacdec.axf
/usr/lib/firmware/nvmm_adtsdec.axf
/usr/lib/firmware/nvmm_h264dec.axf
/usr/lib/firmware/nvmm_h264dec2x.axf
/usr/lib/firmware/nvmm_jpegdec.axf
/usr/lib/firmware/nvmm_jpegenc.axf
/usr/lib/firmware/nvmm_manager.axf
/usr/lib/firmware/nvmm_mp3dec.axf
/usr/lib/firmware/nvmm_mpeg4dec.axf
/usr/lib/firmware/nvmm_service.axf
/usr/lib/firmware/nvrm_avp_0ff00000.bin
/usr/lib/firmware/nvrm_avp_8e000000.bin
/usr/lib/firmware/nvrm_avp_9e000000.bin
/usr/lib/firmware/nvrm_avp_be000000.bin
/usr/lib/firmware/nvrm_avp_eff00000.bin
/usr/lib/gstreamer-0.10/libgstnvxvimagesink.so
/usr/lib/gstreamer-0.10/libgstomx.so
/usr/lib/libEGL.so.1
/usr/lib/libGLESv1_CM.so.1
/usr/lib/libGLESv2.so.2
/usr/lib/libKD.so
/usr/lib/libardrv_dynamic.so
/usr/lib/libcgdrv.so
/usr/lib/libnvapputil.so
/usr/lib/libnvavp.so
/usr/lib/libnvcwm.so
/usr/lib/libnvdc.so
/usr/lib/libnvddk_2d.so
/usr/lib/libnvddk_2d_v2.so
/usr/lib/libnvddk_disp.so
/usr/lib/libnvddk_kbc.so
/usr/lib/libnvddk_mipihsi.so
/usr/lib/libnvddk_nand.so
/usr/lib/libnvddk_se.so
/usr/lib/libnvddk_snor.so
/usr/lib/libnvddk_spif.so
/usr/lib/libnvddk_usbphy.so
/usr/lib/libnvdispatch_helper.so
/usr/lib/libnvglsi.so
/usr/lib/libnvmedia_audio.so
/usr/lib/libnvmm.so
/usr/lib/libnvmm_audio.so
/usr/lib/libnvmm_camera.so
/usr/lib/libnvmm_contentpipe.so
/usr/lib/libnvmm_image.so
/usr/lib/libnvmm_manager.so
/usr/lib/libnvmm_parser.so
/usr/lib/libnvmm_service.so
/usr/lib/libnvmm_utils.so
/usr/lib/libnvmm_video.so
/usr/lib/libnvmm_writer.so
/usr/lib/libnvmmlite.so
/usr/lib/libnvmmlite_audio.so
/usr/lib/libnvmmlite_image.so
/usr/lib/libnvmmlite_utils.so
/usr/lib/libnvmmlite_video.so
/usr/lib/libnvodm_disp.so
/usr/lib/libnvodm_dtvtuner.so
/usr/lib/libnvodm_imager.so
/usr/lib/libnvodm_misc.so
/usr/lib/libnvodm_query.so
/usr/lib/libnvomx.so
/usr/lib/libnvomxilclient.so
/usr/lib/libnvos.so
/usr/lib/libnvparser.so
/usr/lib/libnvrm.so
/usr/lib/libnvrm_graphics.so
/usr/lib/libnvsm.so
/usr/lib/libnvtestio.so
/usr/lib/libnvtestresults.so
/usr/lib/libnvtvmr.so
/usr/lib/libnvwinsys.so
/usr/lib/libnvwsi.so
/usr/lib/udev/rules.d/99-tegra-devices.rules
/usr/lib/xorg/modules/drivers/tegra_drv.so
