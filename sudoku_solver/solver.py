board = [
    [8,4,0,7,9,0,2,0,0],
    [6,5,0,0,0,2,0,0,0],
    [0,0,0,4,0,5,9,0,3],
    [7,6,0,0,0,0,8,0,0],
    [3,0,8,0,0,0,7,0,9],
    [0,0,4,0,0,0,0,2,6],
    [4,0,7,3,0,8,0,0,0],
    [0,0,0,5,0,0,0,4,1],
    [0,0,5,0,4,1,0,8,7],
]
    
#prints the board by traversing through matrix
def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
                print("------------------------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ",end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j])+" ", end="")

#finds the first empty space and returns the coordinate
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == 0):
                return (i,j)
    return False

#check if the input is valid
def check(board, number, position):
    #check row
    #goes through the row and check for number
    #if the row contains the number that's not in the empty space position, return false
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    #check column
    #goes through the column and check for number
    #if the column contains the number that's not in the empty space position, return false
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False
    #check the whole box
    #goes through the box, if you find the number, then you check if the position
    #is the same as the empty box position
    #return false if it's not, else return true
    box_row = position[1]//3
    box_column = position[0]//3
    for y in range(box_column*3, box_column*3 + 3):
        for x in range(box_row*3, box_row*3 + 3):
            if board[y][x] == number and (y,x) != position:
                return False
    return True

#solves the sudoku
def solution(board):
    #gets the coordinates
    found = findEmpty(board)
    if not found:
        return True
    else:
        row, column = found
    #go through all numbers on each space
    for i in range(1,10):
        if check(board, i, (row, column)):
            board[row][column] = i

            if solution(board):
                return True

            board[row][column] = 0
    return False


printBoard(board)
solution(board)
print("*********************************")
printBoard(board)
