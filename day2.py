"""Day 2: Inventory Management System

https://adventofcode.com/2018/day/2
"""

import itertools

from questions import day2 as question

parsed_question = question.strip().splitlines()


def part1() -> int:
    """To make sure you didn't miss any, you scan the likely candidate boxes
    again, counting the number that have an ID containing exactly two of any
    letter and then separately counting those with exactly three of any letter.
    You can multiply those two counts together to get a rudimentary checksum
    and compare it to what your device predicts.

    What is the checksum for your list of box IDs?
    """
    two_letter_count = 0
    three_letter_count = 0

    for box_id in parsed_question:
        letters = set(box_id)
        has_two_letters = False
        has_three_letters = False
        for letter in letters:
            count = box_id.count(letter)
            if count == 2:
                has_two_letters = True
            elif count == 3:
                has_three_letters = True

        two_letter_count += has_two_letters
        three_letter_count += has_three_letters

    return two_letter_count * three_letter_count


def part2() -> str:
    """The boxes will have IDs which differ by exactly one character at the
    same position in both strings.

    What letters are common between the two correct box IDs?
    """
    for x, y in itertools.combinations(parsed_question, 2):
        last_difference = None  # index of letter
        for i in range(len(x)):
            if x[i] != y[i]:
                if last_difference is not None:
                    break
                last_difference = i
        else:
            assert last_difference is not None
            return x[:last_difference] + x[last_difference + 1:]

    assert False  # Otherwise, mypy: missing return statement!


print("Day 2, part 1 answer:", part1())
print("Day 2, part 2 answer:", part2())
