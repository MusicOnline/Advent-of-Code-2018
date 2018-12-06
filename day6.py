"""Day 6: Chronal Coordinates

https://adventofcode.com/2018/day/6
"""

from typing import Dict, List, Tuple

from questions import day6 as question

all_coords = []

# Prefer doing a list comprehension, but mypy will think point: Tuple[int, ...]
for c in question.strip().splitlines():
    point = [int(n) for n in c.split(", ")]
    all_coords.append((point[0], point[1]))


def calculate_grid_size(
        coords: List[Tuple[int, int]]) -> Tuple[int, int, int, int]:
    min_x = min(coords, key=lambda c: c[0])[0]
    min_y = min(coords, key=lambda c: c[1])[1]
    max_x = max(coords, key=lambda c: c[0])[0]
    max_y = max(coords, key=lambda c: c[1])[1]

    return min_x, min_y, max_x, max_y


min_x, min_y, max_x, max_y = calculate_grid_size(all_coords)


def part1() -> int:
    """Using only the Manhattan distance, determine the area around each
    coordinate by counting the number of integer X,Y locations that are closest
    to that coordinate (and aren't tied in distance to any other coordinate).

    What is the size of the largest area that isn't infinite?
    """
    coords = list(all_coords)  # copy the list, don't mutate it!

    def calculate_areas(
            coords: List[Tuple[int, int]],
            min_x: int, min_y: int,
            max_x: int, max_y: int) -> Dict[Tuple[int, int], int]:
        coords_and_area = {c: 0 for c in coords}
        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                if (x, y) in coords:
                    coords_and_area[x, y] += 1
                    continue

                manhattan_distances = []
                for cx, cy in coords:
                    manhattan_distances.append(
                        (cx, cy, abs(x - cx) + abs(y - cy)))

                manhattan_distances.sort(key=lambda c: c[2])
                if manhattan_distances[0][2] != manhattan_distances[1][2]:
                    cx, cy = manhattan_distances[0][:2]
                    coords_and_area[cx, cy] += 1

        return coords_and_area

    areas = calculate_areas(coords, min_x, min_y, max_x, max_y)
    areas2 = calculate_areas(coords, min_x, min_y, max_x + 1, max_y + 1)

    for (x, y), area in areas2.items():
        if area != areas[x, y]:
            coords.remove((x, y))

    _min_x, _min_y, _max_x, _max_y = calculate_grid_size(coords)
    areas3 = calculate_areas(coords, _min_x - 1, _min_y - 1, _max_x, _max_y)

    for (x, y), area in areas3.items():
        if area != areas[x, y]:
            coords.remove((x, y))

    area_sizes = [areas[x, y] for x, y in coords]
    return max(area_sizes)


def part2() -> int:
    """For each location, add up the distances to all of the given coordinates;
    if the total of those distances is less than 32, that location is within
    the desired region.

    What is the size of the region containing all locations which have a total
    distance to all given coordinates of less than 10000?

    This solution assumes the coordinates are spread out.
    """
    coords = list(all_coords)

    safe_area = 0
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            manhattan_distances = []
            for cx, cy in coords:
                manhattan_distances.append(abs(x - cx) + abs(y - cy))

            if sum(manhattan_distances) < 10000:
                safe_area += 1

    return safe_area


print("Day 6, part 1 answer:", part1())
print("Day 6, part 2 answer:", part2())
