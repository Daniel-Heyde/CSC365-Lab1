import Student
import sys

class StudentDicts:
    # st last, t last, bus, grade
    ''' need:
        * get student by student last
        * get student teacher last
        * get student by bus num
        * get student by grade
        * get students by class num
        * get teachers by class num
        * get teachers by grade
    '''
    # old
    by_st_last_name = {} # val: student
    by_t_last_name = {} # val: list of students
    by_bus = {} # val: list of students
    by_grade = {} # val: list of students
    # new
    by_class_num_student = {} # val: list of students
    by_class_num_teacher = {} # val: list of teachers

    def __init__(self, filename):
        students = self.read_data_from_file(filename)
        self.create_dictionaries(students)

    # create dictionaries from list of student objects
    def create_dictionaries(self, studentList):
        for student in studentList:
            self.add_to_dict(student, self.by_st_last_name, student.stLastName)
            self.add_to_dict(student, self.by_t_last_name, student.tLastName)
            self.add_to_dict(student, self.by_bus, student.bus)
            self.add_to_dict(student, self.by_grade_student, student.grade)

    def add_to_dict(self, student, dict, key):
        if key in dict:
            dict[key].append(student)
        else:
            dict[key] = [student]

    # read data file line by line
    def read_data_from_file(self, filename):
        try:
            file = open(filename, "r")
        except IOError:
            print("Error: File does not appear to exist.")
            sys.exit()

        studentList = []
        for line in file:
            studentList.append(Student.Student(line.strip()))
        return studentList

