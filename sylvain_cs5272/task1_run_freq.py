#!/usr/bin/env python3
# CS5272 Embedded Software Design
# Sylvain Riondet A0178584L
# Project Task 1
# Just running either core A7, A15 or GPU, at all available frequencies, with the run.sh from the provided resources

# imports
import argparse
from time import sleep as t_sleep

from sylvain_cs5272.dvfs import freq_current, freq_write, freq_available, freq_mhz, processors


def main(choice, delay):
    """" Loop through all available frequencies for the given processing unit """

    frequencies = freq_available(choice)
    print(frequencies, flush=True)
    
    print(f"Current frequency is : {freq_mhz(choice, freq_current(choice))} Mhz", flush=True)
        
    for freq in frequencies:
        freq_write(choice, freq)
        counter = 0
        while freq_current(choice) != freq:
            t_sleep(0.001)
            counter += 1
            if counter > 1000:
                print(f"Frequency doesn't want to change, still at {freq_mhz(choice, freq_current(choice))} Mhz, "
                      f"giving up", flush=True)
                break
        
        print(f"Current frequency is {freq_mhz(choice, freq_current(choice))} Mhz (waited {counter}ms). "
              f"Waiting {delay} sec to check the power consumption.", flush=True)
        t_sleep(delay)

    t_sleep(delay*3)
    print("Tests are done, putting back to low power")
    freq_write(choice, frequencies[0])
    print(f"Current frequency is {freq_mhz(choice, freq_current(choice))} Mhz (waited {counter}ms). "
          f"Waiting {delay} sec to check the power consumption.", flush=True)


if __name__ == '__main__':
    # Arguments for inline commands
    cmd = argparse.ArgumentParser("Run the run.sh with various setup of cPU and GPU frequencies")
    cmd.add_argument("choice", help="Choose between a7, a15 or gpu", type=str,
                     default="A7", choices=("a7", "a15", "gpu", "all"))
    cmd.add_argument("-d", "--delay", help="time for each frequency setup", 
                     type=int, default="5")
    args = cmd.parse_args()
    
    print("Launching task 1", flush=True)
    if args.choice == "all":
        for processor in processors:
            main(processor, args.delay)
    else:
        main(args.choice, args.delay)

