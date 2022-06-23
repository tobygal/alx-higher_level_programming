#!/usr/bin/python3
'''
This module defines and initalizes a square class.
'''


class Square:
    '''
    Square Representation.
    '''
    def __init__(self, size=0):
        '''
        Initialization of the size of square of type int.
        Args:
            size of type int
        '''
    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    self.__size = size
