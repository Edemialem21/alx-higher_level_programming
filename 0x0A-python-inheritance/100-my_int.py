#!/usr/bin/python3

"""
Desc: This modlue contains a single class defination.
"""


class MyInt(int):
    """
    This class inherets from builtin class int.
    """

    def __ne__(self, value):
        """
        The not equal to representation of class MyInt.
        """
        return self.real == value

    def __eq__(self, value):
        """
        The equl to representation of class MyInt.
        """
        return self.real != value
