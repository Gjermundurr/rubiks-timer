import time
import sys
from scramble import scramble
import termios
import tty
import select


def getch():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        r, _, _ = select.select([sys.stdin], [], [], 0)
        if r:
            return sys.stdin.read(1)
        return None
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
def display():
    
    print('cstimer by jerry\n')
    print(f'Scramble: {scramble(20)}')
    #sys.stdout.write('press space to start')


def main():
    x = 0
    solving_cube = False
    while True:

        display()
    
        sys.stdout.write(f'\rprocessing... {x}')
        sys.stdout.flush()
        start_key = input('press space to start')
        key = getch()
        if start_key != ' ':
            continue
        solving = True
        x = 0
        while solving:
            sys.stdout.write(f'\rTimer: {x}')

            if key == 'q':
                print() 
                break
            x += 1


if __name__ == '__main__':
    main()
