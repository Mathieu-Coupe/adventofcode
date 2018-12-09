#!/usr/bin/python

import sys

with open("input") as f:
    content = f.read().replace('\n','')

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

            # cC or Cc
            if content[n] != content[n+1] and content[n].upper() == content[n+1].upper():
                # if result is empty, skip next line
                skip_next = True
            else:
                new_content += content[n]

        # update content
        content = new_content

    return content


def find_all_parts(content):
    # convert to lower case
    content = content.lower()

    # remove all duplicates
    return set(content)

print("Candidates :")

# start from short polymer
content = process_polymer(content)

for letter in find_all_parts(content):
    # remove letters from chain and react
    candidate = process_polymer(content.replace(letter, '').replace(letter.upper(), ''))

    print("Candidate for letter %s is %d long" % (letter, len(candidate)))

    
