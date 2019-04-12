import Student
import Teacher
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
    by_grade_student = {} # val: list of students
    # new
    by_class_num_student = {} # val: list of students
    by_class_num_teacher = {} # val: list of teachers
    by_grade_teacher = {} # val: list of teachers

    def __init__(self, student_file, teacher_file):
        students = self.read_students_from_file(student_file)
        teachers = self.read_teachers_from_file(teacher_file)
        self.create_dictionaries(students, teachers)

    # create dictionaries from list of student objects
    def create_dictionaries(self, student_list, teacher_list):
        for teacher in teacher_list:
            self.add_to_dict(teacher, self.by_class_num_teacher, teacher.classroom)
        for student in student_list:
            student.teachers = self.by_class_num_teacher[student.classroom]
            self.add_to_dict(student, self.by_class_num_student, student.classroom)
            self.add_to_dict(student, self.by_st_last_name, student.stLastName)
            self.add_to_dict(student, self.by_bus, student.bus)
            self.add_to_dict(student, self.by_grade_student, student.grade)
            for teacher in student.teachers:
                self.add_to_dict(student, self.by_t_last_name, teacher.TLastName)
                self.add_to_dict(teacher, self.by_grade_teacher, student.grade)

    def add_to_dict(self, value, dict, key):
        if key in dict:
            if (not value in dict[key]):
                dict[key].append(value);
        else:
            dict[key] = [value]

    # read data file line by line
    def read_students_from_file(self, filename):
        file = self.open_file(filename)

        studentList = []
        for line in file:
            studentList.append(Student.Student(line.strip()))
        return studentList

    # read data file line by line
    def read_teachers_from_file(self, filename):
        file = self.open_file(filename)
        studentList = []
        for line in file:
            studentList.append(Teacher.Teacher(line.strip()))
        return studentList

    def open_file(self, filename):
        try:
            file = open(filename, "r")
        except IOError:
            print("Error: File does not appear to exist.")
            sys.exit()
        return file


if __name__ == '__main__':
        StudentDicts("list.txt", "teachers.txt")

