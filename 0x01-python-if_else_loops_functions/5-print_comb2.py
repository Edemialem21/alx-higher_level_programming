#!/usr/bin/python3
decimal = 0
for num in range(0, 100):
    if num < 10:
        print(f"0{num}", end='')
    else:
        print(num, end= '')
    if num != 99:
        print(chr(44), end= ' ')
    decimal += 1
