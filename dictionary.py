# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUTdef dictionary(dictlist):
def dictionary(dictlist,dictlist2):
    print dictlist
    
    dictMap = dict(s.split(' ') for s in dictlist)

    keys = dictMap.keys()
    for k, v in dictMap.iteritems():
        
        for lst in dictlist2:
            
            if lst in keys:
                print "{}={}".format(k,v)
            else:
                print "Not found"
  

dict_ = int(raw_input())
# dictMap = {}
dictlist = []
dictlist2 = []
for i in range(0, dict_):
    string = raw_input()
    dictlist.append(string)
for z in range(0, dict_):
    string2 = raw_input()
    dictlist2.append(string2)
    
dictionary(dictlist,dictlist2)