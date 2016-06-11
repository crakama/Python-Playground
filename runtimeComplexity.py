# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import math


def primeNumber(n):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True


num = int(raw_input())
list_ = []
for i in range(0, num):
    list_.append(raw_input())
primeNumber(list_)


for j in list_:
    if j == 1:
        print "Not prime"
    elif primeNumber(j):
        print("Prime")
    else:
        print("Not prime")
