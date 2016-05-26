class Person:

    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print "Name:", self.lastName + ",", self.firstName
        print "ID:", self.idNumber

class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        avg = sum(self.scores)/numScores
        if avg <= 100 and avg >= 90:
            return "O"
        elif avg < 90 and avg >= 80:
            return "E"
        elif avg < 80 and avg >= 70:
            return "A"
        elif avg < 70 and avg >= 55:
            return "P"
        elif avg < 55 and avg >= 40:
            return "D"
        elif avg < 40:
            return "T"
        else:
            pass

line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input())
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()

