import random
import copy

# it throws a fit if I don't define these here:
board = []
boardMatrix = []
actionBoard = []

# difficulties:
easy = [9, 9, 10]
intermediate = [16, 16, 40]
expert = [16, 30, 99]

def minesweeperSettings():

    global difficulty
    
    print("\n| python minesweeper by jakecolon3 :D |\n\n")

    print("select seed (0 to randomize):\n")
    try:
      seed = int(input("seed: "))
    except:
      print("\nseed must be an integer!\n")
      minesweeperSettings()



    # seed:
    if seed != 0:
        random.seed(seed)
    else:
        random.seed(random.randrange(0, 10))

    
    print("easy (9x9, 10 mines)\nintermediate (16x16, 40 mines)\nexpert (30x16, 99 mines)\ncustom")
    difficultyInput = input("select difficulty: ")
    
    if difficultyInput.casefold() == "easy":
        difficulty = easy
    elif difficultyInput.casefold() == "intermediate":
        difficulty = intermediate
    elif difficultyInput.casefold() == "expert":
        difficulty = expert
    elif difficultyInput.casefold() == "custom":
        print("choose board size and amount of mines (example: 12, 12, 35)")
        customDifficulty = input("rows, columns, mines: ").split(", ")
        difficulty = [int(x) for x in customDifficulty]
    else:
        print("\nnot a valid difficulty! try again\n")
        minesweeperSettings()

    minesweeper()

  
def minesweeper():

    # creates a tuple with boardDimensions - mineAmount zeroes and mineAmount ones and shuffles it
    def minesweeperPositions(boardRows, boardColumns, mineAmount):

        # creates a tuple filled with mineAmount ones
        def minesweeperMines(mineAmount):

            mines = []

            for mine in range(mineAmount):
                mines.append(1)

            mines = tuple(mines)

            return(mines)

        # creates a tuple filled with boardRows * boardColumns zeroes
        def minesweeperSize(boardRows, boardColumns):

            size = []

            for cell in range(boardColumns * boardRows):
                size.append(0)

            size = tuple(size)
            return(size)

        global boardSize
        boardSize = (boardRows, boardColumns)

        global board

        mines = list(minesweeperMines(mineAmount))
        size = list(minesweeperSize(boardRows, boardColumns))

        board = list(size.copy() + mines.copy())

        mines = tuple(mines)
        size = tuple(size)

        for extraSpace in range(len((mines))):
            board.remove(0)

        random.shuffle(board)

        return(board)


    # generates a matrix of zeroes and ones accoring to the board variable
    def minesweeperBoard(boardRows, boardColumns, mineAmount):

        global actionBoard
        global boardMatrix
        boardMatrix = []
        boardMatrixConstructor = []
        row = 0
        boardIndex = 0

        minesweeperPositions(boardRows, boardColumns, mineAmount)

        for row in range(boardRows): 
            for column in range(boardColumns):
                boardMatrixConstructor.append(board[boardIndex])
                boardIndex += 1
            boardMatrix.append(boardMatrixConstructor.copy())
            boardMatrixConstructor.clear()

        actionBoard = copy.deepcopy(boardMatrix)
        return(boardMatrix)

    minesweeperBoard(*difficulty)


    # creates a matrix filled with zeroes, iterates through boardMatrix and increments numberBoard cells adjacent to a mine relative to boardMatrix by 1 whenever it encounters one
    def minesweeperNumberBoard(boardRows, boardColumns, mineAmount):

        global numberBoard
        numberBoard = []
        numberBoardRow = []

        for row in range(boardRows):
            for column in range(boardColumns):
                numberBoardRow.append(0)
            numberBoard.append(numberBoardRow)
            numberBoardRow = []

        boardRows -= 1
        boardColumns -= 1

        x = 0
        y = 0
        for row in boardMatrix:
            for cell in row:
                if x == 0 and y == boardRows:

                    if cell == 1:
                        numberBoard[y][x + 1] += 1
                        numberBoard[y - 1][x] += 1
                        numberBoard[y - 1][x + 1] += 1
                    x += 1

                elif x == boardColumns and y == 0:

                    if cell == 1:
                        numberBoard[y + 1][x] += 1
                        numberBoard[y][x - 1] += 1
                        numberBoard[y + 1][x - 1] += 1
                    x += 1

                elif x == boardColumns and y == boardRows:

                    if cell == 1:
                        numberBoard[y - 1][x] += 1
                        numberBoard[y][x - 1] += 1
                        numberBoard[y - 1][x - 1] += 1
                    x += 1

                elif x == 0:

                    if cell == 1:
                        numberBoard[y + 1][x] += 1
                        numberBoard[y][x + 1] += 1
                        numberBoard[y + 1][x + 1] += 1
                        numberBoard[y - 1][x] += 1
                        numberBoard[y - 1][x + 1] += 1
                    x += 1

                elif y == 0:

                    if cell == 1:
                        numberBoard[y + 1][x] += 1
                        numberBoard[y][x + 1] += 1
                        numberBoard[y + 1][x + 1] += 1
                        numberBoard[y][x - 1] += 1
                        numberBoard[y + 1][x - 1] += 1
                    x += 1

                elif y == boardRows:

                    if cell == 1:
                        numberBoard[y][x + 1] += 1
                        numberBoard[y - 1][x] += 1
                        numberBoard[y][x - 1] += 1
                        numberBoard[y - 1][x - 1] += 1
                        numberBoard[y - 1][x + 1] += 1
                    x += 1

                elif x == boardColumns:

                    if cell == 1:
                        numberBoard[y + 1][x] += 1
                        numberBoard[y - 1][x] += 1
                        numberBoard[y][x - 1] += 1
                        numberBoard[y - 1][x - 1] += 1
                        numberBoard[y + 1][x - 1] += 1
                    x += 1

                elif x != 0 and y != 0:

                    if cell == 1:
                        numberBoard[y + 1][x] += 1
                        numberBoard[y][x + 1] += 1
                        numberBoard[y + 1][x + 1] += 1
                        numberBoard[y - 1][x] += 1
                        numberBoard[y][x - 1] += 1
                        numberBoard[y - 1][x - 1] += 1
                        numberBoard[y + 1][x - 1] += 1
                        numberBoard[y - 1][x + 1] += 1
                    x += 1

                elif x == 0 and y == 0:

                    if cell == 1:
                        numberBoard[y + 1][x] += 1
                        numberBoard[y][x + 1] += 1
                        numberBoard[y + 1][x + 1] += 1
                    x += 1

            x = 0
            y += 1

    minesweeperNumberBoard(*difficulty)


