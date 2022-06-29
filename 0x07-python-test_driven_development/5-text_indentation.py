#!/usr/bin/python3
"""
This is the "5-text_indentation" module.
The function accepts one argument.
"""


def text_indentation(text):
    """adds 2 new lines after ., ?, : """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in '.:?':
        text = text.replace(1, '{}\n'.format(i))
    lines = text.splitlines()
    for index, line in enumerate(lines):
        print(line.strip(), end='' if index == len(lines) - 1 elsr '\n\n')
