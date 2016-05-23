# Enter your code here. Read input from STDIN. Print output to STDOUT
class OddEvenIndex:
    def oddevenIndexed(self,newString):
        even = []
        odd = []
        for i in newString:
            even = []
            odd = []
            for j in range(0, len(i)-1):
                if j in i:
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