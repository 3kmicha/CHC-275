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
    print("2. check out")
    action = input("What would you like to do today?:").strip().lower()
        
    if action == "add to cart":
        print(food)
        try:
            option = input("What do you want?")
            option = int(option)
            qunatity = input("How much would you like?")
            qunatity = int(qunatity)


            total = total + (qunatity) * price[option]
            print(total)
        except Exception as e:
            print(e)
            
    
        
    if action == "check out":
        tax = total * 0.06
        total = total + tax
        print("You're total is:") 
        print(total)
        print("Thank you for shopping with us!")