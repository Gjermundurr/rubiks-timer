import re
import curses
import time
from scramble import scramble
from random import randint


def get_algorithm(alg_list: list):
    return alg_list[randint(0, len(alg_list)-1)]

def main(stdscr):
    
    rubiks_file = './rubiks.txt'
    rubiks_txt = open(rubiks_file, 'r').read()
    algorithms = re.findall('.+:.+', rubiks_txt)

    win_height = 100
    win_width = 100
    begin_x = 5
    begin_y = 5
    win = curses.newwin(win_height, win_width, begin_y, begin_x)
    win.nodelay(True)
    win.timeout(100)

    # X = Horizontal, Y = Vertical

    pos_x_header = 3
    pos_y_header = 3
    pos_x_scramble = 3
    pos_y_scramble = 6
    pos_x_aofive = 3
    pos_y_aofive = 12
    pos_x_aotwelve = 3
    pos_y_aotwelve = 13
    pos_x_timer = 3
    pos_y_timer = 9
    mins = 0.0
    secs = 0.0
    ao_counter = 0
    aofive = [0.0] * 5
    aotwelve = [0.0] * 12 
    aofive_avg = sum(aofive) / 5
    aotwelve_avg = sum(aotwelve) / 12

    running = False
    next_alg = '' 
    while True:
        
        win.clear()
        win.addstr(pos_y_header, pos_x_header, "cspractice by jerry")
        win.addstr(pos_y_scramble, pos_x_scramble, f"{next_alg}")
        
        timer_display =  f"{secs:1.2f}"
        if mins > 1.0:
            timer_display =  f"{mins:1.0f}:{timer_display}"
        win.addstr(pos_y_timer, pos_x_timer, timer_display)
        
        win.addstr(pos_y_aofive, pos_x_aofive, f"ao5: {aofive_avg:.2f}")
        win.addstr(pos_y_aotwelve, pos_x_aotwelve, f"ao12: {aotwelve_avg:.2f}")
        win.refresh()
        curses.napms(10)
        
        key = win.getch()

        if  not running and key == ord(' '):
            running = True
            start_time = time.time()
            key = None

        if running:
            elapsed_time = time.time() - start_time
            mins, secs = divmod(elapsed_time, 60)

        if running and key == ord(' '):
            running = False

            next_alg = get_algorithm(algorithms)
            i_five = ao_counter % 4
            i_twelve = ao_counter % 11
            aofive[i_five] = elapsed_time
            aotwelve[i_twelve] = elapsed_time
            aofive_avg = sum(aofive) / 5
            aotwelve_avg = sum(aotwelve) / 12
            ao_counter += 1

        if key == ord('n'):
            next_alg = get_algorithm(algorithms)

        if key == ord('q'):
            break




if __name__ == '__main__':
    curses.wrapper(main)
