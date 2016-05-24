# Enter your code here. Read input from STDIN. Print output to STDOUT
def dictionary(dictlist, dictlist2):

    dictMap = dict(s.split(' ') for s in dictlist)
    keys = dictMap.keys()
    
    for x in dictlist2:
        if x in keys:
            print "{}={}".format(x,dictMap[x] )
        else:
            print "Not found"

dict_ = int(raw_input())
dictlist = []
dictlist2 = []
for i in range(0, dict_):
    string = raw_input()
    dictlist.append(string)
for z in range(0, dict_):
    string2 = raw_input()
    dictlist2.append(string2)

dictionary(dictlist,dictlist2)