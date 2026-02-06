def makeList():
    nums = []
    check = False
    while check == False:
        option = input("Enter a value or quit:")
        if option == "quit".lower():
            check = True
        else: 
            option = int(option)
            nums.append(option)
    return(nums)
            

list1 = makeList()
print(list1)
list2 = makeList()
print(list2)