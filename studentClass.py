class Student:

    def __init__(self, name, grades):
        self.name = name.split(" ")
        self.fName = self.name[0]
        self.lName = self.name[1]
        self.lName = self.lName.strip("\n")
        self.grades = sorted(grades, key=int)
        self.total = 0
        for i in range(len(grades)):
            self.total += grades[i]
        self.avg = self.total/len(self.grades)
        if self.avg < 60:
            self.letter = "F"
        elif (self.avg >= 60 and self.avg < 70):
            self.letter = "D"
        elif (self.avg >= 70 and self.avg <80):
            self.letter = "C"
        elif (self.avg >= 80 and self.avg < 90):
            self.letter = "B"
        elif (self.avg >= 90):
            self.letter = "A"
        else:
            self.letter = "ERROR"

    def __str__(self):
        stringbuilder = ""
        stringbuilder += (self.fName + " " + self.lName)
        for i in range(len(self.grades)):
            stringbuilder += (" " + str(self.grades[i]))
            if i == len(self.grades)-1:
                stringbuilder += (" -- " + self.letter)
            else:
                stringbuilder += (", ")
        return stringbuilder

    def get_average(self):
        return self.avg

    def get_letter(self):
        return self.letter