# actions:
sweep = s = "s"
flag = f = "f"
uncertain = "?"

# modifies a copy of the board with a specified operation (sweep, flag, ?)
def minesweeperAction(row, column, action = sweep):

    global actionBoard

    # replaces a value in the actionBoard matrix with "s"
    def minesweeperActionSweep(row, column):

        if row > boardSize[0] or column >= boardSize[1]:
            print("invalid position! please select a valid position.\n")
            minesweeperInput()
        elif actionBoard[row][column] == sweep:
            print("Cell has already been swept.\n")
            minesweeperInput()
        elif actionBoard[row][column] == flag:
            print("Cell is flagged.")
            minesweeperInput()
        elif actionBoard[row][column] == 1:
            print("\nyou hit a mine!\n\ntry again?")
            retry = input("type retry to retry with the same settings, n to go back to difficulty select: ")
            if retry.casefold() == "retry":
                minesweeper()
            else:
                minesweeperSettings()
        else:
            actionBoard[row][column] = sweep

        return(actionBoard)

    # replaces a value in the actionBoard matrix with "f" except if it is already "f" in which case it resets it
    def minesweeperActionFlag(row, column):

        if row > boardSize[0] or column >= boardSize[1]:
            print("invalid position! please select a valid position.\n")
            minesweeperInput()
        elif actionBoard[row][column] == flag:
            actionBoard[row][column] = boardMatrix[row][column]
        elif actionBoard[row][column] == sweep:
            print("Cell has already been swept.\n")
            minesweeperInput()
        else:
            actionBoard[row][column] = flag
        return(actionBoard)

    # replaces a value in the actionBoard matrix with "?"
    def minesweeperActionUncertain(row, column):

        if row > boardSize[0] or column > boardSize[1]:
            print("invalid position! please select a valid position.\n")
            minesweeperInput()
        else:
            actionBoard[row][column] = uncertain
        return(actionBoard)


    if action == sweep:
        actionBoard = minesweeperActionSweep(row, column)
    elif action == flag:
        actionBoard = minesweeperActionFlag(row, column)
    elif action == uncertain:
        actionBoard = minesweeperActionUncertain(row, column)
    else:
        print("invalid action! please select a valid action.\n")
        minesweeperInput()

# prints a formatted board by concatenating strings according to actionBoard and numberBoard contents
def minesweeperBoardDisplayed():

    displayedBoard = copy.deepcopy(actionBoard)
    displayedBoardPrinter = ""

    x = 0
    y = 0
    for row in displayedBoard:
        for cell in row:
            if cell == s:
                displayedBoard[y][x] = f"[{numberBoard[y][x]}]"
            elif cell == f:
                displayedBoard[y][x] = "[f]"
            elif displayedBoard[y][x] == uncertain:
                displayedBoard[y][x] = "[?]"
            else:
                displayedBoard[y][x] = "[ ]"
            x += 1
        y += 1
        x = 0


    x = 0
    y = 0
    for row in displayedBoard:
        for column in displayedBoard:
            displayedBoardPrinter += displayedBoard[y][x]
            x += 1
        displayedBoardPrinter += "\n"
        x = 0
        y += 1

    print(displayedBoardPrinter)

minesweeperSettings()

def minesweeperInput():
    minesweeperBoardDisplayed()
    action = input("type row, column, action (defaults to sweep): ").split(", ")
    try:
        action = [int(i) for i in action[:2]]
    except:
        print("\ninvalid input! try again\n")
        minesweeperInput()
    minesweeperAction(*action)

while True:
    print("\nwhat will you do?\n s: sweep\n f: flag\n ?: uncertain\n")
    minesweeperInput()
  