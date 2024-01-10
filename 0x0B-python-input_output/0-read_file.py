#!/usr/bin/python3

"""
Desc: This module deals with reading files.
"""


def read_file(filename=""):
    """
    This function reads a text file (UTF8) and prints it to stdout.
    """

    with open(filename, encoding="utf8") as my_file:
        for text in my_file:
            print(text, end="")
