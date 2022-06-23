#!/usr/bin/python3
'''
This module defines and initalizes a square class.
'''


class Square:
    '''
    Square initialization.
    '''
    def __init__(self, size=0)
    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    self.__size = size
