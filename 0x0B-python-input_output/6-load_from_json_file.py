#!/usr/bin/python3
"""
This function creates an object from json.
"""
import json


def load_from_json_file(filename):
    """load from json"""
    with open(filename, encoding="utf-8") as f:
        return (json.load(f))
