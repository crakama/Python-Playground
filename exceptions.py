'''Read a string, , and print its integer value; if  cannot be converted to an integer, print Bad String.'''

import sys


S = raw_input().strip()
try:
    new_s = int(S)
    print new_s
except:
    print "Bad String"