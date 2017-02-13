#Skeleton Program for the AQA COMP1 Summer 2016 examination
#this code should be used in conjunction with the Preliminary Material
#written by the AQA COMP1 Programmer Team
#developed in a Python 3.4 programming environment

import random

def SetUpGameBoard(Board, BoardSize):
    for Row in range(1, BoardSize + 1):
        for Column in range(1, BoardSize + 1):
            if (Row == (BoardSize + 1) // 2 and Column == (BoardSize + 1) // 2 + 1) or (Column == (BoardSize + 1) // 2 and Row == (BoardSize + 1) // 2 + 1):
                Board[Row][Column] = "C"
            elif (Row == (BoardSize + 1) // 2 + 1 and Column == (BoardSize + 1) // 2 + 1) or (Column == (BoardSize + 1) // 2 and Row == (BoardSize + 1) // 2):
                Board[Row][Column] = "H"
            else:
                Board[Row][Column] = " "
            #end if
        #end for
    #end for
#end def for SetUpGameBoard()



def ChangeBoardSize():
    BoardSize = int(input("Enter a board size (between 4 and 9): "))
    while not(BoardSize >= 4 and BoardSize <= 9):
        BoardSize = int(input("Enter a board size (between 4 and 9): "))
    #end while
    return BoardSize
#end def for ChangeBoardSize()


def GetHumanPlayerMove(PlayerName):
    print(PlayerName, "enter the coordinates of the square where you want to place your piece: ", end="")
    Coordinates = int(input())
    return Coordinates
#end def for GetHumaPlayerMove


def GetComputerPlayerMove(BoardSize):
    return random.randint(1, BoardSize) * 10 + random.randint(1, BoardSize)
#end def ofr GetComputerPlayerMove

def GameOver(Board, BoardSize):
    for Row in range(1, BoardSize + 1):
        for Column in range(1, BoardSize + 1):
            if Board[Row][Column] == " ":
                return False
            #end if
        #end for (column)
    #end for (row)
    return True
#end def for GameOver


def GetPlayersName():
    PlayerName = input("What is your name? ")
    return PlayerName
#end def for GetPlayersName()


def CheckIfMoveIsValid(Board, Move, BoardSize):
    Row = Move % 10
    Column = Move // 10
    MoveIsValid = False
    if (Row + Column) <= (BoardSize*2)
        if Board[Row][Column] == " ":
            MoveIsValid = True
        #end if
    #end if
    return MoveIsValid
#end def

def GetPlayerScore(Board, BoardSize, Piece):
    Score = 0
    for Row in range(1, BoardSize + 1):
        for Column in range(1, BoardSize + 1):
            if Board[Row][Column] == Piece:
                Score = Score + 1
            #end if
        #end for (column)
    #end for (row)
    return Score
#end def for GetPlayerScore

def CheckIfThereArePiecesToFlip(Board, BoardSize, StartRow, StartColumn, RowDirection, ColumnDirection):
    RowCount = StartRow + RowDirection
    ColumnCount = StartColumn + ColumnDirection
    FlipStillPossible = True
    FlipFound = False
    OpponentPieceFound = False

    while RowCount <= BoardSize and RowCount >= 1 and ColumnCount >= 1 and ColumnCount <= BoardSize and FlipStillPossible and not FlipFound:
        if Board[RowCount][ColumnCount] == " ":
            FlipStillPossible = False
        elif Board[RowCount][ColumnCount] != Board[StartRow][StartColumn]:
            OpponentPieceFound = True
        elif Board[RowCount][ColumnCount] == Board[StartRow][StartColumn] and not OpponentPieceFound:
            FlipStillPossible = False
        else:
            FlipFound = True
        #end if
        RowCount = RowCount + RowDirection
        ColumnCount = ColumnCount + ColumnDirection
    #end while
    return FlipFound
#end def for CheckIfThereArePiecesToFlip()

def FlipOpponentPiecesInOneDirection(Board, BoardSize, StartRow, StartColumn, RowDirection, ColumnDirection):
    FlipFound = CheckIfThereArePiecesToFlip(Board, BoardSize, StartRow, StartColumn, RowDirection, ColumnDirection)
    if FlipFound:
        RowCount = StartRow + RowDirection
        ColumnCount = StartColumn + ColumnDirection
        while Board[RowCount][ColumnCount] != " " and Board[RowCount][ColumnCount] != Board[StartRow][StartColumn]:
            if Board[RowCount][ColumnCount] == "H":
                Board[RowCount][ColumnCount] = "C"
            else:
                Board[RowCount][ColumnCount] = "H"
            #end if

            RowCount = RowCount + RowDirection
            ColumnCount = ColumnCount + ColumnDirection
        #end while
    #end if
#end def for FlipOpponentPiecesInOneDirection()


def MakeMove(Board, BoardSize, Move, HumanPlayersTurn):
    Row = Move % 10
    Column = Move // 10
    if HumanPlayersTurn:
        Board[Row][Column] = "H"
    else:
        Board[Row][Column] = "C"
    #end if
    FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, 1, 0)
    FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, -1, 0)
    FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, 0, 1)
    FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, 0, -1)
