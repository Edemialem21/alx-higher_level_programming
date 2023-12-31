#!/usr/bin/python3

"""
initialization of private instance using __self and check TypeError
and ValueError if that is the case it raise an error using error exception.
"""


class Square():
    """
    defination of a private object attribute
    called size, and checks the attribute if it is integer and positive.
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
