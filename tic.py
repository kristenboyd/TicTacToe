from __future__ import print_function

board = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7','8','9']
]


def draw():
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print()
        
def print_grid():
    for i in range(len(board)):
        for j in range(len(board[i])):
                print (board[i][j], end=" | ")
        print ("\n___________")


def init_game():
    print ("Welcome to Tic Tac Toe" + "\n Player One will be 'X'"
    + "\n Player Two will be 'O'")

    Player1 = raw_input("Enter in a position from 1-9  ")
    type(Player1)
    Player2 = raw_input("Enter in a position from 1-9  ")
    type(Player2)
    print_grid()

init_game()
