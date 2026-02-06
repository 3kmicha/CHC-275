def getMedian(userList):

    n = len(userList)

    middle_index = n // 2

    return userList[middle_index]

    middle1 = userList[(n // 2) - 1]

    middle2 = userList[n // 2]

    return (middle1 + middle2) / 2