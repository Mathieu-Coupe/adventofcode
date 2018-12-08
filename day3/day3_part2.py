#!/usr/bin/python

import sys
import numpy
from parse import compile

with open("input") as f:
    content = f.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
items = [x.strip() for x in content]

# create result array as a flat arrays
fabric = numpy.zeros(1000*1000, dtype=int)

# parsing
p = compile("#{} @ {},{}: {}x{}")

for item in items:
    #print("Processing item %s" % (item))
    values = p.parse(item)
    x = int(values[1])
    y = int(values[2])
    h = int(values[3])
    l = int(values[4])
#    print("x=%d y=%d h=%d l=%d" % (x, y, h, l))
    for xp in range(x, x+h):
        for yp in range(y, y+l):
#            print("xp = %d, yp = %d" % (xp, yp))
            fabric[xp*1000+yp] += 1

# verify that each patch has only 1's
for item in items:
    #print("Processing item %s" % (item))
    values = p.parse(item)
    x = int(values[1])
    y = int(values[2])
    h = int(values[3])
    l = int(values[4])
#    print("x=%d y=%d h=%d l=%d" % (x, y, h, l))
    patch_is_okay = True
    for xp in range(x, x+h):
        for yp in range(y, y+l):
#            print("xp = %d, yp = %d" % (xp, yp))
            if fabric[xp*1000+yp] != 1:
                patch_is_okay = False
    
    if patch_is_okay:
        print("Found patch #%s" %(values[0]))

