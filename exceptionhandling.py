try: 
    x = input("Enter num 1:")
    y = input("Enter num 2:")
    x = int(x)
    y = int(y)
    quotient = (x/y)
    print(quotient)
except ValueError:
    print("x and y must be numners")

except ZeroDivisionError:
    print("y cannot be 0")

except Exception as e:
    print(e)

finally: 
    print("Thanks for using the Calculator")
    
    
"""
try: 
    code block
    
except exception:
    code block


"""