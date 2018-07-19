"""
Contains all menu related classes. Menus prompt the user from standard output
(console) and get the user input from standard input (console).
Depending on the user response, the response is processed and the appropriate
actions are taken to navigate through the program.
"""


from textwrap import fill
from util import Singleton, print_wrap


class Menu(metaclass=Singleton):
    """
    Prompts the user for input.
    Depending on the reponse, the menu will either reprompt or exit
    and return some value based on the response.

    This is an abstract singleton class. Do not instantiate.
    """

    cursor_prompt = "\n\n> "  # This is appended to the end of every prompt

    def __init__(self):
        self.main_prompt = ""
        self.prompt = ""
        self.valid_responses = {}
        self.next_menu = None
        self.create_prompts()
        self.create_responses()

    def start(self):
        """
        Initialize the menu

        Returns:
            the next menu to go to
            or None if the program is to be exited
        """
        self.prompt = self.main_prompt
        while self.prompt:
            # returning a None prompt exits the prompt loop and this
            # specific menu.
            self.get_user_input()

        return self.next_menu

    def get_user_input(self):
        """
        Parameters:
            String prompt:  to the user that is printed to standard output
                            without a trailing newline before reading input.

        Returns:
            String prompt:  to specify the next string to prompt to the user
                            or None if the prompt loop is over.
        """
        response = input(self.prompt + self.cursor_prompt)
        if response in self.valid_responses.keys():
            # Call function value in self.valid_responses dictionary
            self.valid_responses.get(response)()
        else:
            # Prompt use that an invalid response was issued
            self.prompt_invalid_response(response)

    def create_prompts(self):
        """
        This is to be implemented by children classes
        """
        raise NotImplementedError("Has not been implemented.")

    def create_responses(self):
        """
        Creates a dictionary of all valid responses.

        self.valid_responses
            keys    String      valid responses
            values  Function    what the menu does when those response are
                                issued
        """
        raise NotImplementedError("Has not been implemented.")

    def prompt_invalid_response(self, response):
        """
        Prompts that the user has issued an invalid response.
        """
        message = "Please enter one of the following: " + str(list(self.valid_responses.keys()))
        self.prompt = self.main_prompt + "\n" + message


class MainMenu(Menu):
    """
    The main menu that will let the user:
        - Start a new game
        - Learn more about the program
        - Exit the program
    """

    def create_prompts(self):
            self.main_prompt = """
                _  __              _
               | |/ /             | |
               | ' /_   _ _ __ ___| | __
               |  <| | | | '__/ __| |/ /
               | . \\ |_| | |  \\__ \\   <
               |_|\\_\\__,_|_|  |___/_|\\_\\
        _____ _                 _       _
       / ____(_)               | |     | |
      | (___  _ _ __ ___  _   _| | __ _| |_ ___  _ __
       \\___ \\| | '_ ` _ \\| | | | |/ _` | __/ _ \\| '__|
       ____) | | | | | | | |_| | | (_| | || (_) | |
      |_____/|_|_| |_| |_|\\__,_|_|\\__,_|\\__\\___/|_|
                               __  ___  _  _  ____
                              /_ |/ _ \\| || ||___ \\
                               | | (_) | || |_ __) |
                               | |\\__, |__   _|__ <
                               | |  / /   | | ___) |
                               |_| /_/    |_||____/

    1. Start        2. About Kursk Simulator        3. Quit
"""

            about_message = fill("Kursk Simulator: 1943 is a tank gunnery simulator built in Python. Tank armour layouts and weapon penetration are modeled based on historical data collected by the Allied governments after WWII. *Kursk Simulator* models the overmatch mechanics (the interactions between weapons and armour that determine the penetration, or non-penetration of a shell through armour) of tank gunnery, with a simplified and stylized model based on elementary physics.", 79)
            self.about_prompt = self.main_prompt + "\n" + about_message


    def create_responses(self):
        def go_to_start_menu():
            self.prompt = None
            self.next_menu = StartMenu()

        def about():
            self.prompt = self.about_prompt

        def quit():
            print("Bye!")
            exit()

        self.valid_responses = {
            "1": go_to_start_menu,
            "2": about,
            "3": quit
        }


class StartMenu(Menu):
    """
    The start menu lets the user configure the game to how they want.
    The user can choose what tanks to use and what ammo they carry.
    """

    def create_prompts(self):
        self.main_prompt = """
        TODO: start menu main prompt

        2. Return to main menu
        """

    def create_responses(self):
        def go_to_main_menu():
            self.prompt = None
            self.next_menu = MainMenu()

        self.valid_responses = {
            "2": go_to_main_menu
        }
