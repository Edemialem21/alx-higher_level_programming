#!/usr/bin/python3

"""
contains a class defination with private instance intialization using __self.
"""


class Square():
    """
    This is a classs with named Square with creating private instance of size.
    """

    def __init__(self, size):
        self.__size = size
