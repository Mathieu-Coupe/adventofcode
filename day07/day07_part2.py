#!/usr/bin/python

import sys
import numpy
from parse import compile
from collections import defaultdict

num_workers = 5
timer = 0
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

class Worker:
  def __init__(self):
    self.step = ''
    self.work = 0

  def start(self, step):
    self.step = step
    self.work = ord(step) - 4

  def do_work(self):
    self.work = self.work -1

  def work_is_finished(self):
    return self.work == 0

  def is_idle(self):
      return self.step == ''

  def set_idle(self):
      self.step = ''
      self.work = 0

  def __str__(self):
    return "%s [%d]" % (self.step, self.work)

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

def all_workers_are_busy(workers):
    for worker in workers:
        if not worker.is_idle():
            return True

    return False

# all idle workers
workers = [Worker() for x in range(num_workers) ]

print("Second\tWorkers\tDone")
while len(steps) > 0 or all_workers_are_busy(workers):
    # advance global tick
    for worker in workers:
        worker.do_work()
        if worker.work_is_finished():
            # add step to done
            done_steps.append(worker.step)

            # remove requirement in other steps
            for step in steps:
                steps[step] = list(filter(lambda x : x != worker.step, steps[step]))

            # worker is now idle
            worker.set_idle()

    # list all available steps
    available_steps = sorted(list(filter(step_available, steps)))

    # check if an idle worker is present
    for step_to_complete in available_steps:
        for worker in workers:
            if worker.is_idle():
                worker.start(step_to_complete)

                # remove step
                del steps[worker.step]

                break

    print("%d\t%s\t%s" % (timer, '\t'.join(map(lambda x : x.step, workers)), ''.join(done_steps)))
    timer += 1



