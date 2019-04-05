import StudentDicts
from Commands import*

def main():
#main method to run the entire program to produce user requested query data 
    studentDict = StudentDicts.StudentDicts("students.txt")
    parser(studentDict)

def parser(studentDict):
    #method to parse commandline user inputs and provide the corresponding query data 
    while(True):
        rawInput = input("Please enter the option for query: ")    
        parsedInput = rawInput.split()
    
        if parsedInput[0] == "S" or parsedInput[0]=="Student":
            if len(parsedInput)==2:
                Commands.searchStudent(parsedInput[1],False,studentDict)
            elif len(parsedInput)==3:
                if parsedInput[1]=="B" or parsedInput[1]=="Bus":
                    Commands.searchStudent(parsedInput[1],True,studentDict)
                else:
                    print("Usage: S[tudent] <lastname> B[us]")
            else:
                print("Usage: S[tudent] <lastname>")
    
        elif parsedInput[0] == "T" or parsedInput[0] == "Teacher":
            if len(parsedInput)==2:
                Commands.searchTeacher(parsedInput[1],True,studentDict)
            else:
                print("Usage: T[eacher] <lastname>")
    
        elif parsedInput[0] == "G" or parsedInput[0] == "Grade":
            if len(parsedInput)==2:
                Commands.searchGrade(parsedInput[1],False, False, studentDict)
            elif len(parsedInput)==3:
                if parsedInput[2]== "H" or parsedInput[2]=="High":
                    Commands.searchGrade(parsedInput[1],True, False, studentDict)
                elif parsedInput[2]=="L" or parsedInput[2]=="Low":
                    Commands.searchGrade(parsedInput[1],False,True, studentDict)
                else:
                    print("Usage: G[rade] <Number> H[igh] or G[rade] <Number L[ow]>")
            else:
                print("Usage: G[rade] <Number>")
    
        elif parsedInput[0] == "B" or parsedInput[0] == "Bus":
            if len(parsedInput)==2:
                Commands.searchBus(parsedInput[1],studentDict)
            else:
                print("Usage: B[us] <Number>")
    
        elif parsedInput[0] == "A" or parsedInput[0] == "Average":
            if len(parsedInput)==2:
                Commands.searchAverage(parsedInput[1],studentDict)
            else:
                print("Usage: A[verage] <Number>")
    
        elif parsedInput[0] == "I" or parsedInput[0] == "Info":
            Commands.searchInfo(studentDict)
    
        elif parsedInput[0] == "Q" or parsedInput[0] == "Quit":
            break
    
        else:
            print("Unrecognized input, please try again")
            

if __name__ == "__main__":
    main()
    