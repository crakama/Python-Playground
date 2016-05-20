"""
Given an array, A , of N integers, print A's elements in reverse order as a single line of space-separated numbers.

Input Format
The first line contains an integer, N (the size of our array). 
The second line contains N space-separated integers describing array A's elements.

"""


#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
arraynew = arr[::-1]

for i in arraynew:
    print i,