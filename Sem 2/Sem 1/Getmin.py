def getMin(numbers):

    number is smallest

    smallest = numbers[0]

    for number in numbers:

     

        if number < smallest:

            smallest = number

   

    return smallest

 

first = [1, 2, 3, 4]

print(first)

print(getMin(first))

second = [4, 2, 1, 3]

print(second)

print(getMin(second))

 