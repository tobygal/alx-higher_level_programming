#!/usr/bin/python3
"""
A class Square that inherits from rectangle.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Implementation """
    def __init__(self, size: int, x=0, y=0, id=None):
        """ Initialization. """

        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self) -> str:
        """ string representation. """
        return "[Square] ({:d}) {:d}/{:d} - {:d}" \
            .format(self.id, self.x, self.y, self.__size)

    @property
    def size(self) -> int:
        """ size getter """
        return self.__size

    @size.setter
    def size(self, value: int):
        """size setter. """
        self.__size = value
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """using args to assign attributes."""
        attr = ['id', 'size', 'x', 'y']
        if args:
            for att, num in zip(attr, args):
                setattr(self, att, num)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)

    def to_dictionary(self):
        """set square to dictionary"""
        id = self.id
        size = self.__size
        x = self.x
        y = self.y

        return {'id': id, 'x': x, 'size': size, 'y': y}
