class AmmoRack(object):
    """
    The ammo rack class
    """
    def __init__(self, ammo_capacity, ammo):
        self.ammo_capacity = ammo_capacity
        self.ammo = ammo

    def remove(self, name):
        # Get the number of shells of specified type
        count = self.get(name)
        # if the rack does not contain the specified ammo type
        # return nothing
        if count is None:
            return None

        # If there are no more shells left, then remove shell
        # from ammo rack
        new_count = count - 1
        if new_count == 0:
            self.ammo.remove(name)
        else:
            # Otherwise, we decrease the ammo count by 1
            self.ammo.put(name, new_count)
