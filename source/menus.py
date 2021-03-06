"""
Contains all menu related classes. Menus prompt the user from standard output
(console) and get the user input from standard input (console).
Depending on the user response, the response is processed and the appropriate
actions are taken to navigate through the program.
"""


from typing import Callable, Dict
from util import Singleton, wrap
from text import Color, Style, color, style, modify


class Menu:
    """
    Prompts the user for input.
    Depending on the reponse, the menu will either reprompt or exit
    and return some value based on the response.

    This is an abstract singleton class. Do not instantiate.
    All subclasses must implement create_prompts() and create_responses().
    """

    cursor_prompt = "\n\n> "  # This is appended to the end of every prompt

    __metaclass__ = Singleton

    def __init__(self):
        self.main_prompt = str
        self.prompt = ""
        self.valid_responses = Dict[str, Callable]
        self.next_menu = None
        self.create_prompts()
        self.create_responses()

    def start(self) -> 'Menu':
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

    def get_user_input(self) -> None:
        """
        Parameters:
            String prompt:  to the user that is printed to standard output
                            without a trailing newline before reading input.

        Returns:
            void:           However, it modifies self.prompt which allows
                            the user to exit the prompt loop in start().
        """
        response = input(self.prompt + self.cursor_prompt)
        if response in self.valid_responses.keys():
            # Call function value in self.valid_responses dictionary
            self.valid_responses.get(response)()
        elif self.matches_range(response):
            self.evaluate(response)
        else:
            # Prompt use that an invalid response was issued
            self.prompt_invalid_response(response)

    def create_prompts(self) -> None:
        """
        This is to be implemented by children classes
        """
        raise NotImplementedError("Subclass must implement this method.")

    def create_responses(self) -> None:
        """
        Creates a dictionary of all valid responses.

        self.valid_responses
            keys    String      valid responses
            values  Function    what the menu does when those response are
                                issued
        """
        raise NotImplementedError("Subclass must implement this method.")

    def matches_range(self, response: str) -> bool:
        """
        If the user response does not match a specifc value in the
        self.valid_responses dictionary, then check that it is contained
        within a certain range of values.

        Parameters:
            String response

        Returns:
            boolean True if response matches range
        """
        return False

    def evaluate(self, response: str) -> None:
        """
        If the user input matches the desired range, then evaluate it here.
        This is a special case where the user input is not to be evaluated by
        calling the response function in self.valid_responses.

        Parameters:
            String response

        Returns:
            void
        """
        raise NotImplementedError("Has not been implemented.")

    def prompt_invalid_response(self, response: str) -> None:
        """
        Prompts that the user has issued an invalid response.
        By default, this lists the possible response options to the user.
        """
        options = ""
        response_keys = list(self.valid_responses.keys())
        if len(response_keys) > 1:
            for i in range(len(response_keys) - 1):
                options += color(response_keys[i], Color.CYAN) + color(", ", Color.RED)
            options += color("or ", Color.RED) + color(response_keys[len(response_keys) - 1], Color.CYAN)
        else:
            options = color(response_keys[0], Color.CYAN)
        message = color("Please choose ", Color.RED) + options + color(".", Color.RED)

        self.prompt = self.main_prompt + "\n" + message


class MainMenu(Menu):
    """
    The main menu that will let the user:
        - Start a new game
        - Learn more about the program
        - Exit the program

    It is the first menu that the user interacts with when the program starts.
    """

    def create_prompts(self) -> None:
        self.main_prompt = modify("""
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

""", Color.YELLOW, Style.BOLD) + \
        "    " + color("1. ", Color.CYAN) + \
        modify("Start", Color.YELLOW, Style.UNDERLINE) + "        " + \
        color("2. ", Color.CYAN) + \
        modify("About Kursk Simulator", Color.YELLOW, Style.UNDERLINE) + "        " + \
        color("3. ", Color.CYAN) + modify("Quit", Color.YELLOW, Style.UNDERLINE) + "\n"

        about_message = wrap("""
Kursk Simulator: 1943 is a tank gunnery simulator built in Python. Tank armour
layouts and weapon penetration are modeled based on historical data collected
by the Allied governments after WWII. Kursk Simulator models the overmatch
mechanics (the interactions between weapons and armour that determine the
penetration, or non-penetration of a shell through armour) of tank gunnery,
with a simplified and stylized model based on elementary physics.
""")
        self.about_prompt = self.main_prompt + "\n" + about_message

    def create_responses(self) -> None:
        def go_to_start_menu():
            self.prompt = None
            self.next_menu = SelectTankMenu()

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


