print("welcome to calculator")


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

math =input("enter your math:")

if math == "Addition":
    x=input("num1:")
    y=input("num2:")
    x=int(x)
    y=int(y)
    sum=x+y 
    print(f"the sum of {x} + {y} = {sum}")
    
elif math == "Subtraction":
    a=input("num3")
    b=input("num4")
    a=int(a)
    b=int(b)
    difference=a-b 
    print(f"the difference {a} - {b} = {difference}")
    
elif math == "Multiplication":
    x=input("num1")
    y=input("num2")
    x=int(x)
    y=int(y)
    product=x*y 
    print(f"the product of {x} * {y} = {product}")
    
elif math == "Division":
    a=input("num3")
    b=input("num4")
    a=int(a)
    b=int(b)
    quotient=a/b 
    print(f"the quotient {a} / {b} = {quotient}")
    