#end def for Make Move()

def PrintLine(BoardSize):
    print("   ", end="")
    for Count in range(1, BoardSize * 2):
        print("_", end="")
    #end for
    print()
#end def for Print Line


def DisplayGameBoard(Board, BoardSize):
    print()
    print("  ", end="")
    for Column in range(1, BoardSize + 1):
        print(" ", end="")
        print(Column, end="")
    #end for
    print()
    PrintLine(BoardSize)
    for Row in range(1, BoardSize + 1):
        print(Row, end="")
        print(" ", end="")
        for Column in range(1, BoardSize + 1):
            print("|", end="")
            print(Board[Row][Column], end="")
        #end for
        print("|")
        PrintLine(BoardSize)
        print()
    #end for
#end def for DiplayGameBoard()

def DisplayMenu():
    print("(p)lay game")
    print("(e)nter name")
    print("(c)hange board size")
    print("(q)uit")
    print()
#end def for DiaplyMenu()

def GetMenuChoice(PlayerName):
    print(PlayerName, "enter the letter of your chosen option: ", end="")
    Choice = input()
    return Choice
#end def for GetMenuChoice()


def CreateBoard(BoardSize):
    Board = []
    for Count in range(BoardSize + 1):
        Board.append([])
        for Count2 in range(BoardSize + 1):
            Board[Count].append("")
        #end for
    #end for
    return Board
#end def for CreateBoard()


def PlayGame(PlayerName, BoardSize):
    Board = CreateBoard(BoardSize)
    SetUpGameBoard(Board, BoardSize)
    HumanPlayersTurn = False
    while not GameOver(Board, BoardSize):
        HumanPlayersTurn = not HumanPlayersTurn
        DisplayGameBoard(Board, BoardSize)
        MoveIsValid = False
        while not MoveIsValid:
            if HumanPlayersTurn:
                Move = GetHumanPlayerMove(PlayerName)
            else:
                Move = GetComputerPlayerMove(BoardSize)
            #end if

            MoveIsValid = CheckIfMoveIsValid(Board, Move, BoardSize)
        #end while
        if not HumanPlayersTurn:
            print("Press the Enter key and the computer will make its move")
            input()
        #end if
        MakeMove(Board, BoardSize, Move, HumanPlayersTurn)
    #end while
    DisplayGameBoard(Board, BoardSize)
    HumanPlayerScore = GetPlayerScore(Board, BoardSize, "H")
    ComputerPlayerScore = GetPlayerScore(Board, BoardSize, "C")
    if HumanPlayerScore > ComputerPlayerScore:
        print("Well done", PlayerName, ", you have won the game!")
    elif HumanPlayerScore == ComputerPlayerScore:
        print("That was a draw!")
    else:
        print("The computer has won the game!")
    #end if
    print()
#end def for PlayGame()

def main():
    random.seed()
    BoardSize = 6
    PlayerName = ""
    Choice = ""
    while Choice != "q":
        DisplayMenu()
        Choice = GetMenuChoice(PlayerName)
        if Choice == "p":
            PlayGame(PlayerName, BoardSize)
        elif Choice == "e":
            PlayerName = GetPlayersName()
        elif Choice == "c":
            BoardSize = ChangeBoardSize()
        #end if
    #end while
#run main()
main()
