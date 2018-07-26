"""
Anything to make life easier goes here.
"""

import textwrap
from time import time
from typing import Callable

import types

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


def print_wrap(inText: str) -> None:
    """
    Prints a string and hardwraps the text by word at 79 columns.
    """
    outText = textwrap.fill(inText, 79)
    for line in outText:
        print(line)


def wrap(text: str) -> str:
    """
    Wraps text to 79 columns

    Paramters:
        String  text

    Returns:
        String wrapped_text
    """
    return textwrap.fill(text, 79)


def time_function(func: Callable) -> Callable:
    """
    Decorator/wrapper function.

    Make a function print how long it took to call whenever it is called.

    Parameter:
        function func: any arbitrary function

    Returns:
        function timed_func: same function, but now prints its call time when
        called
    """
    def timed_func(*args, **kwargs):
        before = time()
        return_value = func(*args, **kwargs)
        after = time()
        print(func.__name__ + "() elapsed:", after - before, "seconds")
        return return_value
    timed_func.__name__ = func.__name__
    return timed_func  # the input function is now wrapped to time


def time_class(cls: object) -> object:  # TODO class static type
    """
    Decorate/wrapper function.

    Make all methods of a class timed.

    Parameter:
        class cls: any arbitrary class

    Returns:
        class timed_class: same class, but now all methods print its call time
        when called
    """
    # print("cls type is: " + str(type(cls)))
    for attr_name in dir(cls):
        attr_value = getattr(cls, attr_name)
        if isinstance(attr_value, types.FunctionType): # check if attr is a function
            # print("\tattr_value: " + str(attr_value))
            # apply the function_decorator to your function
            # and replace the original one with your new one
            setattr(cls, attr_name, time_function(attr_value))
    return cls
