#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = len(my_list) - 1
    for i in range(idx, -1, -1):
        if i >= 0:
            print("{:d}".format(my_list[i]))

