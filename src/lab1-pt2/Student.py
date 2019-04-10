import sys

class Student:
    """class for student object"""

    def __init__(self, line):
        # parse given file line into student object
        studentInfo = line.split(",")
        if len(studentInfo) != 6:
            sys.exit("Error: Invalid file format")
        self.line = line
        self.stLastName = studentInfo[0]
        self.stFirstName = studentInfo[1]
        self.grade = studentInfo[2]
        self.classroom = studentInfo[3]
        self.bus = studentInfo[4]
        self.gpa = float(studentInfo[5])

    def __repr__(self):
        return "("+self.line+")"