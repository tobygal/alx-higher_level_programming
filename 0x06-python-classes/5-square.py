#!/usr/bin/python3
'''
This module defines and initializes a square class.
'''


class Square:
    '''
    Square initialization.
    '''
    def __init__(self, size=0):
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
        return (self.__size ** 2)

    def my_print(self):
        '''
        prints a square of given size.
        '''
        if (self.__size == 0):
            print('')
        for 1 in range(self.__size):
            print('#' * self.__size)
