import random
import curses
from curses import wrapper



def main(stdscr):
    # Clear screen
    stdscr.clear()

    s = curses.initscr()
    curses.curs_set(False) ## remove blinking cursor
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)


    #sh, sw = s.getmaxyx()
    sh, sw = 100, 100 ## nice squared window

    w = curses.newwin(sh, sw, 0, 0) ## height, width, begin_y, begin_x


    w.keypad(True)
    w.timeout(100)

    snk_x, snk_y = sw//4, sh//4

    snake = [ [snk_y, snk_x], ## body
            [snk_y, snk_x-1],
            [snk_y, snk_x-2]
            ] 

    #food = [sh//2, sh//2]
    a, b = random.randint(1, sh-1), random.randint(1, sw-1)
    food = [a,b]
    w.addch(food[0], food[1],  curses.ACS_PI)

    key = curses.KEY_RIGHT

    while True:
        next_key = w.getch()
        key =  key if next_key == -1 else next_key

        if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
            curses.endwin()
            quit()
        
        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        
        if key == curses.KEY_UP:
            new_head[0] -= 1

        if key == curses.KEY_LEFT:
            new_head[1] -= 1

        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        if snake[0] == food:
            food = None
            while food is None:
                a, b = random.randint(1, sh-1), random.randint(1, sw-1)
                nf = [a, b ] ## new food
                food = nf if nf not in snake else None

            w.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], '#')

        w.addch(snake[0][0], snake[0][1], curses.ACS_PLMINUS)
    


if __name__ == '__main__':
    wrapper(main)