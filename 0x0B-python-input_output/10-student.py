#!/usr/bin/python3
"""
A class Student.
"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrive dictionary"""
        if attrs is not None and all(isinstance(y, str) for y in attrs):
            L = {}
            for m, n in self.__dict__.items():
                if m in attrs:
                    L[m] = n
            return L
        else:
            return self.__dict__
