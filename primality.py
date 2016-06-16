# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
Finding the prime number from a list using square root of n big o notation

"""


num = int(raw_input())
list_ = []
for i in range(0, num):
    list_.append(int(raw_input()))


def is_prime(number):
    if number == 2:
        return "Prime"
    if number == 3:
        return "Prime"
    if number % 2 == 0:
        return "Not prime"
    if number % 3 == 0:
        return "Not prime"

    i = 5
    w = 2
    while i * i <= number:
        if number % i == 0:
            return "Not prime"
        i = i + w
        w = 6 - w

    return "Prime"

for j in list_:

    if j == 1:
        print "Not prime"

    else:
        print is_prime(j)
