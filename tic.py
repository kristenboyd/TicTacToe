from __future__ import print_function

board = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7','8','9']
]


def print_grid():
    for i in range(len(board)):
        for j in range(len(board[i])):
                print (board[i][j], end=" | ")
        print ("\n___________")



def init_game():
    print ("Welcome to Tic Tac Toe" + "\n Player One will be 'X'"
    + "\n Player Two will be 'O'")
    start_game()

def start_game():
    playing = True
    while playing == True:
        print_grid()


def p1 ():
    player_1 = ("Player One")
    print (player_1 + "Enter a position from 1-9")
    marks(player_choice)

def p2():
    player_1 = ("Player One")
    print (player_1 + "Enter a position from 1-9")
    marks(player_choice)

def marks(player_choice):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print (board[i][j])

            if (board[i][j]) == (player_choice):
                board[i][j] = ('o')







init_game()
