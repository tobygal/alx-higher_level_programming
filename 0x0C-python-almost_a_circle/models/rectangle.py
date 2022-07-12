#!/usr/bin/python3
"""
A class Rectangle that inherits from Base class.
"""


from models.base import Base


class Rectangle(Base):
    """Impementation."""
    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """ Initialization"""
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """ string representation"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    def check_value_type(self, name: str, value: object, greater_equal=False):
        """ value and type validation"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if not greater_equal:
            if value <= 0:
                raise ValueError("{} must be >= 0".format(name))
            else:
                if value < 0:
                    raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self) -> int:
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width: int):
        """width setter"""
        self.check_value_type('width', width)
        self.__width = width

    @property
    def height(self) -> int:
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height: int):
        self.check_value_type('height', height)
        self.__height = height

    @property
    def x(self) -> int:
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x: int):
        """x setter"""
        self.check_value_type('x', x, True)
        self.__x = x

    @property
    def y(self) -> int:
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y: int):
        """y setter"""
        self.check_value_type('y', y, True)
        self.__y = y

    def area(self):
        return (self.__height * self.__width)
