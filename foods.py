total = 0

file = open ("foods.txt","r")
buffer = file.readlines()

file.close()
food = []
price = []
for line in buffer:
    line = line.strip()
    line = line.split(",")
    print(line)
    food.append(line[0])
    line[1] = float(line[1])
    price.append(line[1])
    
    
    
    
    
check = False
while check == False:
    print("Welcome to the Grocery Store!")

    print("1. add to cart")
    print("2. remove items")
    print("3. check out")
    action = input("What would you like to do today?:").strip().lower()
        
    if action == "add to cart":
        print(food)
        option = input("What do you want?")
        option = int()
        qunatity = input("How much would you like?")
        total = total + int(qunatity) * price[option]
        
    if action == "check out":
        print("You're total is:") 
        print(total)
        print("Thank you for shopping with us!")