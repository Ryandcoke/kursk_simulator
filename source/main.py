

class Menu(object):
    """
    Prompts the user for input.
    Depending on the reponse, the menu will either reprompt or exit
    and return some value based on the response.
    """
    main_prompt = ""
    valid_responses = {}
    in_menu = True

    def __init__(self, main_prompt):
        self.main_prompt = main_prompt

    def start():
        """
        Initialize the menu
        """
        current_prompt = main_prompt
        while current_prompt:
            current_prompt = get_user_input(current_prompt)


class MenuFactory(object):
    """
    Creates menus
    """
    @staticmethod
    def get_menu(name):
        pass


def initialize_main_menu():
    """
    Prompt the user with the main menu options and get user input
    """


             _  __              _          
            | |/ /             | |         
            | ' /_   _ _ __ ___| | __      
            |  <| | | | '__/ __| |/ /      
            | . \ |_| | |  \__ \   <       
            |_|\_\__,_|_|  |___/_|\_\      
     _____ _                 _       _
    / ____(_)               | |     | |
   | (___  _ _ __ ___  _   _| | __ _| |_ ___  _ __
    \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
    ____) | | | | | | | |_| | | (_| | || (_) | |
   |_____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|
                            __  ___  _  _  ____  
                           /_ |/ _ \| || ||___ \ 
                            | | (_) | || |_ __) |
                            | |\__, |__   _|__ < 
                            | |  / /   | | ___) |
                            |_| /_/    |_||____/ 



def main():
    """
    Initialize the program
    """
    # Start off in the main menu
    current_menu = MainMenu
    while current_menu is not None:
        current_menu = current_menu.start()


main()
