#!/usr/bin/python3
"""
This function converts a json to a string.
"""


import json


def from_json_string(my_str):
    """return an object represented by json"""
    return json.loads(my_str)
