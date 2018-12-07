"""Day 7: The Sum of Its Parts

https://adventofcode.com/2018/day/7

Each part of the question was not separated into its own function as they can
be done in the same loop.
"""

import re
from string import ascii_uppercase
from typing import Dict, Optional, Set, Tuple

from questions import day7 as question

pattern = r"Step (.) must be finished before step (.) can begin\."
steps: Dict[str, Set[str]] = {}  # Mapping of step: requirements.
correct_steps = []

# For part 2.
workers: Dict[int, Optional[Tuple[str, int]]] = {n: None for n in range(5)}

# Parse question input.
for line in question.strip().splitlines():
    match = re.match(pattern, line)
    assert match is not None
    if match.group(2) not in steps:
        steps[match.group(2)] = set()

    steps[match.group(2)].add(match.group(1))

# Find first step.
for letter in ascii_uppercase:
    if letter not in steps:
        correct_steps.append(letter)
        total_time = 60 + ascii_uppercase.index(letter) + 1
        break

while steps:
    shortest_time_left = None

    # Find shortest time left, for part 2.
    for worker, value in workers.items():
        if value is None:
            continue
        step, time_left = value
        if shortest_time_left is None or time_left < shortest_time_left:
            shortest_time_left = time_left

    # Continue flow of time, for part 2.
    total_time += shortest_time_left or 0

    # Subtract time left from current tasks, for part 2.
    for worker, value in workers.items():
        if value is None:
            continue
        step, time_left = value
        if time_left == shortest_time_left:
            correct_steps.append(step)
            steps.pop(step, None)
            workers[worker] = None
        else:
            workers[worker] = (step, time_left - (shortest_time_left or 0))

    available_steps = []

    # Gather all available steps to process next.
    for step, required_steps in steps.items():

        # Make mypy ignore this line because it thinks x is not indexable,
        # even with the if statement at the end of the list comprehension.
        steps_in_processing = [
            x[0] for x in workers.values() if x is not None]  # type: ignore

        if (set(correct_steps) >= required_steps
                and step not in steps_in_processing):
            available_steps.append(
                (step, 60 + ascii_uppercase.index(step) + 1))

    # Assign steps to workers, for part 2.
    if available_steps:
        available_steps.sort(key=lambda tup: tup[0])
        gen_available_steps = (x for x in available_steps)

        for w in range(len(workers)):
            if workers[w] is None:
                try:
                    workers[w] = next(gen_available_steps)
                except StopIteration:
                    break


print("Day 7, part 1 answer:", "".join(correct_steps))
print("Day 7, part 2 answer:", total_time)
