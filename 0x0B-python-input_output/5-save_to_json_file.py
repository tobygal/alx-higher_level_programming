#!/usr/bin/python3
"""
This function saves a text file from json string.
"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
