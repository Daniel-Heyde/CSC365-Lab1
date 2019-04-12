from StudentDicts import StudentDicts
from Commands import Commands

def parser(studentDict):
    #method to parse commandline user inputs and provide the corresponding query data 
    while(True):
        rawInput = input("Please enter the option for query: ")
        parsedInput = rawInput.split()

        if len(parsedInput) == 0:
            continue
    
        if parsedInput[0] == "S" or parsedInput[0]=="Student":
            search_by_student(parsedInput, studentDict)
    
        elif parsedInput[0] == "T" or parsedInput[0] == "Teacher":
            searchByTeacher(parsedInput, studentDict)
    
        elif parsedInput[0] == "G" or parsedInput[0] == "Grade":
            searchByGrade(parsedInput, studentDict)
    
        elif parsedInput[0] == "B" or parsedInput[0] == "Bus":
            searchByBus(parsedInput, studentDict)
    
        elif parsedInput[0] == "A" or parsedInput[0] == "Average":
            searchByGpa(parsedInput, studentDict)
        
        elif parsedInput[0] == "C" or parsedInput[0] == "Classroom":
            searchByClassroom(parsedInput, studentDict)
        
        elif parsedInput[0] == "E" or parsedInput[0] == "Enrollment":
            Commands().enrollment(studentDict)
            
        elif parsedInput[0] == "D" or parsedInput[0] == "Data":
            Commands().analytics(parsedInput, studentDict)
            
        elif parsedInput[0] == "I" or parsedInput[0] == "Info":
            Commands().info(studentDict)
    
        elif parsedInput[0] == "Q" or parsedInput[0] == "Quit":
            break
    
        else:
            print("Unrecognized input, please try again")

def search_by_student(parsedInput, studentDict):
    if len(parsedInput) == 2:
        Commands().searchStudent(parsedInput[1], False, studentDict)
    elif len(parsedInput) == 3:
        if parsedInput[2] == "B" or parsedInput[2] == "Bus":
            Commands().searchStudent(parsedInput[1], True, studentDict)
        else:
            print("Usage: S[tudent] <lastname> B[us]")
    else:
        print("Usage: S[tudent] <lastname>")

def searchByTeacher(parsedInput, studentDict):
    if len(parsedInput) == 2:
        Commands().searchTeacher(parsedInput[1], studentDict)
    else:
        print("Usage: T[eacher] <lastname>")

def searchByGrade(parsedInput, studentDict):
    if len(parsedInput) == 2:
        Commands().searchGrade(parsedInput[1], 1, studentDict)
    elif len(parsedInput) == 3:
        if parsedInput[2] == "H" or parsedInput[2] == "High":
            Commands().searchGrade(parsedInput[1], 2, studentDict)
        elif parsedInput[2] == "L" or parsedInput[2] == "Low":
            Commands().searchGrade(parsedInput[1], 3, studentDict)
        elif parsedInput[2] == "T" or parsedInput[2] == "Teacher":
            Commands().searchGrade(parsedInput[1], 4, studentDict)
        else:
            print("Usage: G[rade] <Number> H[igh] or G[rade] <Number> L[ow] or G[rade] <Number> T[eacher]")
    else:
        print("Usage: G[rade] <Number>")

def searchByBus(parsedInput, studentDict):
    if len(parsedInput) == 2:
        Commands().searchBus(parsedInput[1], studentDict)
    else:
        print("Usage: B[us] <Number>")

def searchByGpa(parsedInput, studentDict):
    if len(parsedInput) == 2:
        Commands().searchAverage(parsedInput[1], studentDict)
    else:
        print("Usage: A[verage] <Number>")
def searchByClassroom(parsedInput, studentDict):
    if len(parsedInput) == 3:
        if parsedInput[2] == "S" or parsedInput[2] == "Student":
            Commands().searchClassroom(parsedInput[1], 1, studentDict)
        elif parsedInput[2] == "T" or parsedInput[2] == "Teacher":
            Commands().searchClassroom(parsedInput[1], 2, studentDict)
        else:
            print("Usage: C[lassroom] <Number> S[tudent] or C[lassroom] <Number> T[eacher] ");
    else:
            print("Usage: C[lassroom] <Number> S[tudent] or C[lassroom] <Number> T[eacher] ");

def analytics(parsedInput, studentDict):
    if len(parsedInput) == 3:
        if parsedInput[1] == "G" or parsedInput[1] == "Grade":
            #parsedInput[2] would be the grader number of the student
            Commands().dataAnalyze(parsedInput[1], parsedInput[2], 1, studentDict)
        elif parsedInput[1] == "B" or parsedInput[1] == "Bus":
            #parsedInput[2] would be the bus route number of student 
            Commands().dataAnalyze(parsedInput[1], parsedInput[2], 2, studentDict)
        else:
            print("Usage: D[ata] G[rade] <Number> or D[ata] B[us] <Number>")
            
    elif len(parsedInput) == 4:
        if parsedInput[1] == "G" or parsedInput[1] == "Grade":
            if parsedInput[3] == "T" or parsedInput[3] == "Teacher":
                #parsedInput[2] as grader number 
                Commands().dataAnalyze(parsedInput[1], parsedInput[2], 3, studentDict)
        else:
            print("Usage: D[ata] G[rade] <Number> T[eacher]")
    else:
        print("Usage: D[ata] G[rade] <Number> or D[ata] B[us] <Number> or D[ata] G[rade] <Number> T[eacher]")
        
if __name__ == "__main__":
    # main method to run the entire program to produce user requested query data
    studentDict = StudentDicts("students.txt")
    parser(studentDict)