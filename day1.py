"""Day 1: Chronal Calibration

https://adventofcode.com/2018/day/1
"""

from questions import day1 as question

parsed_question = [int(line) for line in question.strip().splitlines()]


def part1() -> int:
    """Starting with a frequency of zero, what is the resulting frequency after
    all of the changes in frequency have been applied?
    """
    return sum(parsed_question)


def part2() -> int:
    """What is the first frequency your device reaches twice?"""
    current_frequency = 0
    past_frequencies = {0}
    while True:
        for n in parsed_question:
            new = current_frequency + n
            if new in past_frequencies:
                return new
            past_frequencies.add(new)
            current_frequency = new


print("Day 1, part 1 answer:", part1())
print("Day 1, part 2 answer:", part2())
