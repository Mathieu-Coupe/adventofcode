#!/usr/bin/python

import sys

with open("input") as f:
    content = f.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
items = [x.strip() for x in content]

# check if only one char is different
def compare(a, b):
    joker = True
    for i in range(0, len(a)-1):
        if a[i] != b[i]:
            if joker == False:
                return False
            else:
                joker = False

    return True

# transform list to count number of chars in each chain
for item1 in items:
    for item2 in items:
        if item1 != item2:
            if compare(item1, item2):
                # merge both string to find final result
                result = ""
                for n in range(0, len(item1)):
                    if item1[n] == item2[n]:
                        result += item1[n]
                
                print("Result = %s" % (result))
                sys.exit()
