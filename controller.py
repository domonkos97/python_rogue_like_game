'''
The conroll file(system) is storing all the functions that run in the background 
to make the game possible.
Such functions as: creating a player, creating the board etc, enemies,
the inventory etc
'''

height = 10
width = 10


def create_board(height=15, width=30):
    # height/width edges included
    height, width = height+2, width+2

    # create empty board
    board = []
    cell = ""
    for row_ind in range(height):
        row = []
        board.append(row)
        for cell_ind in range(width):
            cell = " "
            board[row_ind].append(cell)

    # create walls around it
    for row_ind, row in enumerate(board):
        for cell_ind, cell in enumerate(row):
            if row_ind == 0 or row_ind == height-1:
                row[cell_ind] = 'X'

            if cell_ind == 0 or cell_ind == width-1:
                row[cell_ind] = 'X'
    return board
    # random generate walls


create_board(height, width)
