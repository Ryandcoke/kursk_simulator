from menus import MainMenu


def main():
    """
    Runs the menu loop until the program exits
    During the loop, the  user can swap between menus
        - main
        - startup
        - game
    """
    # Start off in the main menu
    current_menu = MainMenu()
    while current_menu is not None:
        current_menu = current_menu.start()


# Initialize the program
if __name__ == "__main__":
    # main.py must be ran directly to start program
    main()
else:
    print("Do not import __main__.py from other modules.")
