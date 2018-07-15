class Menu(object):
    """
    Prompts the user for input.
    Depending on the reponse, the menu will either reprompt or exit
    and return some value based on the response.
    """
    def __init__(self, main_prompt, valid_responses):
        self.main_prompt = main_prompt
        self.valid_responses = valid_responses

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


class MenuFactory(object):
    """
    Creates menus
    """
    @staticmethod
    def get_menu(name):
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
