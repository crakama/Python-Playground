"""
Complete the Difference class by writing the following:

A class constructor that takes an array of integers as a parameter and saves it to the  instance variable.
A computeDifference method that finds the maximum absolute difference between any  numbers in  and stores it in the  instance variable


"""

class Difference:
    def __init__(self, a):
        self.__elements = a


def computeDifference(a):
    maxnumber = max(a)
    minnumber = min(a)
    maxDifference = maxnumber - minnumber
    print maxDifference

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference
