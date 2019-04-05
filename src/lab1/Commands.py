import StudentDicts

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
                print("Bus Route:" + student.bus)
            else:
                print("Grade: " + student.grade)
                print("Classroom Assignment: " + student.classroom)
                print("Teacher Last Name: " + student.tLastName)
                print("Teacher First Name: " + student.tFirstName)
            print("\n")
        print("\n")

    def searchTeacher(self, lastname, data):
        # method for searching given a teacher lastname
        if not (lastname in data):
            return
        studentList = data[lastname]
        for student in studentList:
            print("Student Last Name: " + student.stLastName)
            print("Student First Name: " + student.stFirstName)
            print("\n")
        print("\n")

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
            print("\n")
        print("\n")

    def searchGrade(self, grade, high, low, data):
        # method for searching given a grade with boolean high and low options
        highestGPA = None
        lowestGPA = None

        if not (grade in data):
            return

        studentList = data[grade]
        for student in studentList:
            if high is True:
                if highestGPA is None or student.gpa > highestGPA:
                    highestGPA = student
            elif low is True:
                if lowestGPA is None or student.gpa < lowestGPA:
                    lowestGPA = student

        print("Student Last Name: " + student.stLastName)
        print("Student First Name: " + student.stFirstName)
        print("GPA: " + student.gpa)
        print("Teacher Last Name: " + student.tLastName)
        print("Teacher First Name: " + student.tFirstName)
        print("Bus: " + student.bus)
        print("\n")

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
        print("Average GPA: " + avgGPA)
        print("\n\n")

    def info(self, data):
        # method for info command
        for grade in range(0,7,1):
            count = 0
            studentList = data[grade]
            count += len(studentList)
            print("Grade: " + count)
        print("\n")

if __name__ == '__main__':
    dicts = StudentDicts.StudentDicts("students.txt")
    Commands().searchStudent("abcde", True, dicts.by_st_last_name)
    Commands().searchTeacher("FAFARD", dicts.by_t_last_name)
    Commands().searchBus("54", dicts.by_bus)
