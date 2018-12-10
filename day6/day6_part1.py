#!/usr/bin/python

import sys
import numpy
from parse import compile

with open("input") as f:
    content = f.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
items = [x.strip() for x in content]

# parse compile
p = compile("{}, {}")

# array to store places
places = []

place_name = ord('A');
max_x = 0
max_y = 0

for item in items:
    # parse
    values = p.parse(item)
    x = int(values[0])
    y = int(values[1])
    if x > max_x:
        max_x = x

    if y > max_y:
        max_y = y

    places.append(dict(name=chr(place_name), x=x, y=y, infinite=False))
    place_name += 1

#print(places)
#max_x += 1
#max_y += 1

grid = []
# create grid from 0 to max(x)/max(y)
for y in range(0, max_y+1):
    grid_line = []
    for x in range(0, max_x+1):
        grid_line.append(dict(x=x, y=y, place=None, distance=99999, nearest=None))
    grid.append(grid_line)

#print(grid)

def display_grid(g):
    for y in range(0, max_y+1):
        for x in range(0, max_x+1):
            if g[y][x]['place'] != None:
                sys.stdout.write(g[y][x]['place'])
            else:
                if g[y][x]['nearest'] != None:
                    sys.stdout.write(g[y][x]['nearest'].lower())
                else:
                    sys.stdout.write('.')
        sys.stdout.write('\n')

# calculate distance and take ownership of grid place nearest of place
def populate(place):
    for y in range(0, max_y+1):
        for x in range(0, max_x+1):
            distance = abs(place['x'] - x) + abs(place['y'] - y)
            if distance == 0:
                grid[y][x]['place'] = place['name']
            if distance < grid[y][x]['distance']:
                # this place is near than previous one
                grid[y][x]['distance'] = distance
                grid[y][x]['nearest'] = place['name']
            elif distance == grid[y][x]['distance']:
                # this place is between two
                grid[y][x]['nearest'] = '.'


# iterate over places
for place in places:
    populate(place)

display_grid(grid)

for place in places:
    owned = 0
    # count number of owned places
    for y in range(0, max_y+1):
        for x in range(0, max_x+1):
            if grid[y][x]['nearest'] == place['name']:
                owned += 1
                # check for infinite 
                if y == 0 or x == 0 or y == max_y or x == max_x:
                    place['infinite'] = True

    place['owned'] = owned

# find largest area
places.sort(key=lambda place: (place['infinite'] == False) * place['owned'], reverse=True)

print(places)
print("Result is : %s with size %d" % (places[0]['name'], places[0]['owned']))
