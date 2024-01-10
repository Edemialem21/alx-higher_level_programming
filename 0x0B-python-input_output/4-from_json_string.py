#!/usr/bin/python3

"""
Desc: This module deals with the json object.
"""
from json import loads as ls


def from_json_string(my_str):
    """
    This function returns an object (Python data structure)
    represented by a JSON string
    """
    return ls(my_str)
