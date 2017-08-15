from __future__ import print_function

board = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7','8','9']
]



def print_intro():
    "Use the board to choose you position number, \nyou can only choose numbers 1-9"

def print_grid():
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
    playerturn  = 1
    while running:
        if playerturn == 1:
            postion = get_position(playerturn)
            print (position)
            mark_position(playerturn,input)
            print_grid()

            running = False
    print ("game over")

def mark_position(playerturn, input):
    if playerturn == 1:
        board[get_row_index(input)][get_colum_index(input)] = 'X'
    else:
        board[get_row_index(input)][get_colum_index(input)] = 'O'

    return False
'''

    if board[input] == 1:
         board[1]= 'x'
    else:
            print ("This position is taken, please choose a different spot"):

# def marks(player_choice):
    # for i in range(len(board)):
        # for j in range(len(board[i])):
           # print (board[i][j])

            #if (board[i][j]) == ():
                # board[i][j] = ('o')
'''


init_game()
start_game()
