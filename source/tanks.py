"""
Contains all tank classes.
"""


from enum import Enum
from typing import Callable, Dict, List, Set
from tank_components import AmmoRack, Plate
from shells import ShellName


class TankName(Enum):
    """
    Valid tank options for TankFactory to create.
    """
    T_34 = "T-34"
    KV_1 = "KV-1"
    SHERMAN = "Sherman"
    PANZER_III = "Panzer III"
    PANZER_IV = "Panzer IV"
    PANTHER = "Panther"
    TIGER = "Tiger"
    FERDINAND = "Ferdinand"

    def __str__(self):
        return self.value


class Tank:
    """
    Represents a tank, which is composed of a collection of plates that form
    its hitbox, and an ammo rack that is filled with shells. Certain
    restrictions can be placed on the type of shells the ammo rack can contain.
    Tanks can move at specified speed.

    Tanks should not be instantiated directly by constructor.
    Use TankFactory to create tanks instead.
    """

    def __init__(self, name: TankName, description: str, speed: int,
                 ammo_rack: AmmoRack, shell_types: Set[ShellName],
                 hitbox: List[Plate]):
        self.name = name
        self.description = description
        self.speed = speed
        self.ammo_rack = ammo_rack
        self.shell_types = shell_types
        self.hitbox = hitbox


class TankFactory:
    """
    Instantiates Tank instances. Use get_tank(TankName) to create tanks.
    """

    VALID_TANKS = Dict[TankName, Callable]
    initialized = False

    @staticmethod
    def _initialize() -> None:
        """
        This connects each Tank to its corresponding creation method, which is
        needed for get_tank().
        """
        TankFactory.VALID_TANKS = {
            TankName.T_34: TankFactory._get_t34,
            TankName.KV_1: TankFactory._get_kv1,
            TankName.SHERMAN: TankFactory._get_sherman,
            TankName.PANZER_III: TankFactory._get_panzer3,
            TankName.PANZER_IV: TankFactory._get_panzer4,
            TankName.TIGER: TankFactory._get_tiger,
            TankName.FERDINAND: TankFactory._get_ferdinand
        }
        TankFactory.initialized = True

    @staticmethod
    def get_tank(name: TankName) -> Tank:
        """
        Get a tank of a specified name. Use TankName to choose from all
        valid tank names.

        Parameters:
            TankName    name:   of tank wanted to retreive.
                                Ex. TankName.SHERMAN, TankName.TIGER
        Returns:
            Tank        tank:   of specified tank name
        """
        if not TankFactory.initialized:
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
        # TODO: Currently debug values
        name = TankName.SHERMAN
        description = "TODO: Sherman tank description"
        speed = 5
        ammo_capacity = 5
        ammo_rack = AmmoRack(ammo_capacity)
        shell_types = {
            ShellName.M72
        }
        hitbox = [

        ]
        return Tank(name, description, speed, ammo_rack,
                    shell_types, hitbox)

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
