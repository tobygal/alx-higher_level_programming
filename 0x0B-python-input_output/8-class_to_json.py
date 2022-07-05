#!/usr/bin/python3
"""
This function returns the dictionary description with simple data
structure for JSON serialization of an object.
"""


import json


def class_to_json(obj):
    """dictionary object"""
    return obj.__dict__
