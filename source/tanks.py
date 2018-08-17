"""
Contains all tank classes.
"""


from typing import Callable, Dict, List, Set
from tank_components import AmmoRack, Plate
from shells import Shell

class Tank(object):
    """
    Represents a tank, which is composed of a collection of plates that form
    its hitbox, and an ammo rack that is filled with shells. Certain
    restrictions can be placed on the type of shells the ammo rack can contain.
    Tanks can move at specified speed.

    Tanks should not be instantiated directly by constructor.
    Use TankFactory to create tanks instead.
    """
    # Name constants
    # Use these names to specify to TankFactory on which tank to get
    T_34 = "T-34"
    KV_1 = "KV-1"
    SHERMAN = "Sherman"
    PANZER_III = "Panzer III"
    PANZER_IV = "Panzer IV"
    PANTHER = "Panther"
    TIGER = "Tiger"
    FERDINAND = "Ferdinand"

    def __init__(self, name: str, description: str, speed: int,
                 ammo_rack: AmmoRack, ammo_capacity: int,
                 shell_types: Set[Shell], hitbox: List[Plate]):
        self.name = name
        self.description = description
        self.speed = speed
        self.ammo_rack = ammo_rack
        self.ammo_capacity = ammo_capacity
        self.shell_types = shell_types
        self.hitbox = hitbox


class TankFactory(object):
    """
    Instantiates Tank instances. Use get_tank().
    """

    VALID_TANKS = Dict[str, Callable]
    initialized = False

    @staticmethod
    def _initialize():
        """
        This connects each Tank to its corresponding creation method, which is
        needed for get_tank().
        """
        TankFactory.VALID_TANKS = {
            Tank.T_34: TankFactory._get_t34,
            Tank.KV_1: TankFactory._get_kv1,
            Tank.SHERMAN: TankFactory._get_sherman,
            Tank.PANZER_III: TankFactory._get_panzer3,
            Tank.PANZER_IV: TankFactory._get_panzer4,
            Tank.TIGER: TankFactory._get_tiger,
            Tank.FERDINAND: TankFactory._get_ferdinand
        }
        TankFactory.initialized = True  # Does not need to be initialized again

    @staticmethod
    def get_tank(name: str) -> Tank:
        """
        Get a tank of a specified name. Use Tank.TANK_NAME to choose from all
        valid tank names.

        Parameters:
            str     name:   of tank wanted to retreive.
                            Ex. Tank.SHERMAN, Tank.TIGER
        Returns:
            Tank    tank:   of specified tank name
        """
        if not TankFactory.initialized:  # Check if initalized first
            TankFactory._initialize()

        if name in TankFactory.VALID_TANKS.keys():
            return TankFactory.VALID_TANKS[name]()
        else:
            raise ValueError("Invalid tank name.")

    @staticmethod
    def _get_t34() -> Tank:
        # TODO:
        pass

    @staticmethod
    def _get_kv1() -> Tank:
        # TODO:
        pass

    @staticmethod
    def _get_sherman() -> Tank:
        # This is just for debugging purposes
        return Tank(5, AmmoRack(5, {"a": 1}), 5, {"a"}, None)

    @staticmethod
    def _get_panzer3() -> Tank:
        # TODO:
        pass

    @staticmethod
    def _get_panzer4() -> Tank:
        # TODO:
        pass

    @staticmethod
    def _get_tiger() -> Tank:
        # TODO:
        pass

    @staticmethod
    def _get_ferdinand() -> Tank:
        # TODO:
        pass
