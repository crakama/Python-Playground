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