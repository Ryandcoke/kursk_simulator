class Shell(object):
    """
    The shell class
    """
    def __init__(self, name, constant, coefficient_1, coefficient_2, damage):
        self.name = name
        self.constant = constant
        self.coefficient_1 = coefficient_1
        self.coefficient_2 = coefficient_2
        self.damage = damage


class ExplosiveShell(Shell):
    """

    """
    def __init__(self):
        pass
