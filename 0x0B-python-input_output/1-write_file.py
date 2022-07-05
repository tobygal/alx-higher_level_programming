#!/usr/bin/python3
"""
This function writes to a file and returns the
number of character written
"""


def write_file(filename="", text=""):
    """write to a text file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
