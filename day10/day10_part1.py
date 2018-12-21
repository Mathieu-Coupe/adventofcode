#!/usr/bin/python

from __future__ import print_function
import sys
from parse import compile

with open("input") as f:
    content = f.readlines()

p = compile("position=<{},{}> velocity=<{},{}>")
items = []

class Point:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def __repr__(self):
        return "(%d, %d) [%d, %d]" % (self.position[0], self.position[1], self.velocity[0], self.velocity[1])

    def pos(self, time):
        return (self.position[0] + self.velocity[0] * time, self.position[1] + self.velocity[1] * time)

for line in content:
    x, y, vx, vy = p.parse(line)
    items.append(Point((int(x),int(y)), (int(vx), int(vy))))

max_time = 100000
min_surface = sys.maxint
min_surface_time = None
continue_search = True
time = 0
dimensions = None

while continue_search:
    min_x = sys.maxint
    max_x = -sys.maxint
    min_y = sys.maxint
    max_y = -sys.maxint

    for item in items:
        x, y = item.pos(time)

        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    size_x = max_x - min_x
    size_y = max_y - min_y
    surface = size_x * size_y
    if surface < min_surface:
        min_surface_time = time
        min_surface = surface
        dimensions = dict(min_x=min_x, min_y=min_y, max_x=max_x, max_y=max_y)

    time += 1
    if min_surface_time and time - min_surface_time > 500:
        continue_search = False

print("Minimal surface at time %d" % min_surface_time)
print(dimensions)

def display_grid(g):
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            sys.stdout.write(grid[y][x])
        sys.stdout.write('\n')

for time in [min_surface_time]:
    min_x = dimensions['min_x'] - 10
    min_y = dimensions['min_y'] - 10
    max_x = dimensions['max_x'] + 10
    max_y = dimensions['max_y'] + 10

    grid = []
    # create grid from min_x/min_y to max_x/max_y
    for y in range(0, max_y-min_y+1):
        grid_line = []
        for x in range(0, max_x-min_x+1):
            grid_line.append('.')
        grid.append(grid_line)

    # fill grid
    for item in items:
        x, y = item.pos(time)
        grid[y - min_y][x - min_x] = '#'

    print("Current time = %d" % time)
    display_grid(grid)
