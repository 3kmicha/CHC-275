board = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]
current_player = "O"

print(board)

def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print("|", end ="")
            print(board[i][j], end = "|")
        print()
printBoard(board)
            
def printplaceMaker(board,current_player,row,col):
    board[row][col] = current_player
    if board[row][col] == 0:
        pass
    else:
        print("Sorry that spot is taken")
        
def printswitchplayer(current_player):  
    if current_player == "0":
        return "X"
    elif current_player == "X":
        return "O"

def printcheckWinner(board, current_player):
    for i in range(len(board)):
       pass
   
    for row in board:
        for space in row:
            if space == 0: 
                return False

    return True

def main():
    grid = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    
    
    curr ="X"
    if __name__ == "__main__":
        main()