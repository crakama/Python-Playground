# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import math



def primeNumber(n):
    n = float(n)
    
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

num = int(raw_input())
list_ = []
for i in range(0, num):
    list_.append(raw_input())
    
for j in list_:
    if j==1:
        print "Not prime"
    elif primeNumber(j):
        print("Prime")
    else:
        print("Not prime")
 