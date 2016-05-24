n = "01010101110000100"
#!/bin/python
import sys
n = int(raw_input())
binary = str(bin(n)).strip("0b")
print binary

def BinaryCount(binary):
    maxCount = 0
    currentCount = 0
    for i in binary:
        if i == "1":
            currentCount = currentCount + 1
        if i == "0":
            if maxCount < currentCount:
                print maxCount
                maxCount = currentCount
            currentCount = 0
    print maxCount
BinaryCount(binary)
