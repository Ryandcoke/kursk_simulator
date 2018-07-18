"""
Anything to make life easier goes here.
"""

class Singleton(type):
    """
    Metaclass.

    Class instances of this can only have 1 instance. In other words,
    if their constructor is called, a new single instance is returned if none
    exist, and that that same instance is return upon any future constructor
    calls.
    """
    _instances = {}  # stores all singleston object instances
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:  # if not created, create and store it
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]  # return singleton instance
