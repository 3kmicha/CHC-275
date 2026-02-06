
import math


"""
Function Name: getList
Parameters: none
Return Type: List
Description: Prompts user to fill in an empty list until they are satisfied 
"""
def getList():
    print("Welcome to the List Statistics Calculator")
    print("Enter a list of intergers or 'q' to end the lsit")
    print("Enter an interger: 1")
    print("Enter an interger: 2")
    print("Enter an interger: 3")
    print("Enter an interger: 4")
    print("Enter an interger: 5")
    print("Enter an interger: q")
    print("Please Choose the Statistic you would like to calculate")
    return list

""" 
Function Name: printMenu
Parameters: none
Return Type: none
Description: Prints menu for statistics calculator
"""
def printMenu():
    print("Please Choose the Statistic you would like to calculate")
    print("1. Min")
    print("2. Max")
    print("3. Mean")
    print("4. Median")
    print("5. Clear List")
    


"""
Function Name: getMean
Parameters: List
Return Type: Float
Description: Calculates the mean for the list and returns the value 
"""
def getMean(userList):
    sum = 0 
mylist = [17,64,16,71,13,92,97,98,31,60,83,2,84,68,62,22,24,76,95,55,6,59,10,29,35,85,26,4,1,53,12,61,20,77,89,5,94,74,25,81,70,82,73,18,15,46,69,3,87,66,23,80,42,21,7,65,9,
0,36,96,52,79,32,39,1,33,40,50,14,48,45,51,27,34,30,100,88,9,63,86,19,78,54,47,57
,49,67,91,56,44,58,72,43,38,11,37,75,4,28,99,8,93]
for num in mylist:
    sum = sum + num     
mean = sum / len(mylist)
print(mean)



"""
Function Name: getMedian
Parameters: List
Return Type: Float
Description: Calculates the median for the list and returns the value  
"""
def getMedian(userList):
    userList = sorted(userList)

""" 
Function Name: getMin
Parameters: List
Return Type: Float
Description: Finds the minimum of the unsorted list
"""
def getMin(userList):
    pass

""" 
Function Name: getMax
Parameters: List
Return Type: Float
Description: Finds the maximum of the unsorted list
"""
def getMax(userList):
    pass

""" 
Function Name: getStdDev
Parameters: List
Return Type: none
Description: Calculates the population Standard Deviation of a list
"""
def getStdDev(userList):
    pass



def main():
    pass


if __name__ == "__main__":
    main()