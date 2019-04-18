# set all necessary permissions
sudo chmod 666 /sys/devices/system/cpu/cpufreq/policy*/scaling_governor
sudo chmod 666 /sys/devices/system/cpu/cpufreq/policy*/scaling_setspeed
sudo chmod 666 /sys/devices/platform/11800000.mali/devfreq/devfreq0/governor
sudo chmod 666 /sys/devices/platform/11800000.mali/devfreq/devfreq0/userspace/set_freq