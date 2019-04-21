#!/usr/bin/env bash
# set all necessary permissions
# 200000 300000 400000 500000 600000 700000 800000 900000 1000000 1100000 1200000 1300000 1400000 1500000 1600000 1700000 1800000 1900000 2000000

sudo chmod 666 /sys/devices/system/cpu/cpufreq/policy4/scaling_governor
echo userspace > /sys/devices/system/cpu/cpufreq/policy4/scaling_governor

sudo chmod 666 /sys/devices/system/cpu/cpufreq/policy4/scaling_setspeed
echo $1 > /sys/devices/system/cpu/cpufreq/policy4/scaling_setspeed

