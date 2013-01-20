#!/bin/sh

# Power save mode, according to android.

echo interactive > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
echo interactive > /sys/devices/system/cpu/cpu1/cpufreq/scaling_governor
echo interactive > /sys/devices/system/cpu/cpu2/cpufreq/scaling_governor
echo interactive > /sys/devices/system/cpu/cpu3/cpufreq/scaling_governor

echo 1 > /sys/module/cpu_tegra3/parameters/auto_hotplug

echo 4 > /sys/module/cpu_tegra/parameters/system_mode
echo 1300 > /sys/kernel/tegra_cap/core_cap_level
echo 0 > /sys/kernel/tegra_cap/core_cap_state
echo 10 > /sys/module/cpu_tegra3/parameters/mp_overhead
echo 99999999 > /sys/module/cpu_tegra/parameters/pwr_cap_limit_1
echo 99999999 > /sys/module/cpu_tegra/parameters/pwr_cap_limit_2
echo 99999999 > /sys/module/cpu_tegra/parameters/pwr_cap_limit_3
echo 99999999 > /sys/module/cpu_tegra/parameters/pwr_cap_limit_4

echo "Y" > /sys/module/cpuidle/parameters/lp2_in_idle
echo 2048 > /sys/block/mmcblk0/queue/read_ahead_kb
