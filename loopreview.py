"""
    Task given a S string, , of length  N that is indexed from 0 to N-1 ,
    print its even-indexed and odd-indexed characters as  2 space-separated
    strings on a single line (see the Sample below for more detail).
    Note:  0 is considered to be an even index
"""



# Enter your code here. Read input from STDIN. Print output to STDOUT
class OddEvenIndex:
    def oddevenIndexed(self,newString):

        for i in newString:

            for j in i:
                even = i[::2]
                odd = i[1::2]

                print "{} {}".format(even,odd)

testcasenum = int(raw_input())
newString = []

for i in range(0,testcasenum):
    string = raw_input()

    newString.append(string)
oddeven = OddEvenIndex()
oddeven.oddevenIndexed(newString)
