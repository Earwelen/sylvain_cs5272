#!/usr/bin/env python3
# CS5272 Embedded Software Design
# Sylvain Riondet A0178584L
# General file to change frequencies

# imports
import configparser
import os


paths_freq = configparser.ConfigParser()
paths_freq.read("/home/odroid/Project/sylvain_cs5272/sylvain_cs5272/paths_freq.ini")
processors = ("a7", "a15", "gpu")


def freq_current(choice):
    with open(paths_freq[choice]["cur"]) as f:
        cur_freq = f.read().split()[0]
    return cur_freq


def freq_write(choice, value):
    with open(paths_freq[choice]["set"], "w") as f:
        f.write(value)


def freq_available(choice):
    with open(paths_freq[choice]["available"]) as f:
        return f.read().split()


def freq_mhz(choice, value):
    if choice == "gpu":
        return int(value)/10**6
    else:
        return int(value)/10**3

