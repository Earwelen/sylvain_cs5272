#!/usr/bin/env python3
# CS5272 Embedded Software Design
# Sylvain Riondet A0178584L
# General file to change frequencies

# imports
import configparser

paths_freq = configparser.ConfigParser()
paths_freq.read("sylvain_cs5272/paths_freq.ini")


def freq_current(choice, raw=True):
    with open(paths_freq[choice]["cur"]) as f:
        cur_freq = f.read()
        cur_freq_formatted = f"{int(cur_freq)/1000:.0f}" if cur_freq.isdigit() else cur_freq
    return cur_freq if raw else cur_freq_formatted


def freq_write(choice, value):
    with open(paths_freq[choice]["set"], "w") as f:
        f.write(value)


def freq_available(choice):
    print(paths_freq[choice]["available"])
    with open(paths_freq[choice]["available"]) as f:
        return f.read().split()

