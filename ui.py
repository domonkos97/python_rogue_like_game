'''
The view(UI) file is to print out the game onto the terminal
and potentially for pygame.
'''
import controller


def display_board(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()


def display_player(player):
    for k, v in player.items():
        print(f"{k}: {v}")
