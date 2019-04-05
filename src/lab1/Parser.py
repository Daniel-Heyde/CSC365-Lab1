import Student
import StudentDicts
import Commands

def main():
#main method to run the entire program to produce user requested query data 
    studentDict = StudentDicts("students.txt");
    parser(studentDict)

def parser():
    #method to parse commandline user inputs and provide the corresponding query data 
    while(True):
        rawInput = input("Please enter the option for query: ")    
        parsedInput = rawInput.split()
    
        if parsedInput[0] == "S" or parsedInput[0]=="Student":
            if len(parsedInput)==2:
                print("query for grade and classrom assignment")
            elif len(parsedInput)==3:
                if parsedInput[1]=="B" or parsedInput[1]=="Bus":
                    print("query for bus route")
                else:
                    print("Usage: S[tudent] <lastname> B[us]")
            else:
                print("Usage: S[tudent] <lastname>")
    
        elif parsedInput[0] == "T" or parsedInput[0] == "Teacher":
            if len(parsedInput)==2:
                print("query for students")
            else:
                print("Usage: T[eacher] <lastname>")
    
        elif parsedInput[0] == "G" or parsedInput[0] == "Grade":
            if len(parsedInput)==2:
                print("query for last and first name according to grade")
            elif len(parsedInput)==3:
                if parsedInput[2]== "H" or parsedInput[2]=="High":
                    print("find studnet with higheset GPA")
                elif parsedInput[2]=="L" or parsedInput[2]=="Low":
                    print("find student with lowest GPA")
                else:
                    print("Usage: G[rade] <Number> H[igh] or G[rade] <Number L[ow]>")
            else:
                print("Usage: G[rade] <Number>")
    
        elif parsedInput[0] == "B" or parsedInput[0] == "Bus":
            if len(parsedInput)==2:
                print("query for students name that takes the same bus")
            else:
                print("Usage: B[us] <Number>")
    
        elif parsedInput[0] == "A" or parsedInput[0] == "Average":
            if len(parsedInput)==2:
                print("query for average GPA for given grade")
            else:
                print("Usage: A[verage] <Number>")
    
        elif parsedInput[0] == "I" or parsedInput[0] == "Info":
            print("query for number students for each grade")
    
        elif parsedInput[0] == "Q" or parsedInput[0] == "Quit":
            break
    
        else:
            print("Unrecognized input, please try again")
            

if __name__ == "__main__":
    main()
    