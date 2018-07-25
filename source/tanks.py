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
    # Name constants
    T_34 = "T-34"
    KV_1 = "KV-1"
    SHERMAN = "Sherman"
    PANZER_III = "Panzer III"
    PANZER_IV = "Panzer IV"
    PANTHER = "Panther"
    TIGER = "Tiger"
    FERDINAND = "Ferdinand"

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
    Instantiates Tank instances.
    """

    VALID_TANKS = {}
    initialized = False

    @staticmethod
    def _initialize():
        """
        This connects each Tank to its corresponding creation method, which is
        needed for get_tank().
        """
        TankFactory.VALID_TANKS = {
            Tank.T_34 : TankFactory._get_t34,
            Tank.KV_1 : TankFactory._get_kv1,
            Tank.SHERMAN : TankFactory._get_sherman,
            Tank.PANZER_III : TankFactory._get_panzer3,
            Tank.PANZER_IV : TankFactory._get_panzer4,
            Tank.TIGER : TankFactory._get_tiger,
            Tank.FERDINAND : TankFactory._get_ferdinand
        }
        TankFactory.initialized = True  # Does not need to be initialized again

    @staticmethod
    def get_tank(name):
        """
        Get a tank of a specified name. Use Tank.TANK_NAME to choose from all
        valid tank names.

        Parameters:
            String  name:   of tank wanted to retreive.
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
    def _get_t34():
        # TODO:
        pass

    @staticmethod
    def _get_kv1():
        # TODO:
        pass

    @staticmethod
    def _get_sherman():
        # This is just for debugging purposes
        return Tank(5, AmmoRack(5, {"a": 1}), 5, {"a"}, None)

    @staticmethod
    def _get_panzer3():
        # TODO:
        pass

    @staticmethod
    def _get_panzer4():
        # TODO:
        pass

    @staticmethod
    def _get_tiger():
        # TODO:
        pass

    @staticmethod
    def _get_ferdinand():
        # TODO:
        pass
