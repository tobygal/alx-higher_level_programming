#!/usr/bin/python3
"""
This is the "4-print_square" module.
The module has one function, print_square(size).
"""


def print_square(size):
    """Prints a square with length size using # """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") " size, end="")
