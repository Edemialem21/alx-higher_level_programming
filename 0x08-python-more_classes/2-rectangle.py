#!/usr/bin/python3
"""
creating an empty class called Rectangle
"""


class Rectangle:
    """
    an empty class of rectangle
    """
    def __init__(self, width=0, height=0):
        """ initialze all private instance with default values"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter to retrive the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width valu except for it is not integer and less than zero
        if that is not the case it raise typerror and value error
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """it gets the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the hight valu except for it is not integer and less than zero
        if that is not the case it raise typerror and value error
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculates area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """calculates perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width + self.height))
