#!/usr/bin/python3

"""
Desc: This module deals with JSON string.
"""
from json import dumps as d


def to_json_string(my_obj):
    """
    This function returns the JSON representation of an object (string)
    """

    return d(my_obj)
