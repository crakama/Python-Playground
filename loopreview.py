"""
Task 
Given a S string, , of length  N that is indexed from 0 to N-1 , 
print its even-indexed and odd-indexed characters as  2 space-separated 
strings on a single line (see the Sample below for more detail).
Note:  0 is considered to be an even index
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
class OddEvenIndex:
    def oddevenIndexed(self,newString):
        even = []
        odd = []
        for i in newString:
            even = []
            odd = []
            for j in i:
  
                ind = i.index(j)
                if ind % 2 == 0:
                          
                    even.append(j)
                    neweven = "".join(even)
                    #print even
                else:
                    
                    odd.append(j)
                    newodd = "".join(odd)
                    
            print "{} {}".format(neweven,newodd)
    
testcasenum = int(raw_input())
newString = []

for i in range(0,testcasenum):
    string = raw_input()
    lenString = len(string)
    newString.append(string)
oddeven = OddEvenIndex()
oddeven.oddevenIndexed(newString)