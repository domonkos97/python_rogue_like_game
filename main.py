'''
This file defines the game logic (main logic), with it only containing one function. 
At the end of the file, there are ideas for further improvment of the game.
'''
import os
import controller
import ui

height = 15
width = 30


def main():
    '''
    The main function defines the game logic, using functions from UI and the controller.
    '''
    os.system('clear')
    player = controller.create_player()
    os.system('clear')
    board = controller.create_board(height, width)
    ui.display_board(board)
    ui.display_player(player)


if __name__ == '__main__':
    main()


# SUGGESTIONS TO IMPROVE THE GAME:
    # create a database
    # saves usernames, their highest scores (hishest level)
    # need module.py !!
