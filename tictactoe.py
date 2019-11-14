def move(board, location, player):
    x, y = location
    valid = False
    if len(board) != 3 or len(board[0]) != 3:
        print("invalid board, try again")
        return [['', '', ''], ['', '', ''], ['', '', '']], valid
    if not (player == 'X' or player =='O'):
        print("invalid player! try again")
    elif (x < 0 or x > 2) or (y < 0 or y > 2):
        print("invalid coordinates! try again!")
    elif board[x][y] == 'X' or board[x][y] =='O':
        print("somebody already moved there! try again!")
    else:
        board[x][y] = player
        valid = True
    return board, valid

def tictactoewin(board, player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    for i in range(2):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    return False

def printboard(board):
    print("  [ 1    2    3 ]")
    for x in range(3):
        print(str(x+1) + " " + str(board[x]))


def tictactoe():
    play = True
    while play:
        x_win = False
        o_win = False
        moves = 0
        turn = "X"
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        print("LETS PLAY TIC TAC TOE!!!!")
                
        while not x_win and not o_win and moves < 9:
            printboard(board)
            print(f"player {turn}, its your turn! where do you wanna go? ")
            valid = False
            
            while not valid:
                x = int(input("what row would you like to move? ")) - 1
                y = int(input("what column would you like to move? ")) - 1 
                board, valid = move(board,(x,y), turn)
                           
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            
            x_win = tictactoewin(board, "X")
            o_win = tictactoewin(board, "O")
            moves += 1
        
        printboard(board)
        if x_win:
            print("X wins! good job!")
        elif o_win:
            print("O wins! good job!")
        else:
            print("Its a tie?!?")
        play = input("would you like to play again? ('YES' to continue)") == "YES"
    print("Thanks for playing!")

tictactoe()