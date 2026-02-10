import math

def makeList():
    nums = []
    check = False
    while check == False:
        option = input("Enter a list of intergers or 'q' to end the lsit:")
        if option == "quit".lower():
            check = True
        else: 
            option = int(option)
            nums.append(option)
    return(nums)

def printMenu():
    print("Please Choose the Statistic you would like to calculate")
    print("1. Min")
    print("2. Max")
    print("3. Mean")
    print("4. Median")
    print("5. Clear List")
""""""    


"""
Function Name: getMean
Parameters: List
Return Type: Float
Description: Calculates the mean for the list and returns the value 
"""
def getMean(userList):
    pass

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
    print("Welcome to the List Statistics Calculator")
    list1 = makeList()
    print(list1)
    check = False
    while check == False:
        printMenu()
        option = input("Select what you want top do:")
        if option == "q":
            check = True


if __name__ == "__main__":
    main()