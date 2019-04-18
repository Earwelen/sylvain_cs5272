#!/usr/bin/env bash
# set all necessary permissions
cat /sys/devices/system/cpu/cpufreq/policy0/scaling_cur_freq
cat /sys/devices/system/cpu/cpufreq/policy4/scaling_cur_freq
cat /sys/devices/platform/11800000.mali/devfreq/devfreq0/cur_freq
