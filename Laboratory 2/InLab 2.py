class Student(object):                  #create a student class
    def __init__(self, name, number):   #initialize the students name and number
        self.name = name
        self.scores = []                #gets the list of scores
        for count in range(number):
            self.scores.append(0)

    def getName(self):                  #function to get the name
        return self.name

    def setScore(self, i, score):       #function to set the score of the student
        self.scores[i - 1] = score

    def getScore(self, i):              #function to get the score
        return self.scores[i - 1]

    def getAverage(self):               #function to get the average of the score
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):             #function to get the highest score
        return max(self.scores)

    def __str__(self):
        return "Name: " + self.name + "\nScores: " + \
               " ".join(map(str, self.scores))


s = Student("James", 5)

print(s.getName())
s.setScore(1, 10)
s.setScore(2, 50)
print(s.getScore(1))
print(s.getAverage())
print(s.getHighScore())
