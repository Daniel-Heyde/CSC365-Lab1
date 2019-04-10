
class Commands:
    """class implementing search commands"""

    def searchStudent(self, lastname, bus, data):
        # method for searching given a student lastname and an optional boolean bus option
        if not (lastname in data):
            return
        studentList = data[lastname]
        for student in studentList:
            print("Student Last Name: " + student.stLastName)
            print("Student First Name: " + student.stFirstName)
            if bus is True:
                print("Bus Route: " + student.bus)
            else:
                print("Grade: " + student.grade)
                print("Classroom Assignment: " + student.classroom)
                print("Teacher Last Name: " + student.tLastName)
                print("Teacher First Name: " + student.tFirstName)
            print("")
        print("")

    def searchTeacher(self, lastname, data):
        # method for searching given a teacher lastname
        if not (lastname in data):
            return
        studentList = data[lastname]
        for student in studentList:
            print("Student Last Name: " + student.stLastName)
            print("Student First Name: " + student.stFirstName)
            print("")
        print("")

    def searchBus(self, bus, data):
        if not (bus in data):
            return
        # method for searching given a bus route number
        studentList = data[bus]
        for student in studentList:
            print("Student Last Name: " + student.stLastName)
            print("Student First Name: " + student.stFirstName)
            print("Grade: " + student.grade)
            print("Classroom Assignment: " + student.classroom)
            print("")
        print("")

    def searchGrade(self, grade, high, low, data):
        # method for searching given a grade with boolean high and low options
        highestGPA = None
        lowestGPA = None

        if not (grade in data):
            return

        studentList = data[grade]
        for student in studentList:
            if high:
                if highestGPA is None or student.gpa > highestGPA.gpa:
                    highestGPA = student
            elif low:
                if lowestGPA is None or student.gpa < lowestGPA.gpa:
                    lowestGPA = student
            else:
                print("Student Last Name: " + student.stLastName)
                print("Student First Name: " + student.stFirstName)
                print("")

        if low or high:
            if highestGPA is not None:
                student = highestGPA
            else:
                student = lowestGPA
            print("Student Last Name: " + student.stLastName)
            print("Student First Name: " + student.stFirstName)
            print("GPA: " + str(student.gpa))
            print("Teacher Last Name: " + student.tLastName)
            print("Teacher First Name: " + student.tFirstName)
            print("Bus: " + student.bus)
            print("")

    def searchAverage(self, grade, data):
        # method for searchng given a grade
        sum = 0
        num_students = 0

        if not (grade in data):
            return

        studentList = data[grade]
        for student in studentList:
            sum += student.gpa
            num_students += 1

        avgGPA = sum / num_students

        print("Grade: " + grade)
        print("Average GPA: " + str(avgGPA))
        print("")

    def info(self, data):
        # method for info command

        for grade in range(0,7,1):
            key = str(grade)
            studentList = []
            if key in data:
                studentList = data[key]
            print(key + ": " + str(len(studentList)))

        print("")

    def searchClassroom(self, classroom, option, data):
        # search

    def enrollment(self, data):
        # search

    def dataAnalyze(self, option, data):
        # search