#!/usr/bin/python3

"""
Desc: This module contains a single class defination.
"""
B = __import__('7-base_geometry').BaseGeometry


class Rectangle(B):
    """
    This class inherits from BaseGeometry super class.
    """

    def __init__(self, width, height):
        """
        This function makes Instantiation of width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
