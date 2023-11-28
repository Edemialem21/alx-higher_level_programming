#!/usr/bin/python3
def pow(a, b):
    po = 1
    if b == 0:
        return 1
    elif b < 0:
        for i in range(abs(b)):
            po /= a
        return po
    else:
        for i in range(b):
            po *= a
        return po           
