import random   # used from random coordinate generator.


def main():
    # declare variables
    turns = 0
    win = "noWinner"
    board = [["", "", ""],  # generates initial board
             ["", "", ""],
             ["", "", ""]]

    drawBoard(board)    # draws the board
    while win == "noWinner":   # loops whilst no one has won

        players = ['human', 'computer']

        for player in range(len(players)):  # changes value of player to 'human' then 'computer'

            turns += 1  # totals number of turns

            print players[player], "'s turn"    # prints whos go it is

            x, y = getTurn(board, players, player)   # returns x and y coords of turn

            updateBoard(x, y, board, players, player)  # places counters at coordinates

            print "Board:", board   # displays board
            print ""

            if players[player] == 'human':  # if humans's turn
                win = checkWin(board, "X")  # fetches if won from checkWin func (human)
                if win != "noWinner":   # if either draw or win
                    break   # exit loop
            else:
                win = checkWin(board, "O")  # fetches if won from checkWin func (comp)
                if win != "noWinner":   # if either draw or win
                    break   # exit loop

    if win == "Draw":   # if all spaces full + no 3 in a row
        print "It's a draw!"
    else:
        if win == "Winner": # if a player has won
            print players[player].capitalize(), "has won!"  # displays who's won

    print players[player].capitalize(), "won in", turns, "turns."   # displays how many turns it took


def getTurn(board, players, player):

    if players[player] == "human":
        # human
        spaceFree = False
        while not spaceFree:    # loops until found a free space
            x = getNatural("Enter x coord: ")   # x = valid number from 0 to 2
            y = getNatural("Enter y coord: ")   # y = valid number from 0 to 2
            if not board[x][y] == "-":  # if space is not free
                print("Space is already taken! Try again.")
                print ""
            else:   # there is a space free!
                spaceFree = True
    else:
        # computer
        spaceFree = False
        while not spaceFree:
            x, y = getRandom()  # gets random x, y numbers from 0 to 2
            if board[x][y] == "-":  # if empty
                spaceFree = True

    return x, y


def updateBoard(x, y, board, players, player):

    if players[player] == 'human':  # if human turn
        board[x][y] = "X"   # puts X on player's coordinates
    else:   # if computer turn
        board[x][y] = "O"   # puts O on computer's coordinates


def getNatural(message):
    valid = False
    while not valid:    # while number is not valid
        number = str(input(message))
        if not number.isdigit():    # if number is not a digit
            print('Not a number! Try again')
            print("")
        else:
            if not (0 <= int(number) <= 2): # if number is not between 0 and 2
                print('Not within range 0-2! Try again.')
            else:
                valid = True    # number is valid and can be returned
    return int(number)


def getRandom():    # simple random number generator from 0 to 2
    x = random.randint(0, 2)
    y = random.randint(0, 2)

    return x, y


def checkWin(board, turn):

    win = "noWinner"

    # check for horizontal 3 in a row
    for x in range(0, 3):   # changes value of x from 0 to 2
        counter = 0     # resets counter
        if board[x][0] == turn:     # if first column of x has a specific counter
            counter += 1    # there is a correct counter there, +1 counter
            if board[x][1] == turn:     # if second column of x has a specific counter
                counter += 1    # there is a correct counter there, +1 counter
                if board[x][2] == turn:     # if third column of x has a specific counter
                    counter += 1    # there is a correct counter there, +1 counter
                    win = "Winner"      # there is a winner!

    # check for vertical 3 in a row
    for y in range(0, 3):
        counter = 0
        if board[0][y] == turn:
            counter += 1
            if board[1][y] == turn:
                counter += 1
                if board[2][y] == turn:
                    counter += 1
                    win = "Winner"

    # check for negative diagonal 3 in a row
    counter = 0
    for x in range(0, 3):
        for y in range(0, 3):
            if x + y == 2:
                if board[x][y] == turn:
                    counter += 1
    if counter == 3:
        win = "Winner"

    # check for positive diagonal 3 in a row
    counter = 0
    for x in range(0, 3):
        for y in range(0, 3):
            if x - y == 0:
                if board[x][y] == turn:
                    counter += 1
    if counter == 3:
        win = "Winner"

    checkDraw = True

    for y in range(0, 3):
        for x in range(0, 3):
            if board[x][y] == "-":
                checkDraw = False

    if checkDraw == True:
        win = "Draw"
        print("DRAW")

    return win


def drawBoard(board):
    for y in range(0, 3):
        for x in range(0, 3):
            board[x][y] = "-"   # put a - in every space

main()  # calls main() function to srart the program.
