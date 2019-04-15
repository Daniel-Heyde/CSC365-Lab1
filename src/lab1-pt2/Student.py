'''
    Daniel Heyde
    Flo Costa
    Steven Sun
'''

import sys

class Student:
    """class for student object"""

    def __init__(self, line):
        # parse given file line into student object
        studentInfo = line.split(",")
        if len(studentInfo) != 6:
            sys.exit("Error: Invalid student file format")
        self.line = line
        self.stLastName = studentInfo[0]
        self.stFirstName = studentInfo[1]
        self.grade = studentInfo[2]
        self.classroom = studentInfo[3]
        self.bus = studentInfo[4]
        self.gpa = float(studentInfo[5])
        self.teachers = None

    def __repr__(self):
        teach_string = ""
        for teacher in self.teachers:
            teach_string += teacher.__repr__()
        return "\n\t("+self.line+", "+ teach_string + ")\n"