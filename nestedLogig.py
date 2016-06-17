"""
Task
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine(if any). The fee structure is as follows:
If the book is returned on or before the expected return date, no fine will be charged(i.e.: fine=0.
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine=15 * days late.
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine=500 * monthslate .
If the book is returned after the calendar year in which it was expected, there is a fixed fine of .


"""


def Library(returndate, expecteddate):

        if returndate[2] > expecteddate[2]:
            fine = 10000
            print fine
        elif returndate[0] > expecteddate[0] and returndate[1] == expecteddate[1] and returndate[2] == expecteddate[2]:

            dayslate = returndate[0] - expecteddate[0]
            fine = 15 * dayslate
            print fine

        elif returndate[1] > expecteddate[1] and returndate[2] == expecteddate[2]:
            monthslate = returndate[1] - expecteddate[1]
            fine = 500 * monthslate
            print fine

        else:
            print 0
returnDate = map(int, raw_input().split(" "))
expectedReturn = map(int, raw_input().split(" "))
Library(returnDate, expectedReturn)