"""
Contains all tank classes.
"""


from tank_components import AmmoRack


class Tank(object):
    """
    The tank class.

    Tanks should not be instantiated directly by constructor.
    Use TankFactory to create tanks instead.

    """
    def __init__(self, name, description, speed, ammo_rack, ammo_capacity, shell_types, hitbox):
        self.name = name
        self.description = description
        self.speed = speed
        self.ammo_rack = ammo_rack
        self.ammo_capacity = ammo_capacity
        self.shell_types = shell_types
        self.hitbox = hitbox


class TankFactory(object):
    """
    Creates tank objects.
    """
    VALID_TANKS = {}

    @staticmethod
    def initialize():
        """
        Run this before doing anything else with this class
        """
        TankFactory.VALID_TANKS["Sherman"] = TankFactory.create_sherman

    @staticmethod
    def get_tank(name):
        """
        Parameters:
            String name
                of tank wanted to retreive
        Returns:
            a tank of specified tank name
        """
        if name in TankFactory.VALID_TANKS.keys():
            return TankFactory.VALID_TANKS[name]()  # debug

    @staticmethod
    def create_sherman():
        # This is just for debugging p
        return Tank(5, AmmoRack(5, {"a": 1}), 5, {"a"}, None)
