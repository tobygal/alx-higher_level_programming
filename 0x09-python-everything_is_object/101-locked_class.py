#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """Class prevents dynamic instances attributes."""
    __slots__ = ["first_name"]
