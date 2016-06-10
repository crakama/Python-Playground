
import sys


"""
    Given ana array, a of n containing distinct elements, 
    sort array a ascending order using the Bubble Sort algorithmn
    then print the nubber of swaps, first element and last element of the new swaped list
"""
def bubbleSort(list_):
    swap = True
    listlen = len(list_) - 1
    swapcount = 0
    while listlen > 0 and swap: 
        
        swap = False
        for pass_ in range(listlen):
            
            if list_[pass_] > list_[pass_ + 1]:
                swap = True
                swapcount = swapcount + 1
                temp = list_[pass_]
                list_[pass_] = list_[pass_ + 1]
                list_[pass_ + 1] = temp
        listlen = listlen - 1
    print "Array is sorted in {} swaps.".format(swapcount)
    print "First Element: {}".format(list_[0])
    print "Last Element: {}".format(list_[len(list_) -1])

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
bubbleSort(a)
