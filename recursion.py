"""
   Task
   Write a factorial function that takes a positive integer,
   as a parameter and prints the result of (factorial)
"""


def factorial(num):
    count = 1
    while num > 0:

        count = count * num
        num = num - 1
    return count
"""METHOD 2"""

def factorial(num):

    if num <= 0:
        return 1
    else:
        return num * factorial(num - 1)

num = 4
factorial(num)
