'''
    Daniel Heyde
    Flo Costa
    Steven Sun
'''

import sys

class Teacher:
    """class for teacher object"""

    def __init__(self, line):
        # parse given file line into teacher object
        teacherInfo = line.split(", ")
        if len(teacherInfo) != 3:
            sys.exit("Error: Invalid teacher file format")
        self.line = line
        self.TLastName = teacherInfo[0]
        self.TFirstName = teacherInfo[1]
        self.classroom = teacherInfo[2]

    def __repr__(self):
        return "("+self.line+")"
