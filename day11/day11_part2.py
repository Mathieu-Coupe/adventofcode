#!/usr/bin/python

from __future__ import print_function
import sys
import numpy

with open("input") as f:
    grid_serial = int(f.read())

print("Grid serial number = %d" % grid_serial)
#grid_serial = 42
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

max_fuel = 0
result = ""
for r in range(1, 300+1):
    print("Using range %d" % r)

    fuel_cell = numpy.zeros((xsize, ysize), dtype=int)
    for y in range(ysize - r):
        for x in range(xsize - r):
            fuel_cell[x, y] = numpy.sum(grid[x:x+r, y:y+r])

    places = numpy.where(fuel_cell == numpy.max(fuel_cell))
    if fuel_cell[places[0][0], places[1][0]] > max_fuel:
        max_fuel = fuel_cell[places[0][0], places[1][0]]
        result = "%d,%d,%d" % (places[0][0], places[1][0], r)

def display_grid(g):
    # display grid
    for y in range(ysize):
        for x in range(xsize):
            print("%d " % g[x, y], end='')
        print("")

#display_grid(grid)
#display_grid(fuel_cell)
#find max value
print("result = %s" % result)
