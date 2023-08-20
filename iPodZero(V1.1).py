# Designing a Python UI for the iPodZero Project
# Features include: scrolling with clickwheel, option select, mp3 music playback, bluetooth(maybe)
# Version 1.1

import curses

# Define the options
options = ["Music", "Shuffle", "About"]
current_option = 0

def update_option(direction):
    global current_option
    current_option = (current_option + direction) % len(options)

def update_ui(stdscr):
    stdscr.clear()
    for idx, option in enumerate(options):
        if idx == current_option:
            stdscr.addstr(idx, 0, option, curses.color_pair(1))
        else:
            stdscr.addstr(idx, 0, option, curses.color_pair(0))
    stdscr.refresh()

def main(stdscr):
    # Initialize curses settings
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)

    while True:
        update_ui(stdscr)
        key = stdscr.getch()

        if key == curses.KEY_UP:
            update_option(-1)  # Scroll up
        elif key == curses.KEY_DOWN:
            update_option(1)  # Scroll down

if __name__ == "__main__":
    curses.wrapper(main)
