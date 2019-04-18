#!/usr/bin/env bash
# set all necessary permissions
sudo chmod 666 /sys/devices/platform/11800000.mali/devfreq/devfreq0/governor
echo userspace > /sys/devices/platform/11800000.mali/devfreq/devfreq0/governor
sudo chmod 666 /sys/devices/platform/11800000.mali/devfreq/devfreq0/userspace/set_freq
echo $1 > /sys/devices/platform/11800000.mali/devfreq/devfreq0/userspace/set_freq
