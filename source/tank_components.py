class AmmoRack(object):
    """
    The ammo rack class
    """
    def __init__(self, ammo_capacity, ammo):
        self.ammo_capacity = ammo_capacity
        self.ammo = ammo

    def remove(self, name):
        """
        name  ex:
            "American Mark I"

        Returns:
            True if shell was removed
        """
        # Get the number of shells of specified type
        count = self.get(name)

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
            self.ammo.put(name, new_count)
            return True
