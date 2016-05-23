"""
Given N messages, do things:
1. Find G,the number of groups that she can form and print it on a new line.
2. Let M be the size of the largest possible group; print all groups having elements in the following
order:
The strings within each group must be in descending order, printed as a single line of spaceseparated
values.
If there are or more groups of size M , then each group must be printed in ascending order,
meaning you should print them lexicographically as if they were letters. An example of
lexicographically ordered numeric characters would be 1<11>111<2

Note: To compare two groups G1 and G2 lexicographically , compare the elements from left to right and
take the first element that doesn't match. Let the elements be e1 and e2 . Now make lexicographical
comparision between e1 and e2. If e1 is lexicographically smaller than e2 , then the group G1 is also smaller
than .
"""

def grouping(groupString):
    group = [1,2,3,4,5,6,7,8,9]
    for i in numstring:
        if numstring.count(i)== 1:
            print i,
        elif numstring.count(i) == 2:
            print i,



for i in range(0, num):
    numstring = int(raw_input())

grouping(numstring)



