#!/usr/bin/python3

"""
initialization of private instance using __self and check TypeError
and ValueError if that is the case it raise an error using error exception.
"""


class Square():
    """
    defination of a private attribute called size and public method named area
    and checks the private attribute if it is integer and positive.
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
    def area(self):
        return self.__size ** 2
