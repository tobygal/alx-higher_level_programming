#!/usr/bin/python3
"""
This file contains a class called Base.
"""


class Base:
    """ Base class implementation"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class instance"""
        if id is not None:
            self._id = id
        else:
            Base.__nb_objects += 1
            self._id = Base.__nb_objects
