#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        a = ord(str[i])
        if a > 96 and a < 123:
            a -= 32
            a = chr(a)
            c = i + 1
            str = str[:i] + a + str[c:]
        else:
            continue
    print("{}".format(str))
