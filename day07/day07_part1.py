#!/usr/bin/python

import sys
import numpy
from parse import compile
from collections import defaultdict

with open("input") as f:
    content = f.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
items = [x.strip() for x in content]

# sample : Step A must be finished before step B can begin.
# parse compile
p = compile("Step {} must be finished before step {} can begin.")

# array to storeteps
steps = defaultdict(list)
all_steps = set()

for item in items:
    # parse
    requirement, step = p.parse(item)
    
    # add step to list of all steps
    all_steps.add(step)
    all_steps.add(requirement)

    # add requirement to step
    steps[step].append(requirement)

all_steps = sorted(all_steps)

# add steps with no requirements
for step in all_steps:
    # accessing the item will create an empty list
    steps[step]

print(all_steps)
print(steps)

# list of al done steps
done_steps = []

def step_available(step):
    # check requirements for the step
    for req in steps[step]:
#        print("Check requirement %s of step %s" % (req, step))
        if req not in done_steps:
#            print("Requirement %s is not ready" % (req))
            return False

    return True

while len(steps) > 0:
    # list all available steps
    available_steps = sorted(list(filter(step_available, steps)))
    step_completed = available_steps.pop(0)

    # add step to done
    done_steps.append(step_completed)

    # remove step
    del steps[step_completed]

    # remove requirement in other steps
    for step in steps:
        steps[step] = list(filter(lambda x : x != step_completed, steps[step]))

#    print(done_steps)
#    print(steps)

print(''.join(done_steps))
