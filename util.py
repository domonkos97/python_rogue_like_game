'''
Util is for additional functions that are likely to be used by functions 
in the controll file, such as a random genertor or key pressing, clear screen etc.
'''

import sys


def key_pressed():
    '''
    Detects keyboard inputs
    '''
    try:
        import tty
        import termios
    except ImportError:
        try:
            # probably Windows
            import msvcrt
        except ImportError:
            # FIXME what to do on other platforms?
            raise ImportError('getch not available')
        else:
            key = msvcrt.getch().decode('utf-8')
            return key
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def movement(key):
    if key == 'a':
        print('you pressed a')


def clear_screen():
    pass


def key_press():
    pass
