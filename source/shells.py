"""
Contains all shell classes. Shells are the ammunition used by tanks and are
contained within ammo racks.
"""


class Shell(object):
    """
    Represents a shell to be fired
    """
    def __init__(self, name, constant, coefficient_1, coefficient_2, damage):
        self.name = name
        self.constant = constant
        self.coefficient_1 = coefficient_1
        self.coefficient_2 = coefficient_2
        self.damage = damage


class ShellFactory(object):
    """
    Creates shells

    E X C E S S I V E B O I L E R P L A T E C O D E B O Y S

    This is important because AmmoRack does not actually store shells but
    the name of the shell type (String).
    """
    @staticmethod
    def get_shell(name):
        """
        Creates a shell of a specified name

        Parameters:
            String  name:   of shell to create

        Returns:
            Shell   shell:  of specified name
                            or None if invalid name
        """
        pass


class ExplosiveShell(Shell):
    """

    May or may not be needed. If the "explosive" property has the same effect
    for all explosive shells, then we can simply add a boolean explosive
    attribute to the Shell class.

    """
    def __init__(self):
        pass
