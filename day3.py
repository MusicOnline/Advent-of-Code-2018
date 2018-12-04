"""Day 3: No Matter How You Slice It

https://adventofcode.com/2018/day/3
"""

import re
from collections import namedtuple
from typing import List

from questions import day3 as question

pattern = r"#(\d+?) @ (\d+?),(\d+?): (\d+?)x(\d+)"
rectangles = []
Rectangle = namedtuple("Rectangle", "id x y width height")

for q in question.strip().splitlines():
    match = re.match(pattern, q)
    assert match is not None
    attrs = [int(m) if m.isdigit() else m for m in match.groups()]
    rectangles.append(Rectangle(*attrs))

grid: List[List[List[int]]] = [
    [[] for j in range(1000)] for i in range(1000)]

for rect in rectangles:
    x1 = rect.x
    x2 = x1 + rect.width
    y1 = rect.y
    y2 = y1 + rect.height
    for row in range(y1, y2):
        for unit in range(x1, x2):
            grid[row][unit].append(rect.id)


def part1() -> int:
    """How many square inches of fabric are within two or more claims?"""
    overlapped = 0
    for row in grid:
        for unit in row:
            if len(unit) >= 2:
                overlapped += 1
    return overlapped


def part2() -> set:
    """What is the ID of the only claim that doesn't overlap?"""
    all_rects = {rect.id for rect in rectangles}
    overlapped = set()
    for row in grid:
        for unit in row:
            if len(unit) >= 2:
                overlapped.update(unit)
    return all_rects.difference(overlapped)


print("Day 3, part 1 answer:", part1())
print("Day 3, part 2 answer:", part2())
