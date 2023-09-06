// TUI-C is a Terminal UI made in C, just like the name!
// intended for easy setup, just run the file in a C editor
// if on Linux (make sure ncurses is installed), use: gcc -o TUI-C TUI-C.c -lncurses
// to run on linux do: ./TUI-C

#include <ncurses.h>
#include <stdlib.h>

int main() {
    // Initialize ncurses
    initscr();
    cbreak();
    noecho();
    keypad(stdscr, TRUE);

    // Create a window for the main content
    WINDOW *mainwin = newwin(320, 240, 2, 2);

    // Define menu items
    // You can customize these
    char *menu_items[] = {
        "Music                                                  ",
        "Shuffle                                                ",
        "Bluetooth                                              ",
        "About                                                  ",
        "Shutdown                                               "
    };

    int num_items = sizeof(menu_items) / sizeof(menu_items[0]);
    int current_item = 0;

    while (1) {
        // Clear the main window
        werase(mainwin);

        // Print the menu items
        for (int i = 0; i < num_items; i++) {
            if (i == current_item) {
                wattron(mainwin, A_REVERSE);
            }
            mvwprintw(mainwin, i, 0, menu_items[i]);
            wattroff(mainwin, A_REVERSE);
        }

        // Refresh the main window
        wrefresh(mainwin);

        // Get user input
        int choice = getch();

        switch (choice) {
            case KEY_UP:
                if (current_item > 0) {
                    current_item--;
                }
                break;
            case KEY_DOWN:
                if (current_item < num_items - 1) {
                    current_item++;
                }
                break;
            case 10: // Enter key
                // You can add logic to perform actions based on the selected menu item
                if (current_item = 5) {
                    system("sudo shutdown now");
                }
                break;
            default:
                break;
        }

        // Exit the loop when 'q' is pressed
        if (choice == 'q') {
            break;
        }
    }

    // Clean up and exit
    delwin(mainwin);
    endwin();
    refresh();

    return 0;
}
