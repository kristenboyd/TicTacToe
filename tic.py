from __future__ import print_function

board = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7','8','9']
]



def print_grid():
    "Use the board to choose you position number, \nyou can only choose numbers 1-9"
    for i in range(len(board)):
        for j in range(len(board[i])):
                print (board[i][j], end=" | ")
        print ("\n___________")



def init_game():
    player1 = input("Enter Player One\'s name: ")
    player2 = input("Enter Player Two\'s name: ")
    print(player1 + " will be 'X'" + "\n" + player2 + " will be 'O'")



def get_position(playerturn):
    input = raw_input("player " + str(playerturn) + " Selcet a position ")
    input = int(input)
    if(valid_input(input)):
        return input
    else:
        print ("invalid input")
        get_position(playerturn)

def valid_input(input):
    if (((input) >= 1 and (input) <= 9) == False) or board[get_row_index(input)][get_colum_index(input)] == 'X' or board[get_row_index(input)][get_colum_index(input)] == 'O':
        return False
    else:
        return True

def get_row_index(input):

    if input == 1:
        return 0
    if input == 2:
        return 0
    if input == 3:
        return 0
    if input == 4:
        return 1
    if input == 5:
        return 1
    if input == 6:
        return 1
    if input == 7:
        return 2
    if input == 8:
        return 2
    if input == 9:
        return 2


def get_colum_index(input):

    if input == 1:
        return 0
    if input == 2:
        return 1
    if input == 3:
        return 2
    if input == 4:
        return 0
    if input == 5:
        return 1
    if input == 6:
        return 2
    if input == 7:
        return 0
    if input == 8:
        return 1
    if input == 9:
        return 2



def start_game():
    running = True
    playerturn = 1
    while running:
        if playerturn == 1:
            position = get_position(playerturn)
            mark_position(playerturn,position)

            print_grid()
            playerturn = 2
            win_combos(playerturn)
        else:
            position = get_position(playerturn)
            mark_position(playerturn,position)

            print_grid()
            playerturn = 1
            win_combos(playerturn)

def mark_position(playerturn, input):
    if playerturn == 1:
        board[get_row_index(input)][get_colum_index(input)] = 'X'
    else:
        board[get_row_index(input)][get_colum_index(input)] = 'O'
    return False



def win_combos(playerturn):
    print ("Win Combos")
    if playerturn == 1:
        print("Checking Player1")
        if check_index('X'):
            print ("Player One Wins!")
    else:
        if check_index('O'):
            print ("Player Two Wins!")
                     

'''
    elif playerturn == 2:
        if board[0][0] == '0' and board[0][1] == '0' and board[0][2] == '0':
            print ("Player Two Wins!")
    else:
        Print("No Winner")                
'''


def check_index(Marker):
    print("In check Index")
  
    if board[0][0] == Marker and board[0][1] == Marker and board[0][2] == Marker:
        return True

    elif board[1][0] == Marker and board[1][1] == Marker and board[1][2] == Marker:
        return True

    elif board[2][0] == Marker and board[2][1] == Marker and board[2][2] == Marker:
        return True
               
    elif board[0][0] == Marker and board[1][0] == Marker and board[2][0] == Marker:
        return True

    elif board[0][1] == Marker and board[1][1] == Marker and board[2][1] == Marker:
        return True
        
    elif board[0][2] == Marker and board[1][2] == Marker and board[2][2] == Marker:
        return True
        
    elif board[0][0] == Marker and board[1][1] == Marker and board[2][2] == Marker:
        return True

    elif board[0][2] == Marker and board[1][1] == Marker and board[2][0] == Marker:
        return True
        
    else:
        return False 





'''
    board = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7','8','9']
    ]

[3,5,7] 147][258][369]
    Diagonal = 159, 357
    Vertical = 147, 258, 369
    Horizontal = 123, 456, 789

'''


init_game()
start_game()
