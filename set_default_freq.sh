#!/usr/bin/env bash
# set all necessary permissions
sudo chmod 666 /sys/devices/system/cpu/cpufreq/policy*/scaling_governor
echo ondemand > /sys/devices/system/cpu/cpufreq/policy0/scaling_governor
echo ondemand > /sys/devices/system/cpu/cpufreq/policy4/scaling_governor

sudo chmod 666 /sys/devices/platform/11800000.mali/devfreq/devfreq0/governor
echo performance > /sys/devices/platform/11800000.mali/devfreq/devfreq0/governor