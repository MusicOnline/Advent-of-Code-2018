"""Day 9: Marble Mania

https://adventofcode.com/2018/day/9
"""

import collections
import re
from typing import Deque, Dict, Generator, Match, Optional

from questions import day9 as question

pattern: str = r"(\d+?) players; last marble is worth (\d+?) points"
match: Optional[Match] = re.match(pattern, question)

assert match is not None
args: Generator[int, None, None] = (int(x) for x in match.groups())

players: int = next(args)
last_marble: int = next(args)


def get_high_score(players: int, last_marble: int) -> int:
    """"""
    circle: Deque[int] = collections.deque([0])
    scores: Dict[int, int] = {n: 0 for n in range(players)}

    for marble in range(1, last_marble + 1):

        if marble % 23 == 0:
            circle.rotate(-7)
            scores[marble % players] += marble + circle.pop()
            continue

        circle.rotate(2)
        circle.append(marble)

    return max(scores.values())


print("Day 9, part 1 answer:", get_high_score(players, last_marble))
print("Day 9, part 2 answer:", get_high_score(players, last_marble * 100))
