"""
Task
Consider a database table, Emails,
which has the attributes First Name and Email ID.
Given N  rows of data simulating the Emails table,
print an alphabetically-ordered list of people whose
email address ends in @gmail

"""
import re


def regexPattern(newpattern):
    sortedpattern = sorted(newpattern)
    for i in sortedpattern:
        print i


newpattern = []
N = int(raw_input().strip())
for a in xrange(N):
    firstName, emailID = raw_input().strip().split(' ')
    firstName, emailID = [str(firstName), str(emailID)]
    pattern = re.search(r'@gmail.com', emailID)
    if pattern is not None:
        newpattern.append(firstName)
regexPattern(newpattern)
