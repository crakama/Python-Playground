"""
Write a function:

def solution(N)
that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5.

Assume that:

N is an integer within the range [1..2,147,483,647].
Complexity:

expected worst-case time complexity is O(log(N));
expected worst-case space complexity is O(1).

"""



# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N):
    Nbinary = str(bin(N)).strip("0b")
    binarylen = len(Nbinary)
    binarygap = 0
    binarycount = 0
    for element in range(binarylen):
        if Nbinary[element] == "0":
            binarygap = binarygap + 1

        if Nbinary[element] == "1":
            if binarycount < binarygap:
                binarycount = binarygap
            binarygap = 0
    return binarycount
