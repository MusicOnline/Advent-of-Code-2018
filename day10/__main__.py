"""Day 10: The Stars Align

https://adventofcode.com/2018/day/10
"""

import itertools
import re
from typing import Optional

import matplotlib.pyplot as plt

with open("data.txt") as f:
    question: str = f.read()

pattern: str = r"(-?\d+)"
points: list = []

for line in question.strip().splitlines():
    match: list = re.findall(pattern, line)
    points.append(tuple(int(n) for n in match))


def get_points(seconds: int) -> tuple:
    xs: list = []
    ys: list = []

    for p in points:
        x: int = p[0] + p[2] * seconds
        y: int = p[1] + p[3] * seconds
        xs.append(x)
        ys.append(y)

    return xs, ys


def display(args: tuple) -> None:
    i, xs, max_x, delta_x, ys, max_y, delta_y, _ = args

    fig, ax = plt.subplots()
    fig.canvas.set_window_title("Advent of Code 2018 - Day 10")

    plt.plot(xs, ys, "o")
    plt.title(f"{i} seconds")

    delta: int

    if delta_x > delta_y:
        delta = delta_x
    else:
        delta = delta_y

    plt.axis("off")
    plt.xlim(max_x - delta - 1, max_x + 1)
    plt.ylim(max_y - delta - 1, max_y + 1)

    plt.show()


last_diff: Optional[tuple] = None

for i in itertools.count():
    xs, ys = get_points(i)

    max_x: int = max(xs)
    max_y: int = max(ys)
    delta_x: int = max_x - min(xs)
    delta_y: int = max_y - min(ys)

    diff: int = delta_x + delta_y

    if last_diff is None or diff < last_diff[-1]:
        last_diff = (i, xs, max_x, delta_x, ys, max_y, delta_y, diff)
    else:
        assert last_diff is not None
        display(last_diff)
        break
