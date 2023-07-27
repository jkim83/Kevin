#! /usr/bin/env python3

#Challenge A
#Kevin Kim
import sys

def sunView(buildings):
    if len(buildings) == 1:
        return 1
    
    counter = 1 #for rightmost building
    maxheight = buildings[-1]

    for i in range(len(buildings) - 2, -1, -1):
        if buildings[i] > maxheight:
            counter += 1
            maxheight = buildings[i]
        else:
            continue
    return counter


def program(stream = sys.stdin):
    for line in stream:
        buildings = list(map(int, line.split()))
        if len(buildings) == 0:
            print(0)
        else:
            res = sunView(buildings)
            print(res)

program()


