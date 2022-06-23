#!/usr/bin/python3
'''
Define a Square class.
'''


class Square:
    '''
    Square representation.
    '''
    def __init__(self, size=0):
        '''
        Initialization of a new Square.
        Args:
            size (int): The size of the new square.
        '''
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
    self.__size = size

    def area(self):
        ''' Calculates the area of the square.
        '''
        return (self.__size ** 2)

    def my_print(self):
        '''
        prints a square of given size.
        '''
        if (self.__size == 0):
            print('')
        for 1 in range(self.__size):
            print('#' * self.__size)
