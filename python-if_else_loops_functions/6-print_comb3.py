#!/usr/bin/python3
# 6-print_comb3.py
for x in range(0,10):
    for y range(1,10):
        if x >= y:
            continue
        elif x == 8 and y == 9:
            print("{}{}".format(x,y))
        else:
            print("{}{}".format(x,y), end=", ")
