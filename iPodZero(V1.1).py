# Designing a Python UI for the iPodZero Project
# Features include: scrolling with clickwheel, option select, mp3 music playback, bluetooth(maybe)
# Version 1.4

import curses
import RPi.GPIO as GPIO

# Define the GPIO pins
CW_SCL_PIN = 23
CW_SDA_PIN = 5

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
    # Initialize GPIO settings
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(CW_SCL_PIN, GPIO.IN)
    GPIO.setup(CW_SDA_PIN, GPIO.IN)

    # Initialize the rotary encoder state
    prev_clk_state = GPIO.input(CW_SCL_PIN)
    prev_dt_state = GPIO.input(CW_SDA_PIN)

    # Initialize curses settings
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)

    while True:
        update_ui(stdscr)

        # Read the current state of the rotary encoder
        clk_state = GPIO.input(CW_SCL_PIN)
        dt_state = GPIO.input(CW_SDA_PIN)

        # Determine the direction of rotation
        if clk_state != prev_clk_state:
            if dt_state != clk_state:
                update_option(1)  # Scroll down
            else:
                update_option(-1)  # Scroll up

        prev_clk_state = clk_state
        prev_dt_state = dt_state

        key = stdscr.getch()

        if key == ord("q"):
            break

    GPIO.cleanup()  # Clean up GPIO pins on exit

if __name__ == "__main__":
    curses.wrapper(main)
