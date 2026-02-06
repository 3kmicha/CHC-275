def update(num1):
    num1 = num1 + 10
x = 5
update(x)
print(x)


mylist = [1,2,3,4]
print(mylist)


def update2(nums):
    nums.append(5)
update2(mylist)
print(mylist)

def updateBalance(money, change):
    money = money - change 
    return money

balance = 1000
