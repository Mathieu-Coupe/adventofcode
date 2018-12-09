#!/usr/bin/python

import sys

with open("input") as f:
    content = f.read().replace('\n','')

def combine(a, b):
    # cC or Cc
    if a != b and a.upper() == b.upper():
        return ""

    return a

print("Processing, initial size is %d" % (len(content)))

def process_polymer(content):
    previous_size = 0
    while previous_size != len(content):
#       print("New iteration : %s" % (content))

        # save old size
        previous_size = len(content)
        new_content = ""
        skip_next = False

        # add empty char at end for easy looping
        content += " "

        # combine elements
        for n in range(0, len(content) - 1):
            if skip_next:
#                print("skipping iteration")
                skip_next = False
                continue

#            print("Reacting %s and %s --> %s" % (content[n], content[n+1], combine(content[n], content[n+1])))
            reacted = combine(content[n], content[n+1])

            # if result is empty, skip next line
            if reacted == "":
                skip_next = True

            new_content += reacted

        # update content
        content = new_content

    return content

content = process_polymer(content)
print("Final size is %d" % (len(content)))
