#!/usr/bin/env python3
# CS5272 Embedded Software Design
# Sylvain Riondet A0178584L
# Project Task 2
# Operating Modes

# TODO: schedutil
#  http://heim.ifi.uio.no/~knuto/kernel/4.14/admin-guide/pm/cpufreq.html
#  schedutil: need to learn how to use the scaling governor
#  if task loaded by "CFS" then "Per-Entity Load Tracking (PELT)" allows for automatic CPU scaling

# TODO multiple policies for more flexibility in cores
#  can create new custom "policyXXX" to control any core !

# todo on/off camera and use "input i" in the object_detection.cpp to save power
# todo turn off all unused peripherals
# todo change camera FPS ?

# Create other files for each mode
import argparse


def main(mode):
    if mode == "save":
        return
    else:
        return


if __name__ == '__main__':
    # Arguments for inline commands
    cmd = argparse.ArgumentParser("Use various power modes")
    cmd.add_argument("mode", help="Choose between save, normal, or performance", type=str,
                     default="normal", choices=("save", "normal", "perf"))
    args = cmd.parse_args()

    print("Launching main", flush=True)
    main(args.mode)

