"""#1D List 
# - Mutable ( they can change in lentgh)
# - Square bracktes are used to get a singel elemnt out of a list 
# mylist(mylist[])
.append(val) adds things 
.remove(val) removes things

#2D List 
#same thing but instead of storing numbers and names instead of list you are storing lists inside of those lists 
#example 
"""

"""grid = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]
#- Square bracktes are used to get a singel elemnt out of a list
# This a naturaL thing to becaus ething slike 

print(grid[0][0])

"""
"""stythax is "print(grid[row][col])"
these list grow from top to bottom and lleft to right
[0][0] is top left

Travrtsing 1D List
"""
"""nums = [1,2,3,4,5]
for nums in nums: # This is a for each loop
    pass            # We cant directly acces our list 

for i in range(len(nums)): # This is for i loop
    pass

i = 0 
while i < len(nums): # While Loop
    i = i +1
"""

"""grid = [
    [1,2,3,4,5,6,7,8,9,10],
    [11,12,13,14,15,16,17],
    [18,19,20,21,22,23,24],
]
"""
"""for row in grid:
    for num in row:
        print(num)
        
for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(f"({i},{j})" = {grid[i][j]}", end = "")
"""              

board = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

print(board)

def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print("|", end ="")
            print(board[i][j], end = "|")
        print()
    printBoard(board)
            