class SelectTankMenu(Menu):
    """
    The user is prompted with a selection of tanks they can choose from and
    get information about each tank.
    """

    def create_prompts(self) -> None:
        self.main_prompt = """
TODO: This is just for debugging stuff.

Select a tank or learn more about it.

Debug tank
1. Choose
2. About

m. Return to main menu
"""

        self.about_debug_prompt = "Debug tank description"

    def create_responses(self) -> None:
        def go_to_main_menu():
            self.prompt = None
            self.next_menu = MainMenu()

        def about_debug():
            self.prompt = self.main_prompt + "\n" + self.about_debug_prompt

        self.valid_responses = {
            "2": about_debug,
            "m": go_to_main_menu
        }


class GameMenu(Menu):
    """
    General game menu.

    Allows gives the option to restart, or return to main menu.
    """

    def create_responses(self) -> None:
        # TODO
        # Figure out how children will add to these responses
        def go_to_main_menu():
            self.prompt = None
            self.next_menu = MainMenu()

        def restart():
            # TODO
            # this need to set the valid locations, health and ammo racks
            # to their default states before the game started.
            # This means that these values need to be saved before the
            # game starts so they can be retrieved.
            pass


class GameMoveMenu(Menu):
    """
    In game, the user can choose what direction and how far to move.
    """

    def create_prompts(self) -> None:
        self.main_prompt = """
TODO: Choose where to move.
"""
    # TODO: Show the maximum range to move backwards and forwards, depending
    # on current tank selected.

    def create_responses(self) -> None:
        def go_to_main_menu():
            self.prompt = None
            self.next_menu = MainMenu()


class GameShellMenu(Menu):
    """
    In game, the user can choose what shell to load for their upcoming shot.
    """

    def create_prompts(self) -> None:
        self.main_prompt = """
TODO: Choose the next shell to fire.
        """
        # TODO: Iterate through tank ammo rack

    def create_responses(self) -> None:

        def go_to_main_menu():
            self.prompt = None
            self.next_menu = MainMenu()

        self.valid_responses = {
            "m": go_to_main_menu
        }


class GameAimMenu(Menu):
    """
    In game, the user can pick the angle at which they aim their upcoming shot.
    """

    MIN_ANGLE = 0  # degrees from horizontal
    MAX_ANGLE = 90

    def create_prompts(self) -> None:
        self.main_prompt = """
Choose an angle to fire at (0° - 90°)
        """

    def create_responses(self) -> None:
        def go_to_main_menu():
            self.prompt = None
            self.next_menu = MainMenu()

        def restart():
            # TODO
            # this need to set the valid locations, health and ammo racks
            # to their default states before the game started.
            # This means that these values need to be saved before the
            # game starts so they can be retrieved.
            pass

        self.valid_responses = {
            "r": restart,
            "m": go_to_main_menu
        }

    def matches_range(self, response: str) -> bool:
        """
        valid input is any int from 0 to 90
        """
        try:
            return GameAimMenu.MIN_ANGLE <= int(response) <= GameAimMenu.MAX_ANGLE
        except Exception:
            return False

    def evaluate(self, response: str) -> None:
        degrees = int(response)  # guaranteed int due to matches_range()
        # TODO: set the angle to int(response)
        pass

    def prompt_invalid_response(self) -> None:
        message = "Please choose an angle between 0° and 90°, r, or m."
        self.prompt = self.main_prompt + "\n" + message


class FillAmmoMenu(Menu):
    """
    The user can pick what ammo to fill their tank's ammo rack with.
    """

    def create_prompts(self) -> None:
        pass

    def create_responses(self) -> None:
        pass
