
file = open ("names.txt","r")
buffer = file.readlines()
print(buffer)
file.close()
names = []
grades = []
for line in buffer:
    line = line.strip()
    line = line.split(",")
    print(line)
    names.append(line[0])
    line[1] = int(line[1])
    grades.append(line[1])
    
print(names)
print(grades)
    
names.append('Oden')
grades.append(21)
buffer = []
file = open ("names.txt","w")
for i in range(len(names)):
    line = f"{names[i]},{grades[i]}\n"
    buffer.append(line)
    
buffer[-1] = buffer[-1].strip()

file.writelines(buffer)
file.close

