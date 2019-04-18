#!/usr/bin/env python3
# CS5272 Embedded Software Design
# Sylvain Riondet A0178584L
# Main script, choose task 1, 2, 3, or 4 (advanced)

# imports
import argparse
from sylvain_cs5272.dvfs import processors

from sylvain_cs5272 import task1_run_freq

if __name__ == '__main__':
    # Arguments for inline commands
    cmd = argparse.ArgumentParser("Main script for CS5272, by Sylvain Riondet. relaunch with -h for help. \n"
                                  "Tasks can run independently, for example sylvain_cs5272/task1_run_freq.py \n")
    cmd.add_argument("task", help="Choose task number. You can write '1a15 for task 1, test for a15'", type=str,
                     default="1")  # , choices=("1", "2", "3", "4"))
    args = cmd.parse_args()
    task = args.task

    print("Launching task " + task, flush=True)
    if task[0] == "1":
        if task[1:] in processors:
            task1_run_freq.main(task[1:], 5)
        else:
            task1_run_freq.main("a7", 5)



