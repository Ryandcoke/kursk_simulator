"""
Contains all menu related classes. Menus prompt the user from standard output
(console) and get the user input from standard input (console).
Depending on the user response, the response is processed and the appropriate
actions are taken to navigate through the program.
"""


from util import Singleton


class Menu(metaclass=Singleton):
    """
    Prompts the user for input.
    Depending on the reponse, the menu will either reprompt or exit
    and return some value based on the response.

    This is an abstract singleton class. Do not instantiate.
    """

    def __init__(self):
        self.main_prompt = ""
        self.valid_responses = {}
        self.create_prompts()
        self.create_responses()

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

    def get_user_input(self, prompt):
        """
        Parameters:
            String prompt:  to the user that is printed to standard output
                            without a trailing newline before reading input.

        Returns:
            String prompt:  to specify the next string to prompt to the user
                            or None if the prompt loop is over.
        """
        response = input(prompt + self.cursor_prompt)
        if response in self.valid_responses.keys():
            # Call function value in self.valid_responses dictionary
            self.valid_responses.get(response)()
        else:
            # Prompt use that an invalid response was issued
            self.prompt_invalid_response(response)

        return prompt

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
        raise NotImplementedError("Has not been implemented.")


class MainMenu(Menu):
    """
    The main menu that will let the user:
        - Start a new game
        - Learn more about the program
        - Exit the program
    """

    cursor_prompt = "\n\n> "  # This is appended to the end of every prompt

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


    def create_responses(self):
        def start():
            # TODO
            print("start")

        def about():
            # TODO
            print("about")

        def quit():
            # TODO
            print("Bye")
            exit()

        self.valid_responses = {
            "1": start,
            "2": about,
            "3": quit
        }

    instance = None  # singletone instance

    def __init__(self):
        """
        If Singleton instance not created yet, create it and return it.
        Else, return the already created instance to avoid duplicate instances.
        """
        super().__init__()
        # if not MainMenu.instance:
        #     MainMenu.instance = MainMenu.__MainMenu()
