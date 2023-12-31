#!/usr/bin/python3

"""
initialization of private instance using __self and check TypeError and ValueError if that is the case it raise an error using error exception.
"""


class Square():
    """
    Square class which creates private instance of size using exception handling in pyhton for TypeError and valueError handling.
    """

    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

