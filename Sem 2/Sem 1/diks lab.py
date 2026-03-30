"""
Name: Micha Morozov
Section: 1
Description: Template for Lab 5
"""

"""
Scenario: we live in a world where blackbaud no longer exists. our job is to write
a student records program that can print out the transcript, grade level, and email of our students.
You are to implement this using functions, dictionaries, and lists
"""


def getStudent(directory, student):
    """
        Function Name: getStudent
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type: Multiple returns of all values associated to the keys at directory[student] 
        Description:
            A Function that returns all of the values associated to the keys in the dictionary at key "student"
    """
    pass

def getStudentGrades(directory, student):
    """
        Function Name: getStudentGrades
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type: Dictionary of Student Gradebook
        Description:
            A Function that returns a Dictinary of the student's gradebook at dictionary[student]
    """
    pass

def getStudentGradeLevel(directory,student):
    """
        Function Name: getStudentGradeLevel
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type:  integer corresponding to student's grade level
        Description:
            A Function that returns a Dictionary of the student's gradebook at dictionary[student]
    """
    pass

def getStudentEmail(directory,student):
    """
        Function Name: getStudentGradeLevel
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type:  string corresponding to student's email
        Description:
            A Function that returns a string of the student's email at dictionary[student]
    """
    email = input("What is the students email?")

def getStudentsByGradeLevel(directory, gradelevel):
    """
        Function Name: getStudentsbyGradeLevel
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            gradelevel <int> : integer corresponding to the grade level
            Return Type:  none
        Description:
            procedure that prints out all of the students of a corresponding grade level.
    """
    
    

def addStudent(directory):
    name = input("What is the students name?").strip().lower()
    email = input("What is the students email?").strip().lower()
    gradelevel = int(input("What is the students Grade Level"))
    grades = {"History": int(input("What is the History Grade?")), "English": int(input("What is the English Grade?")), "Math": int(input("What is the Math Grade?")), "Religion": int(input("What is the Religion Grade?"))}
    directory [name] = {"email": email, "gradelevel": gradelevel, "grades": grades}
    
    
   

def removeStudent(directory, student):
    directory.pop(student)
    

def updateGrade(directory, student):
    """
     Function Name: updateGrades
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type:  none
        Description:
            procedure that updates a student's gradebook
    """
    pass


def calculateGPA(directory, student):
    """
     Function Name: calculateGPA
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type:  <float> average of all grades
        Description:
            creates a GPA variable set equal to zero, then computes the average (mean) of all of the grades in the gradebook
    """
    GPA = 0
    pass


def checkHonorRoll(directory,student):
    """
     Function Name: checkHonorRoll
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type:  <bool> True or False depending on a student has made the honor roll or not
        Description:
            Calls the calculateGPA() subroutine that gets the GPA then checks all grades in the grade book to see if they are all over 81, then returns True or False depending on if the GPA is 88 or better
    """
    pass

def printMenu():
    
    
    print("2. Add Student")
    print("3. Remove Student")
    print("4. Get Student")
    print("5. Update Grades")
    print("6. Calculate GPA")
    print("7. Get Student by Grade Level")
    print("8. Exit")
    
    
    
    
    
def main():
    Students = {}
    print("1. Welcome to Calvert Hall's Student Directory")
    check = False
    while check == False:
        printMenu()
        option = input("Please make a selection:")
        if option.strip() == "8":
            print("You have exited Calvert Hall's Student Directory")
            check = True
        if option == "2":
            addStudent(Students)
            print(Students)
        if option == "3":
            removeStudent(directory, student)
        if option == "4":
            pass
        if option == "5":
            pass
        if option == "6":
            pass
        if option == "7":
            pass

if __name__ == "__main__":
    main()

