import sys
"""
    To solve this challenge, we must first take each character in , 
    enqueue it in a queue, and also push that same character onto a stack.
    Once that's done, we must dequeue the first character from the queue and pop the top character off the stack, 
    then compare the two characters to see if they are the same; as long as the characters match, 
    we continue dequeueing, popping, and comparing each character 
    until our containers are empty (a non-match means  isn't a palindrome).

"""

from collections import deque
class Solution:
    # Write your code here
    def __init__(self):
        self.stack_ = []
        self.enqueue_ = deque([])
        
    def pushCharacter(self, i):
        return self.stack_.append(i)
        
    def enqueueCharacter(self, j):
        return self.enqueue_.append(j)
        
    
    def popCharacter(self):
        return self.stack_.pop()
        
    def dequeueCharacter(self):
    	''' popleft pops elements starting from the left'''
        return self.enqueue_.popleft()



# read the string s
s=raw_input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l / 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    sys.stdout.write ("The word, "+s+", is a palindrome.")
else:
    sys.stdout.write ("The word, "+s+", is not a palindrome.")    