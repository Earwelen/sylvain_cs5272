#!/usr/bin/env bash
# set all necessary permissions
# 177000000 266000000 350000000 420000000 480000000 543000000 600000000

sudo chmod 666 /sys/devices/platform/11800000.mali/devfreq/devfreq0/governor
echo userspace > /sys/devices/platform/11800000.mali/devfreq/devfreq0/governor
sudo chmod 666 /sys/devices/platform/11800000.mali/devfreq/devfreq0/userspace/set_freq
echo $1 > /sys/devices/platform/11800000.mali/devfreq/devfreq0/userspace/set_freq
