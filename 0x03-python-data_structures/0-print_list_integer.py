#!/usr/bin/python3
if __name__ == '__main__':
    def print_list_integer(my_list=[]):
        for num in range(len(my_list)):
            print("{:d}".format(my_list[num]))