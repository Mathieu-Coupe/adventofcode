#!/usr/bin/python

import sys
import numpy
from parse import compile

with open("input") as f:
    content = f.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
items = [x.strip() for x in content]

# sort array by time
items = numpy.sort(items)

# example : 
# [1518-07-18 23:57] Guard #157 begins shift
# [1518-04-18 00:44] wakes up
# [1518-10-26 00:20] falls asleep
# [1518-10-12 00:32] falls asleep
# [1518-04-12 00:03] Guard #2857 begins shift
# [1518-08-14 23:52] Guard #331 begins shift

# parsing expression
new_shift = compile("[{}] Guard #{} begins shift")
wakes_up = compile("[{} 00:{}] wakes up")
falls_asleep = compile("[{} 00:{}] falls asleep")

#dictionary to store guard statistics
guards = {}
current_guard_id = None
current_guard_asleep = None

for item in items:
#    print("Parsing line : %s" % (item))

    # case 1 : new shift
    if "begins shift" in item:
        values = new_shift.parse(item)
#        print("New guard %d begins shift at %s" % (int(values[1]), values[0]))
        current_guard_id = int(values[1])

    if "falls asleep" in item:
        values = falls_asleep.parse(item)
#        print("Guard falls asleep at minute %d" % (int(values[1])))
        current_guard_asleep = int(values[1])

    if "wakes up" in item:
        values = wakes_up.parse(item)
#        print("Guard wakes up at minute %d" % (int(values[1])))
        current_guard_wakes_up = int(values[1])
#        print("Guard %d has been asleep between %d and %d" % (current_guard_id, current_guard_asleep, current_guard_wakes_up))

        if current_guard_id in guards:
            guard_stats = guards[current_guard_id]
        else:
            guard_stats = numpy.zeros(60, dtype=int)

        # update guard stats
        for n in range(current_guard_asleep, current_guard_wakes_up):
            guard_stats[n] += 1
        
        # store back result in dict
        guards[current_guard_id] = guard_stats

# find which guard has the most frequent minute of sleep
def calculate(item):
    # count total sleep
    minutes_of_sleep = numpy.sum(item[1])
    return { minutes_of_sleep: item[0] }

stats = map(lambda x: calculate(x), guards.items())

#stats = map(lambda x: {numpy.bincount(x[1]) : x[0]}, guards.items())
guard_id = max(stats).values()[0]
guard_max_sleep_minute = numpy.argmax(guards[guard_id])

print("Result is %d (the minute %d for guard %d)" % (guard_id * guard_max_sleep_minute, guard_max_sleep_minute, guard_id))
