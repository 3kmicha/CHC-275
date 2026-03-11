"""
Postion within a list is the index
it pulls it out
But it's not the best way to do it
    - We can order people by:
        - Birthday (index)
        - Name 
        - By the order they walked into a room
        
Lets use a dictionary 
"""


products = {"oranges":0, "apples" :5, "grapes":10,}
"To retieave info use sqruare brackets "
print(f"oranges: {products["oranges"]}")


"Below isnt the best way to create list cause what happens when something is removed, now everything is out of place"
productsList = [1,2,3,4,5,6]
print(productsList[3])
productsList.pop(3)
print(productsList[3])


"Adding to the dictionary"
products ["bananas"] = 30
print(f"Bananas: {products['bananas']}")
products [1] = 60
print(f"1: {products[1]}") 
print(products)


"Keys = The fruit"
"Values = The numbers"
"Looping with Dictionaires"


"This prints the values"
for x in products:
    print(products[x])


"This prints the keys"
"Keys are imutable meaning they can only be strings, numbers, and tuples"
for x in products:
    print(x)
for names in products.keys():
    print(names)

"This is how you remove stuff from dictionaires"
mydict = {1:"foo",2:"foot",3:"food",4:"fold",}
print(mydict)
"This is the unsafe way of doing it using del[]"
del mydict[1]
print(mydict)


"here is the safe way to do it using .pop()"
mydict.pop(2)

"heres how to copy, it just makes copies"
copy = mydict
print(copy)


"If you want to delete something but its already not there you can use this"
print(mydict.pop(2, "object not found"))


"Just clears everything within the list"
mydict.clear 


"New data type: Tuple's"
"Use an ordered pair notation like (x,y)"
"These are imutable"

mytuple = (10,20,30)
print(mytuple)

students = {}
students[(1,"John Smith")] = {"english": 80, "math": 93, "econ": 71}
print(students)