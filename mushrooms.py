


check = False
while check == False:
    
    option = input("What is the size of your mushroom?").strip().lower()
    print(option)

    if option == "stop":
            check = True
            
    if option.isnumeric():
        option = int(option)
        print("That is not a number!")
            
    elif option <= "100":
        print("You have a small Mushroom")
        
    elif option > "100" and option < "200":
            print("You have a medium Mushroom")
            
    elif option >= "200":
            print("You have a large Mushroom")
            
    elif option == "stop":
            check = True