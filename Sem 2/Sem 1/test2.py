def getMean(userList):
    sum = 0
    userList = []
    for num in userList:
        sum = sum + num
    mean = sum / len(userList)
    print(mean)