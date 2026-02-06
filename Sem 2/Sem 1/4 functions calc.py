def add (x,y):
    return x + y 

def subtract (x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y
def pow(x,y):
    return x ** y

def main():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Pow")
    print("6. quit")

    check = False
    while check == False:

            math =input("enter your math:").strip().lower()
            try: 
                    
                    if math == "addition":
                            x=input("num1:")
                            y=input("num2:")
                            x=int(x)
                            y=int(y)
                            sum = add (x,y)
                            print(f"the sum of {x} + {y} = {sum}")
                    
                    elif math == "subtraction":
                            a=input("num3:")
                            b=input("num4:")
                            a=int(a)
                            b=int(b)
                            difference=subtract (x,y)
                            print(f"the difference {a} - {b} = {difference}")
                    
                    elif math == "multiplication":
                            x=input("num1:")
                            y=input("num2:")
                            x=int(x)
                            y=int(y)
                            product=x*y 
                            print(f"the product of {x} * {y} = {product}")
                    
                    elif math == "division":
                            a=input("num3:")
                            b=input("num4:")
                            a=int(a)
                            b=int(b)
                            quotient=a/b 
                            print(f"the quotient {a} / {b} = {quotient}")
                            
                    elif math == "pow":
                            a=input("num3:")
                            b=input("num4:")
                            a=int(a)
                            b=int(b)
                            result=a/b 
                            print(f"the result {a} ** {b} = {result}")


                    elif math == "quit":
                            check = True
                    
            except ValueError:
                    print("x and y must be numbers")

            except ZeroDivisionError:
                    print("y cannot be 0")

            except Exception as e:
                    print(e)
if __name__ == "__main__":
    main()