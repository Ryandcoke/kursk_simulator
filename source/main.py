from menus import MainMenu


def main():
    """
    Runs the menu loop until the program exits
    """
    # Start off in the main menu
    current_menu = MainMenu()
    while current_menu is not None:
        current_menu = current_menu.start()


# Initialize the program
main()
