"""
Contains all components that make up tanks.
"""


from enum import Enum
from typing import Dict, Tuple


class AmmoRack:
    """
    Contains a number of shells, up to a maximum ammo capacity.

    Parameters:
        int     ammo_capacity:  the total number of shells this ammo rack can
                                contain
        dict    ammo:           str key:    name of shell
                                int value:  count of shell
    """

    def __init__(self, ammo_capacity: int, ammo: Dict[str, int]):
        self.ammo_capacity = ammo_capacity
        self.ammo = ammo

    def __str__(self):
        return "[ammo capacity: " + str(self.ammo_capacity)
        + " | ammo: " + str(self.ammo) + "]"

    def add(self, name: str, count: int = 1) -> bool:
        """
        Add a number of shells of a specified type to this ammo rack

        Returns:
            True if shell added
        """
        if count + self.get_shell_count() > self.ammo_capacity:
            # Cannot add any more shells if there is no space left
            return False

        # Get the number of shells of specified type
        contained_count = self.ammo.get(name)

        if contained_count is None:
            # if the rack does not contain the specified ammo type
            # add it to rack
            self.ammo[name] = count
        else:
            # else, increment to already contained count
            self.ammo[name] = contained_count + count
        return True

    def get_shell_count(self) -> int:
        """
        Returns:
            the total number of shells this ammo rack contains
        """
        total_count = 0
        for shell, count in self.ammo.items():
            total_count += count
        return total_count

    def remove(self, name: str) -> bool:
        """
        Remove 1 shell of a specified type from this ammo rack

        name  ex:
            "American Mark I"

        Returns:
            True if shell was removed
        """
        # Get the number of shells of specified type
        count = self.ammo.get(name)

        if count is None:
            # if the rack does not contain the specified ammo type
            # return nothing
            return False

        new_count = count - 1

        if new_count < 0:
            # If there are no more shells left, then remove shell
            # from ammo rack
            return False
        else:
            # Otherwise, we decrease the ammo count by 1
            self.ammo[name] = new_count
            return True


class Plate:
    """
    Represents a single linear plate that composes a tank's hitboxes.
    """

    def __init__(self, point1: Tuple[int, int], point2: Tuple[int, int],
                 thickness: int):
        """
        Parameters:
            (x, y)  point1
            (x, y)  point2
            int     thickness in milimeters
        """
        self.point1 = point1
        self.point2 = point2
        self.thickness = thickness
