

mylist = [5,10,15,20,25,30,35,40,]
print(mylist)

i = 0
while i <= len(mylist) - 1:
    (mylist[i]) = mylist[i] + 5
    i = i + 1
    
print(mylist)   
    
mylist = [5,10,15,20,25,30,35,40,]
for num in mylist:
    num = num + 5

print(mylist)

for i in range(len(mylist)):
    mylist[i] = mylist[i] + 5