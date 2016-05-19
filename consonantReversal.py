
"""
    Given N strings, reverse and print each string such that the
    positions of its vowels remain unchanged but all
    its consonants are reversed

"""


N = "abcdefg"
v = "aeiuo"
# agfdecb
newString = []


def consonantReversal(N):
    for i in N:
        if i not in v:
            newString.append(i)
            revString = newString[::-1]

    for i in N:
        if i in v:
            index_i = N.index(i)
            revString.insert(index_i, i)


    return revString

consonantReversal(N)




# Enter your code here. Read input from STDIN. Print output to STDOUT
class Consonants: 
    def consonantReversal(self,N):
        newString = []
        v = "aeiuo"
        N = ['eabafgs', 'abcde']
        
        for i in N:
            for j in i:
                if j not in v:
                    newString.append(j)
                    revString = newString[::-1]
            #print revString
            
            new = []
            for j in i:
                if j in v:
                    new.append(j)
            
                    if j in new:
                        index_i = i.index(j)
                        revString.insert(index_i, j)
                    else:
                        index_i = i.index(j)
                        revString.insert(index_i, j)
                        
              
            print revString

num = int(raw_input())
stringlist = []
for s in range(0,num):
    strings = raw_input()
    stringlist.append(strings)
    con = Consonants()
    con.consonantReversal(stringlist)

