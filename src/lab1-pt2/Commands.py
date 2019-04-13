
class Commands:
    """class implementing search commands"""

    def searchStudent(self, lastname, bus, data):
        # method for searching given a student lastname and an optional boolean bus option
        if not (lastname in data.by_st_last_name):
            return
        studentList = data.by_st_last_name[lastname]
        for student in studentList:
            print("Student Last Name: " + student.stLastName)
            print("Student First Name: " + student.stFirstName)
            if bus is True:
                print("Bus Route: " + student.bus)
            else:
                print("Grade: " + student.grade)
                print("Classroom Assignment: " + student.classroom)
                print("Teacher Last Name: " + student.teachers[0].TLastName)
                print("Teacher First Name: " + student.teachers[0].TFirstName)
            print("")
        print("")

    def searchTeacher(self, lastname, data):
        # method for searching given a teacher lastname
        if not (lastname in data.by_t_last_name):
            return
        studentList = data.by_t_last_name[lastname]
        for student in studentList:
            print("Student Last Name: " + student.stLastName)
            print("Student First Name: " + student.stFirstName)
            print("")
        print("")

    def searchBus(self, bus, data):
        if not (bus in data.by_bus):
            return
        # method for searching given a bus route number
        studentList = data.by_bus[bus]
        for student in studentList:
            print("Student Last Name: " + student.stLastName)
            print("Student First Name: " + student.stFirstName)
            print("Grade: " + student.grade)
            print("Classroom Assignment: " + student.classroom)
            print("")
        print("")

    def searchGrade(self, grade, option, data):
        # method for searching given a grade
        # option 1 = grade -> students in grade
        # option 2 = grade high -> highest gpa student in grade
        # option 3 = grade low -> lowest gpa student in grade
        # option 4 = grade teacher -> teachers in grade

        if option == 4:
            if not (grade in data.by_grade_teacher):
                return

            teacherList = data.by_grade_teacher[grade];
            for teacher in teacherList:
                print("Teacher Last Name: " + teacher.TLastName)
                print("Teacher First Name: " + teacher.TFirstName)
                print("")

        else:
            if not (grade in data.by_grade_student):
                return

            highestGPA = None
            lowestGPA = None

            studentList = data.by_grade_student[grade]
            for student in studentList:
                if option == 2:
                    if highestGPA is None or student.gpa > highestGPA.gpa:
                        highestGPA = student
                elif option == 3:
                    if lowestGPA is None or student.gpa < lowestGPA.gpa:
                        lowestGPA = student
                else:
                    print("Student Last Name: " + student.stLastName)
                    print("Student First Name: " + student.stFirstName)
                    print("")

            if option == 2 or option == 3:
                if highestGPA is not None:
                    student = highestGPA
                else:
                    student = lowestGPA
                print("Student Last Name: " + student.stLastName)
                print("Student First Name: " + student.stFirstName)
                print("GPA: " + str(student.gpa))
                print("Teacher Last Name: " + student.teachers[0].TFirstName)
                print("Teacher First Name: " + student.teachers[0].TLastName)
                print("Bus: " + student.bus)
                print("")

    def searchAverage(self, grade, data):
        # method for searchng given a grade
        sum = 0
        num_students = 0

        if not (grade in data.by_grade_student):
            return

        studentList = data.by_grade_student[grade]
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
            if key in data.by_grade_student:
                studentList = data.by_grade_student[key]
            print(key + ": " + str(len(studentList)))

        print("")

    def searchClassroom(self, classroom, option, data):
        # method for searching classrooms for students or teachers
        # option 1 = students
        # option 2 = teachers

        if option == 1:
            if not (classroom in data.by_class_num_student):
                return

            studentList = data.by_class_num_student[classroom]
            for student in studentList:
                print("Student Last Name: " + student.stLastName)
                print("Student First Name: " + student.stFirstName)
                print("")
            print("")

        else:
            if not (classroom in data.by_class_num_teacher):
                return

            teacherList = data.by_class_num_teacher[classroom]
            for teacher in teacherList:
                print("Teacher Last Name: " + teacher.TLastName)
                print("Teacher First Name: " + teacher.TFirstName)
                print("")
            print("")

    def enrollment(self, data):
        # method that gives enrollment numbers in all classes
        classList = sorted(list(data.by_class_num_student.keys()))
        for classroom in classList:
            count = 0
            studentList = data.by_class_num_student[classroom]
            for student in studentList:
                count += 1
            print("Classroom: " + str(classroom))
            print("Enrollment: " + str(count))
            print("")
        print("")

    def dataAnalyze(self, option, data):
        # method that gives data corresponding to factors that may affect GPA
        # option 1 = grade level
        # option 2 = teacher
        # option 3 = bus route

        if option == 1:
            grades = sorted(list(data.by_grade_student.keys()))
            for grade in grades:
                averageGPA = 0
                num_students = 0
                print("GPA's in Grade: " + grade)
                studentList = data.by_grade_student[grade]
                for student in studentList:
                    averageGPA += student.gpa
                    num_students += 1
                    print(student.gpa)
                print("Average GPA in Grade " + str(grade) + " = " + str(averageGPA/num_students))
                print("")

        elif option == 2:
            teachers = sorted(list(data.by_t_last_name.keys()))
            for teacher in teachers:
                averageGPA = 0
                num_students = 0
                print("GPA's in Teacher: " + teacher)
                studentList = data.by_t_last_name[teacher]
                for student in studentList:
                    averageGPA += student.gpa
                    num_students += 1
                    print(str(student.gpa))
                print("Average GPA in Teacher " + teacher + " = " + str(averageGPA / num_students))
                print("")

        elif option ==3:
            buses = sorted(list(data.by_bus.keys()))
            for bus in buses:
                averageGPA = 0
                num_students = 0
                print("GPA's in Bus: " + str(bus))
                studentList = data.by_bus[bus]
                for student in studentList:
                    averageGPA += student.gpa
                    num_students += 1
                    print(student.gpa)
                print("Average GPA in Bus " + str(bus) + " = " + str(averageGPA / num_students))
                print("")
