#! /usr/bin/env python3

#Challenge B
#Kevin Kim

import sys

def iso(words):
    word1, word2 = words[0], words[1]

    if len(word1) != len(word2): #if lengths arent same, can't be iso
        return False
    
    compare_map = {}

    for i in range(len(word1)):
        compare_map[word1[i]] = word2[i]

    for i in range(len(word1)):
        if word2[i] != compare_map[word1[i]]:
            return False

    return True

def program(stream = sys.stdin):
    for line in stream:
        words = line.split()
        if len(words) != 2:
            continue
        elif iso(words):
            print('Isomorphic')
        else:
            print('Not Isomorphic')

program()


