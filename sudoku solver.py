#print board
def printBoard(board):
    print("---------------------")
    for x in range(0, 9):
        if x == 3 or x == 6:
            print("----------------------")
        for y in range(0, 9):
            if y == 3 or y == 6:
                print("|", end=" ")
            print(board[x][y], end=" ")
        print()
    print("----------------------")

#checking if board is full
def boardcheck(board):
    for x in range(0,9):
        for y in range(0,9):
            if board[x][y]==0:
                return False
    return True

#possible values
def PossibleEntry(board, i ,j):

    PossibilityArray = {}

    for x in range (1, 10):
        PossibilityArray[x] = 0
    

    #for horizontal

    for y in range(0,9):
        if not board[i][y] == 0:
            PossibilityArray[board[i][y]] = 1

    #for vertical

    for x in range(0,9):
        if not board[x][j] == 0:
            PossibilityArray[board[x][j]] = 1

    #for its own box

    k=0
    l=0

    if i>=0 and i<=2:
        k=0
    elif i>=3 and i<=5:
        k=3
    else:
        k=6

    if j>=0 and j<=2:
        l=0
    elif j>=3 and j<=5:
        l=3
    else:
        l=6

    for x in range(k,k+3):
        for y in range(l,l+3):
            if not board[x][x]==0:
                PossibilityArray[board[x][y]] = 1
    
    for x in range (1, 10):
        if PossibilityArray[x] == 0:
            PossibilityArray[x] = x
        else:
            PossibilityArray[x] = 0
    
    return PossibilityArray

#solver
def SudokuSolver(board):
    i = 0
    j = 0

    possiblities = {}

    if boardcheck(board):
        print('Successfully Solved')
        printBoard(board)
        return
    else:
        for x in range(0,9):
            for y in range(0,9):
                if board[x][y] == 0:
                    i = x
                    j = y
                    break
            else:
                continue
            break

        possiblities = PossibleEntry(board, i, j)
        
        for x in range (1, 10):
            if not possiblities[x] == 0:
                board[i][j] = possiblities[x]   #fill the board with predicted value from dict
                SudokuSolver(board)             #solves the board with above predicted value which is most likely wrong
        #after there is no possibility
        board[i][j] = 0     #backtrack (previous box gets reset)
        #previous predicted value is not repeated in the box
def main():
    SudokuBoard = [[0 for x in range(9)]for x in range(9)]
    SudokuBoard[0][0] = 0
    SudokuBoard[0][1] = 0
    SudokuBoard[0][2] = 0
    SudokuBoard[0][3] = 0
    SudokuBoard[0][4] = 0
    SudokuBoard[0][5] = 0
    SudokuBoard[0][6] = 2
    SudokuBoard[0][7] = 0
    SudokuBoard[0][8] = 0
    SudokuBoard[1][0] = 0
    SudokuBoard[1][1] = 8
    SudokuBoard[1][2] = 0
    SudokuBoard[1][3] = 0
    SudokuBoard[1][4] = 0
    SudokuBoard[1][5] = 7
    SudokuBoard[1][6] = 0
    SudokuBoard[1][7] = 9
    SudokuBoard[1][8] = 0
    SudokuBoard[2][0] = 6
    SudokuBoard[2][1] = 0
    SudokuBoard[2][2] = 2
    SudokuBoard[2][3] = 0
    SudokuBoard[2][4] = 0
    SudokuBoard[2][5] = 0
    SudokuBoard[2][6] = 5
    SudokuBoard[2][7] = 0
    SudokuBoard[2][8] = 0
    SudokuBoard[3][0] = 0
    SudokuBoard[3][1] = 7
    SudokuBoard[3][2] = 0
    SudokuBoard[3][3] = 0
    SudokuBoard[3][4] = 6
    SudokuBoard[3][5] = 0
    SudokuBoard[3][6] = 0
    SudokuBoard[3][7] = 0
    SudokuBoard[3][8] = 0
    SudokuBoard[4][0] = 0
    SudokuBoard[4][1] = 0
    SudokuBoard[4][2] = 0
    SudokuBoard[4][3] = 9
    SudokuBoard[4][4] = 0
    SudokuBoard[4][5] = 1
    SudokuBoard[4][6] = 0
    SudokuBoard[4][7] = 0
    SudokuBoard[4][8] = 0
    SudokuBoard[5][0] = 0
    SudokuBoard[5][1] = 0
    SudokuBoard[5][2] = 0
    SudokuBoard[5][3] = 0
    SudokuBoard[5][4] = 2
    SudokuBoard[5][5] = 0
    SudokuBoard[5][6] = 0
    SudokuBoard[5][7] = 4
    SudokuBoard[5][8] = 0
    SudokuBoard[6][0] = 0
    SudokuBoard[6][1] = 0
    SudokuBoard[6][2] = 5
    SudokuBoard[6][3] = 0
    SudokuBoard[6][4] = 0
    SudokuBoard[6][5] = 0
    SudokuBoard[6][6] = 6
    SudokuBoard[6][7] = 0
    SudokuBoard[6][8] = 3
    SudokuBoard[7][0] = 0
    SudokuBoard[7][1] = 9
    SudokuBoard[7][2] = 0
    SudokuBoard[7][3] = 4
    SudokuBoard[7][4] = 0
    SudokuBoard[7][5] = 0
    SudokuBoard[7][6] = 0
    SudokuBoard[7][7] = 7
    SudokuBoard[7][8] = 0
    SudokuBoard[8][0] = 0
    SudokuBoard[8][1] = 0
    SudokuBoard[8][2] = 6
    SudokuBoard[8][3] = 0
    SudokuBoard[8][4] = 0
    SudokuBoard[8][5] = 0
    SudokuBoard[8][6] = 0
    SudokuBoard[8][7] = 0
    SudokuBoard[8][8] = 0
    
    printBoard(SudokuBoard)
    SudokuSolver(SudokuBoard)
    
main()