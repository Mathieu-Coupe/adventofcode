#!/usr/bin/python

from __future__ import print_function
import sys
import numpy

with open("input") as f:
    grid_serial = int(f.read())

print("Grid serial number = %d" % grid_serial)
xsize = 300
ysize = 300

def compute(x, y, serial):
    rack_id = x + 10
    power = rack_id * y
    power += serial
    power *= rack_id
    power = (power % 1000) / 100
    power -= 5
    return power

grid = numpy.zeros((xsize, ysize), dtype=int)
for y in range(ysize):
    for x in range(xsize):
        grid[x, y] = compute(x, y, grid_serial)

fuel_cell = numpy.zeros((xsize, ysize), dtype=int)
for y in range(ysize):
    for x in range(xsize):
        fuel_cell[x, y] = numpy.sum(grid[x:x+3, y:y+3])

def display_grid(g):
    # display grid
    for y in range(ysize):
        for x in range(xsize):
            print("%d " % g[x, y], end='')
        print("")

#display_grid(grid)
#display_grid(fuel_cell)
#find max value
places = numpy.where(fuel_cell == numpy.max(fuel_cell))
print("Coordinates = %d,%d" % (places[0][0], places[1][0]))
