from StudentDicts import StudentDicts
from Commands import Commands

def parser(studentDict):
    #method to parse commandline user inputs and provide the corresponding query data 
    while(True):
        rawInput = input("Please enter the option for query: ")
        parsedInput = rawInput.split()
    
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
    
        elif parsedInput[0] == "I" or parsedInput[0] == "Info":
            Commands().info(studentDict.by_grade)
    
        elif parsedInput[0] == "Q" or parsedInput[0] == "Quit":
            break
    
        else:
            print("Unrecognized input, please try again\n")

def search_by_student(parsedInput, studentDict):
    if len(parsedInput) == 2:
        Commands().searchStudent(parsedInput[1], False, studentDict.by_st_last_name)
    elif len(parsedInput) == 3:
        if parsedInput[1] == "B" or parsedInput[1] == "Bus":
            Commands().searchStudent(parsedInput[1], True, studentDict.by_st_last_name)
        else:
            print("Usage: S[tudent] <lastname> B[us]\n")
    else:
        print("Usage: S[tudent] <lastname>\n")

def searchByTeacher(parsedInput, studentDict):
    if len(parsedInput) == 2:
        Commands().searchTeacher(parsedInput[1], studentDict.by_t_last_name)
    else:
        print("Usage: T[eacher] <lastname>\n")

def searchByGrade(parsedInput, studentDict):
    if len(parsedInput) == 2:
        Commands().searchGrade(parsedInput[1], False, False, studentDict.by_grade)
    elif len(parsedInput) == 3:
        if parsedInput[2] == "H" or parsedInput[2] == "High":
            Commands().searchGrade(parsedInput[1], True, False, studentDict.by_grade)
        elif parsedInput[2] == "L" or parsedInput[2] == "Low":
            Commands().searchGrade(parsedInput[1], False, True, studentDict.by_grade)
        else:
            print("Usage: G[rade] <Number> H[igh] or G[rade] <Number L[ow]>\n")
    else:
        print("Usage: G[rade] <Number>\n")

def searchByBus(parsedInput, studentDict):
    if len(parsedInput) == 2:
        Commands().searchBus(parsedInput[1], studentDict.by_bus)
    else:
        print("Usage: B[us] <Number>\n")

def searchByGpa(parsedInput, studentDict):
    if len(parsedInput) == 2:
        Commands().searchAverage(parsedInput[1], studentDict.by_grade)
    else:
        print("Usage: A[verage] <Number>\n")

if __name__ == "__main__":
    # main method to run the entire program to produce user requested query data
    studentDict = StudentDicts("students.txt")
    parser(studentDict)