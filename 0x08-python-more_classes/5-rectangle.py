#!/usr/bin/python3
"""
This module describes a rectangle based on 0-rectangle.py.
"""


class Rectangle:
    """
    This class describes a Rectangle."""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This method retuns the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """This method returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """This returns a string representation of Rectangle."""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """return a string representation of the rectangle to be able
        to recreate a new instance by using eval"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        del self
        print("Bye rectangle...")
