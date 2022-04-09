'''
The conroll file(system) is storing all the functions that run in the background 
to make the game possible.
Such functions as: creating a player, creating the board etc, enemies,
the inventory etc
'''


height = 10
width = 10


def create_board(height=15, width=30):

    import random
    # height/width edges included
    height, width = height+2, width+2

    # create empty board
    board = []
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

    # random generate walls
    for i in range(100):
        random_x = random.randint(1, width-2)
        random_y = random.randint(1, height-2)
        for row_ind, row in enumerate(board):
            for cell_ind, cell in enumerate(row):
                if row_ind == random_y and cell_ind == random_x:
                    row[cell_ind] = 'o'
    return board


def create_player():

    print('''
    1: Captain Jack Sparrow
    2: Rei Ayanami
    3: Moon Knight
    ''')
    avatar = input("Choose an avatar! ")

    while True:
        if avatar not in "123" or len(avatar) > 1:
            print("ERROR")
            avatar = input("Choose an avatar! ")
        else:
            if avatar == "1":
                name = "Captain Jack Sparrow"
                gender = "Male"
                HP = 100
            elif avatar == "2":
                name = "Rei Ayanami"
                gender = "Female"
                HP = 115
            elif avatar == "3":
                name = "Moon Knight"
                gender = "Male"
                HP = 75
            break
    player = {"Avatar": name, "Gender": gender, "HP": HP}
    return player


def create_inventory():
    pass
