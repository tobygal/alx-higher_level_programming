#!/usr/bin/python3
def magic_string():
    magic_string.s = getattr(magic_string, 's', 0) + 1
    return ("BestSchool, " * (magic_string.s - 1) + "BestSchool")
