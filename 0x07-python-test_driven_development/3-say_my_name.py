#!/usr/bin/python3
"""
This module defines `say_my_name`
The function prints the full name of an individual.
"""


def say_my_name(first_name, last_name=""):
    """Prints 'My name is' then returns the first and last name."""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    return print("My name is {} {}".format(first_name, last_name))
