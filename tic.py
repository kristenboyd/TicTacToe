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

    if input == 1:
        board[1] = 'X'
        print_grid()



    if(valid_input(input)):
        return input






def start_game():
    running = True
    playerturn  = 1
    while running:
        if playerturn == 1:
            postion = get_position(playerturn)
            running = False
    print ("game over")

'''
# def marks(player_choice):
    # for i in range(len(board)):
        # for j in range(len(board[i])):
           # print (board[i][j])

            #if (board[i][j]) == ():
                # board[i][j] = ('o')
'''


init_game()
start_game()
