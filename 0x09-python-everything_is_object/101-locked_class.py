#!/usr/bin/python3

"""
File: 101-locked_class.py
Desc: This module contains a single class defination.
"""


class LockedClass():
    """
    This class prevents the user from dynamically creating
    new instance attributes
    """
    __slots__ = ["first_name"]
