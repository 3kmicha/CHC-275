import math

def makeList():
    nums = []
    check = False
    while check == False:
        option = input("Enter a list of intergers or 'q' to end the lsit:")
        if option == "q".lower():
            check = True
        else: 
            try:
                option = int(option)
                nums.append(option)
            except ValueError:
                print("Sorry you must type in an interger :(")
    return(nums)

def printMenu():
    print("Please Choose the Statistic you would like to calculate")
    print("1. Min")
    print("2. Max")
    print("3. Mean")
    print("4. Median")
    print("5. Clear List")
    print("6. q")
   


"""
Function Name: getMean
Parameters: List
Return Type: Float
Description: Calculates the mean for the list and returns the value 
"""
def getMean(userList):
    sum = 0
    userList = []
    for num in userList:
        sum = sum + num
    mean = sum / len(userList)
    print(mean)

"""
Function Name: getMedian
Parameters: List
Return Type: Float
Description: Calculates the median for the list and returns the value  
"""
def getMedian(userList):
    userList = sorted(userList)
    n = len(userList)
    if n % 2 == 1:
        
        middle_index = n // 2
        return userList[middle_index]
    else: middle_index

""" 
Function Name: getMin
Parameters: List
Return Type: Float
Description: Finds the minimum of the unsorted list
"""
def getMin(userList):
     userList = []
     smallest = userList[0]
     for userList in userList:
         if userList < smallest:
            smallest = userList
     return smallest
    
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
        option = input("Select what you want to Calculate:")
        if option.lower() == "q":
            check = True
        if option == "1":
            min = getMin(list1)
            print(f"You're Min is {min}")
        elif option == "2":
            max = getMax(list1)
            print(f"You're Max is {max}")
        
        elif option == "3":
            mean = getMean(list1)
            print(f"You're Mean is {mean}")
            
        elif option == "4":
            median = getMedian(list1)
            print(f"You're Median is {median}")
            
        elif option == "5":
            pass
        
        else: print()
        


if __name__ == "__main__":
    main()