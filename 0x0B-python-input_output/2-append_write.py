#!/usr/bin/python3
"""
This function appends to a file and returns the length of
appended text.
"""


def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
