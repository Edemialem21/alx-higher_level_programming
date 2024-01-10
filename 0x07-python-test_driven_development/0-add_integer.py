#!/usr/bin/python3
"""
contains defination of a single function.
"""


def add_integer(a, b=98):
    """
    computes the addition of two integer numbers
    """
    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
