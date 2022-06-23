#!/usr/bin/python3
'''
This module defines a square class.
'''


class Square:
    '''
    Initialization of a square.
    '''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(position) != tuple or \
                len(position) != 2 or \
                not all(isinstance(i, int) for i in position) or \
                not all(i >= 0 for i in position):

            raise TypeError('position must be a tuple of 2 positive integers')
            self.__position = position

    def area(self):
        '''
        Calculates area of the square.
        '''
        return (self.__size ** 2)

    def my_print(self):
        '''
        Prints a square of given size with space as position.
        '''
        if (self.__size == 0):
            print('')
        else:
            for i in range(self.position[1]):
                print('')

                for i in range(self.size):
                    print(' ' * self.position[0] + '#' * self.size)
