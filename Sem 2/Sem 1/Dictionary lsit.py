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

for x in products:
    print(products[x])
"This prints the values"

for x in products:
    print(x)
for names in products.keys():
    print(names)
"This prints the keys"

