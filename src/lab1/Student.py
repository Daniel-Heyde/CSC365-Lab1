
class Student:
    """class for student object"""

    def __init__(self, line):
        # parse given file line into student object
        studentInfo = line.split(",")
        self.stLastName = studentInfo[0]
        self.stFirstName = studentInfo[1]
        self.grade = studentInfo[2]
        self.classroom = studentInfo[3]
        self.bus = studentInfo[4]
        self.gpa = studentInfo[5]
        self.tLastName = studentInfo[6]
        self.tFirstName = studentInfo[7]
