#!/usr/bin/python3
char = 97
while char <= 122:
    if chr(char) != 'q' and chr(char) != 'e':
        print("{}".format(chr(char)), end='')
    char += 1
