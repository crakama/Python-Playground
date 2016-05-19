#!/bin/python
"""
Task 
Given an integer, N, print its first 10 multiples. 
Each multiple N * i (where  1 <= i <= 10) 
should be printed on a new line in the form: N * i = result .

"""
import sys


N = int(raw_input().strip())
multlist = [1,2,3,4,5,6,7,8,9,10]

def loops(n, multlist):
    for i in multlist:
        if n > 0:
            mult = n * i
        print "{} x {} = {}".format(n,i,mult)
             
loops(N,multlist)