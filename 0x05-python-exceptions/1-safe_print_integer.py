#!/usr/bin/python3
def safe_print_integer(value):
    boole = True
    try:
        print("{:d}".format(value))
    except (TypeError ValueError):
        boole = False
    finally:
        return boole
