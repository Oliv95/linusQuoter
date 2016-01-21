#!/usr/bin/python3

import random

lines = open("quotes").readlines()
line  = random.choice(lines)[:-1:]
print "we are the knights who say ni!"

