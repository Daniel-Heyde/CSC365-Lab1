import Student

class StudentDicts:
    by_st_last_name = {}
    by_t_last_name = {}
    by_bus = {}
    by_grade = {}

    def __init__(self, filename):
        students = self.read_data_from_file(filename)
        self.create_dictionaries(students)

    # create dictionaries from list of student objects
    def create_dictionaries(self, studentList):
        for student in studentList:
            self.add_to_dict(student, self.by_st_last_name, student.stLastName)
            self.add_to_dict(student, self.by_t_last_name, student.tLastName)
            self.add_to_dict(student, self.by_bus, student.bus)
            self.add_to_dict(student, self.by_grade, student.grade)

    def add_to_dict(self, student, dict, key):
        if key in dict:
            dict[key].append(student)
        else:
            dict[key] = [student]

    # read data file line by line
    def read_data_from_file(self, filename):
        file = open(filename, "r")
        studentList = []
        for line in file:
            studentList.append(Student.Student(line.strip()))
        return studentList

