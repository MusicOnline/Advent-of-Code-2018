"""Day 5: Alchemical Reduction

https://adventofcode.com/2018/day/5
"""

from string import ascii_lowercase
from typing import List, Iterable

from questions import day5 as question


def part1(strand: Iterable[str]) -> int:
    """The polymer is formed by smaller units which, when triggered, react with
    each other such that two adjacent units of the same type and opposite
    polarity are destroyed. Units' types are represented by letters; units'
    polarity is represented by capitalization.

    How many units remain after fully reacting the polymer you scanned?
    """
    stack: List[str] = []
    last_c = None
    for c in strand:
        if (c in ascii_lowercase and c.upper() == last_c
                or c not in ascii_lowercase and c.lower() == last_c):
            stack.pop()
            try:
                last_c = stack[-1]
            except IndexError:
                last_c = None
        else:
            last_c = c
            stack.append(c)

    return len(stack)


def part2() -> int:
    """What is the length of the shortest polymer you can produce by removing
    all units of exactly one type and fully reacting the result?
    """
    shortest = len(question)
    for char in ascii_lowercase:
        new_strand = (c for c in question if c not in (char, char.upper()))
        length = part1(new_strand)
        if length < shortest:
            shortest = length

    return shortest


print("Day 5, part 1 answer:", part1(question))
print("Day 5, part 2 answer:", part2())
