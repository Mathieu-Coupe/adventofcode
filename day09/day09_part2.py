#!/usr/bin/python

from __future__ import print_function
import sys
from parse import compile

with open("input") as f:
    content = f.read().replace('\n','')

p = compile("{} players; last marble is worth {} points")
players, last_marble = p.parse(content)
players, last_marble = int(players), int(last_marble) * 100 # What would the new winning Elf's score be if the number of the last marble were 100 times larger?

print("Players = %d, last marble = %d" % (players, last_marble))

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def display_ring(root, current_position, current_player):
    print('[%d] %d' % (current_player, root.val), end='')
    current = root.next
    while current != root:
        if current == current_position:
            print(' (%d) ' % current.val, end='')
        else:
            print('  %d  ' % current.val, end='')
        current = current.next

    print('')

def run():
    # variables
    scores = [0 for n in range(players)]

    # step0
    root = Node(0)
    root.next = root
    root.prev = root

    player = 0
    current_place = 0
    current_marble = root

    for marble in xrange(1, last_marble +1):

        if marble % 23 == 0:
            # find marble to remove
            marble_to_remove = current_marble.prev.prev.prev.prev.prev.prev.prev

            # current player add marble value to it's score
            scores[player] += marble_to_remove.val + marble

            # remove marble
            marble_to_remove.prev.next, marble_to_remove.next.prev = marble_to_remove.next, marble_to_remove.prev
            current_marble = marble_to_remove.next
        else:
            new_marble = Node(marble)
            # special case
            if root.next == root:
                root.next = new_marble
                root.prev = new_marble
                new_marble.next = root
                new_marble.prev = root
            else:
                # insert marble between current_marble.next and next_marble.next.next
                current_marble = current_marble.next
                next_marble = current_marble.next

                next_marble.prev = new_marble
                current_marble.next = new_marble
                new_marble.next = next_marble
                new_marble.prev = current_marble

            current_marble = new_marble

#        display_ring(root, current_marble, player)

        # next player
        player = (player + 1) % players

#    print(scores)
    print("Max score is : %d" % ( max(scores) ))

# main
run()
