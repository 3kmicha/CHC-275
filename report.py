file = open ("day 1_20.txt","r")
buffer = file.readlines()
file.close()

MSFT = buffer [0].strip().split(f",")
MSFT.pop(0)
AMZN = buffer [1].strip().split(f",")
AMZN.pop(0)
NVDA = buffer [2].strip().split(f",")
NVDA.pop(0)
for i in range(len(MSFT)):
    MSFT [i] = int(MSFT [i])
    AMZN [i] = int(AMZN [i])
    NVDA [i] = int(NVDA [i])
    
print(MSFT)
print(AMZN)
print(NVDA)


    




