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

        print ("Welcome to Tic Tac Toe" + "\n Player One will be 'x'" + "\n Player Two will be 'o'")
        
while True: 
    input = raw_input("Selcet a position")
    input = int(input)
    
    if board[input] != 'x' and board[input] != 'o':
        board[input]= 'x'
        
    else: 
        print ("This position is taken, please choose a different spot")



# def marks(player_choice):
    # for i in range(len(board)):
        # for j in range(len(board[i])):
           # print (board[i][j])

            #if (board[i][j]) == (player_choice):
                # board[i][j] = ('o')







init_game()
