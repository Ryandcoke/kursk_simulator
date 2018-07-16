from enum import Enum

class MenuType(Enum):
    """
    Used for MenuFactory, which will probably not be used.
    """
    INVALID  = 0
    MAIN     = 1
    STARTUP  = 2
    GAME     = 3

class Menu(object):
    """
    Prompts the user for input.
    Depending on the reponse, the menu will either reprompt or exit
    and return some value based on the response.
    """
    def __init__(self):
        self.main_prompt = self.create_prompts()
        self.valid_responses = self.create_responses()

    def start(self):
        """
        Initialize the menu

        Returns:
            the next menu to go to
            or None if the program is to be exited
        """
        current_prompt = self.main_prompt
        while current_prompt:
            # returning a None prompt exits the prompt loop and this
            # specific menu.
            current_prompt = self.get_user_input(current_prompt)

    def get_user_input(self, prompt=""):
        """
        Parameters:
            String prompt:  to the user that is printed to standard output
                            without a trailing newline before reading input.

        Returns:
            String prompt:  to specify the next string to prompt to the user
                            or None if the prompt loop is over.
        """
        response = input(prompt)
        if response in self.valid_responses:
            pass  # TODO
        else:
            pass  # TODO


class MainMenu(object):
    """
    The main menu that will let the user:
      - Start a new game
      - Learn more about the program
      - Exit the program
    """
    class __MainMenu(Menu):
        """
        Singleton nested class to prevent multiple instances of MainMenu
        """
        def __init__(self):
            pass

    instance = None
    def __init__(self):
        """
        If Singleton instance not created yet, create it and return it.
        Else, return the already created instance to avoid duplicate instances.
        """
        if not MainMenu.instance:
            MainMenu.instance = MainMenu.__init__(self)


class MenuFactory(object):
    """
    Creates menus.

    Is this excessive?              Yes.
    Do I care?                      No.
    Am I going to do it anyways?    Maybe.

    FeelsCorporateJavaDeveloperMan

    Since all menus are Singletons, this may be unneccesary to implement,
    or extremely easy.
    """
    @staticmethod
    def get_menu(name):
        """
        Creates a menu of a specified type.
        """
        pass


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
"""
