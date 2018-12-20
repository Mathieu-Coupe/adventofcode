#!/usr/bin/python

import sys
import numpy
from parse import compile
from collections import defaultdict

with open("input") as f:
    content = f.read().replace('\n','').split(' ')

def read_node(elements):
#    print("Read node from %s" % (elements))
    nb_child_nodes = int(elements[0])
    nb_metadata = int(elements[1])

#    print("header[%d,%d]" % (nb_child_nodes, nb_metadata))
    childs = []
    metadata = []
    size = 2 # header
    if nb_child_nodes > 0:
        for n in range(nb_child_nodes):
#            print("Reading child %d" % n)
            child, read_size = read_node(elements[size:])
            childs.append(child)
            size += read_size

    metadata = map(int, elements[size: size+nb_metadata])
#    print("metadata = %s" % metadata)
    size += nb_metadata
#    print("total size = %d" % size)
    return dict(childs= childs, metadata= metadata), size

def sum_metadata(node):
    if len(node['childs']) == 0:
        # no child, count only metadata
        return reduce((lambda x, y: x + y), node['metadata'])

    total = 0
    # process childs
    for n in node['metadata']:
        if n > 0 and n <= len(node['childs']):
            total += sum_metadata(node['childs'][n-1])

    return total

root, total_size = read_node(content)
print("root = %s" % (root))
print("total_size = %d" % (total_size))
print("metadatasum = %d" % sum_metadata(root))
