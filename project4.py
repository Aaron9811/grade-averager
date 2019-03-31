import studentClass

def writeFile(num, avg, high, low, students):
    outputFile = open("summary.txt", "w")
    outputFile.write("Number of students:\t" + str(num) + "\n")
    outputFile.write("Average grade:\t" + str(avg) + "\n")
    outputFile.write("Highest grade:\t" + str(high) + "\n")
    outputFile.write("Lowest grade:\t" + str(low) + "\n")

    longest_name = ""
    longest_name_length = 0
    for i in range(len(students)):
        if len(students[i].fName) + len(students[i].lName) > longest_name_length:
            longest_name = students[i].fName + " " + students[i].lName
            longest_name_length = len(students[i].fName) + len(students[i].lName)
    outputFile.write("Student with longest name: " + longest_name)
    
def main():
    inputFile = open("grades.txt", "r")
    numStudents = int(inputFile.readline())
    studentList = []
    gradeTotal = 0
    gradeAvg = 0
    gradeCounter = 0
    highest_grade = 0
    lowest_grade = float("inf")

    for i in range(numStudents):
        grades = []
        fName = inputFile.readline()
        line = int(inputFile.readline())
        while line != 0:
            grades.append(line)
            gradeTotal += line
            gradeCounter += 1
            if line < lowest_grade:
                lowest_grade = line
            if line > highest_grade:
                highest_grade = line
            line = int(inputFile.readline())
        studentList.append(studentClass.Student(fName,grades))
    inputFile.close()

    for i in range(len(studentList)):
        print(studentList[i])

    gradeAvg = gradeTotal/gradeCounter

    writeFile(numStudents, gradeAvg, highest_grade, lowest_grade, studentList)

main()