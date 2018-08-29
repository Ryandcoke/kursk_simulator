"""
Contains all shell classes. Shells are the ammunition used by tanks and are
contained within ammo racks.
"""


from enum import Enum
from typing import Callable, Dict


class ShellName(Enum):
    PZGR_39_8_8 = "8.8 cm Pzgr. 39"
    PZGR_40_8_8 = "8.8 cm Pzgr. 40"
    HI_39 = "HI.39"
    M61 = "M61"
    M72 = "M72"
    PZGR_39_5_0 = "5.0 cm Pzgr. 39"
    PZGR_40_5_0 = "5.0 cm Pzgr. 40"
    PZGR_39_7_5 = "7.5 cm Pzgr. 39"
    PZGR_40_7_5 = "7.5 cm Pzgr. 40"
    PZGR_39_42_7_5 = "7.5 cm Pzgr. 39/42"
    PZGR_40_42_7_5 = "7.5 cm Pzgr. 40/42"
    BR_350P = "BR-350P"
    BR_350B = "BR-350B"
    ZIS_5_BR_350P = "ZiS-5 BR-350P"
    ZIS_5_BR_350B = "ZiS-5 BR-350B"

    def __str__(self):
        return self.value


class Shell:
    """
    Represents a shell to be fired
    """

    def __init__(self, name: ShellName, constant: float, coefficient_1: float,
                 coefficient_2: float, damage: float):
        self.name = name
        self.constant = constant
        self.coefficient_1 = coefficient_1
        self.coefficient_2 = coefficient_2
        self.damage = damage


class ShellFactory:
    """
    Instantiates Shell instances.

    E X C E S S I V E B O I L E R P L A T E C O D E B O Y S

    This is important because AmmoRack does not actually store shells but
    the name of the shell type (String).
    """

    VALID_SHELLS = Dict[ShellName, Callable]
    initialized = False

    @staticmethod
    def get_shell(name: ShellName) -> Shell:
        """
        Creates a shell of a specified name

        Parameters:
            ShellName   name:   of shell to create

        Returns:
            Shell       shell:  of specified name
                                or None if invalid name
        """
        if not ShellFactory.initialized:
            ShellFactory._initialize()

        if name in ShellFactory.VALID_SHELLS.keys():
            return ShellFactory.VALID_SHELLS[name]()
        else:
            raise ValueError("Invalid shell name.")

    @staticmethod
    def _initialize():
        """
        Connects shell names with shell creation methods in VALID_SHELLS
        dictionary.
        """
        ShellFactory.VALID_SHELLS = {
            ShellName.PZGR_39_8_8: ShellFactory._get_pzgr_39_8_8,
            ShellName.PZGR_40_8_8: ShellFactory._get_pzgr_40_8_8,
            ShellName.HI_39: ShellFactory._get_hi_39,
            ShellName.M61: ShellFactory._get_m61,
            ShellName.M72: ShellFactory._get_m72,
            ShellName.PZGR_39_5_0: ShellFactory._get_pzgr_39_5_0,
            ShellName.PZGR_40_5_0: ShellFactory._get_pzgr_40_5_0,
            ShellName.PZGR_39_7_5: ShellFactory._get_pzgr_39_7_5,
            ShellName.PZGR_40_7_5: ShellFactory._get_pzgr_40_7_5,
            ShellName.PZGR_39_42_7_5: ShellFactory._get_pzgr_39_42_7_5,
            ShellName.PZGR_40_42_7_5: ShellFactory._get_pzgr_40_42_7_5,
            ShellName.BR_350P: ShellFactory._get_br_350p,
            ShellName.BR_350B: ShellFactory._get_br_350b,
            ShellName.ZIS_5_BR_350P: ShellFactory._get_zis_5_br_350p,
            ShellName.ZIS_5_BR_350B: ShellFactory._get_zis_5_br_350b
        }
        ShellFactory.initialized = True

    @staticmethod
    def _get_pzgr_39_8_8() -> Shell:
        pass

    @staticmethod
    def _get_pzgr_40_8_8() -> Shell:
        pass

    @staticmethod
    def _get_hi_39() -> Shell:
        pass

    @staticmethod
    def _get_m61() -> Shell:
        pass

    @staticmethod
    def _get_m72() -> Shell:
        pass

    @staticmethod
    def _get_pzgr_39_5_0() -> Shell:
        pass

    @staticmethod
    def _get_pzgr_40_5_0() -> Shell:
        pass

    @staticmethod
    def _get_pzgr_39_7_5() -> Shell:
        pass

    @staticmethod
    def _get_pzgr_40_7_5() -> Shell:
        pass

    @staticmethod
    def _get_pzgr_39_42_7_5() -> Shell:
        pass

    @staticmethod
    def _get_pzgr_40_42_7_5() -> Shell:
        pass

    @staticmethod
    def _get_br_350p() -> Shell:
        pass

    @staticmethod
    def _get_br_350b() -> Shell:
        pass

    @staticmethod
    def _get_zis_5_br_350p() -> Shell:
        pass

    @staticmethod
    def _get_zis_5_br_350b() -> Shell:
        pass


class ExplosiveShell(Shell):
    """
    May or may not be needed. If the "explosive" property has the same effect
    for all explosive shells, then we can simply add a boolean explosive
    attribute to the Shell class.
    """

    def __init__(self):
        pass
