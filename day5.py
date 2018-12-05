"""Day 5: Alchemical Reduction

https://adventofcode.com/2018/day/5
"""

from string import ascii_lowercase
from typing import List

from questions import day5 as question


def part1(parsed_question: List[str]) -> int:
    """The polymer is formed by smaller units which, when triggered, react with
    each other such that two adjacent units of the same type and opposite
    polarity are destroyed. Units' types are represented by letters; units'
    polarity is represented by capitalization.

    How many units remain after fully reacting the polymer you scanned?
    """
    while True:
        to_pop: List[int] = []
        for i in range(len(parsed_question) - 1):
            left = parsed_question[i]
            right = parsed_question[i + 1]
            if left in ascii_lowercase and left.upper() == right:
                if i not in to_pop and i + 1 not in to_pop:
                    to_pop.extend([i, i + 1])
            elif left not in ascii_lowercase and left.lower() == right:
                if i not in to_pop and i + 1 not in to_pop:
                    to_pop.extend([i, i + 1])

        if not to_pop:
            return len(parsed_question)

        to_pop.sort(reverse=True)
        for i in to_pop:
            parsed_question.pop(i)


def part2() -> int:
    """What is the length of the shortest polymer you can produce by removing
    all units of exactly one type and fully reacting the result?
    """
    all_lengths = {}
    for char in ascii_lowercase:
        new_strand = [c for c in question if c not in (char, char.upper())]
        all_lengths[char] = part1(new_strand)

    return min(all_lengths.values())


print("Day 5, part 1 answer:", part1(list(question)))
print("Day 5, part 2 answer:", part2())
