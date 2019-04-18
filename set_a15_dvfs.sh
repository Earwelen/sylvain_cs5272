#!/usr/bin/env bash
# set all necessary permissions
sudo chmod 666 /sys/devices/system/cpu/cpufreq/policy4/scaling_governor
echo userspace > /sys/devices/system/cpu/cpufreq/policy4/scaling_governor

sudo chmod 666 /sys/devices/system/cpu/cpufreq/policy4/scaling_setspeed
echo $1 > /sys/devices/system/cpu/cpufreq/policy4/scaling_setspeed

