import sys

class Teacher:
    """class for teacher object"""

    def __init__(self, line):
        # parse given file line into teacher object
        teacherInfo = line.split(",")
        if len(teacherInfo) != 6:
            sys.exit("Error: Invalid file format")
        self.line = line
        self.TLastName = teacherInfo[0]
        self.TFirstName = teacherInfo[1]
        self.classroom = teacherInfo[2]

    def __repr__(self):
        return "("+self.line+")"
