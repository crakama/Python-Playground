# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division 
import sys

"""
Read in two integers,  and , and print three lines. 
The first line is the integer division  
(While using Python2 remember to import division from __future__). 
The second line is the result of the modulo operator: . 
The third line prints the divmod of  and .

"""
def divMode(x , y):
    print x//y
    print x%y
    print divmod(x, y)

a = int(raw_input())
b = int(raw_input())
divMode(a, b)




    