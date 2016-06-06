#!/bin/python

import sys


S = raw_input().strip()
try:
    new_s = int(S)
    print new_s
except:
    print "Bad String"