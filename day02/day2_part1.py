#!/usr/bin/python

import sys

with open("input") as f:
    content = f.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
items = [x.strip() for x in content]

items_with_2 = 0
items_with_3 = 0

# transform list to count number of chars in each chain
for item in items:
    chars = []
    chars += item
    counts = [(chars.count(x), x) for x in set(chars)]
    counts_2items = filter(lambda x: x[0] == 2, counts)
    counts_3items = filter(lambda x: x[0] == 3, counts)
    if len(counts_2items) >= 1:
        #print("Found one box with only 2 letters : %s" % (counts_2items))
        items_with_2 += 1

    if len(counts_3items) >= 1:
        #print("Found one box with only 3 letters : %s" % (counts_3items))
        items_with_3 += 1

print("Result is : %d * %d = %d" % (items_with_2, items_with_3, items_with_2*items_with_3))
