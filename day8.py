"""Day 8: Memory Maneuver

https://adventofcode.com/2018/day/8
"""

import functools
import operator
from typing import Any, Dict, Hashable, Tuple

from questions import day8 as question


numbers = [int(n) for n in question.strip().split()]
nodes = []  # List of (num of childs, num of metadata, metadata entries)
child_nodes_left: Dict[int, int] = {}
structure: dict = {}


def nested_get(d: dict, keys: Tuple[Hashable, ...]) -> Any:
    return functools.reduce(operator.getitem, keys, d)


def nested_set(d: dict, keys: Tuple[Hashable, ...], value: Any) -> None:
    for key in keys[:-1]:
        d = d.setdefault(key, {})
    d[keys[-1]] = value


# Apparently Tuple[None] != Tuple[Hashable, ...]? Mypy?

def get_node(  # type: ignore
        index: int = 0,
        path: Tuple[Hashable, ...] = (None,)) -> int:
    """What is the sum of all metadata entries?

    Part 1 of day 8.
    """
    num_children = numbers[index]
    num_metadata = numbers[index + 1]

    try:
        num_children_left = child_nodes_left[index]
    except KeyError:
        child_nodes_left[index] = num_children
        num_children_left = num_children

    if num_children_left == 0:
        if index != 0:
            child_nodes_left[index - 2] -= 1

        node = (
            num_children,
            num_metadata,
            numbers[index + 2:index + 2 + num_metadata])
        nodes.append(node)

        nested_set(structure, path + ("value",), node)

        del numbers[index:index + 2 + num_metadata]
        child_nodes_left.pop(index)
    else:
        # Recursively go down a branch and parse it.
        get_node(index + 2, path + (num_children - num_children_left + 1,))
        # Check current node again if children are parsed.
        get_node(index, path)

    return sum(sum(node[2]) for node in nodes)


def get_node_value(  # type: ignore
        path: Tuple[Hashable, ...] = (None,)) -> int:
    """What is the value of the root node?

    If a node has no child nodes, its value is the sum of its metadata entries.
    So, the value of node B is 10+11+12=33, and the value of node D is 99.

    However, if a node does have child nodes, the metadata entries become
    indexes which refer to those child nodes. A metadata entry of 1 refers to
    the first child node, 2 to the second, 3 to the third, and so on. The value
    of this node is the sum of the values of the child nodes referenced by the
    metadata entries. If a referenced child node does not exist, that reference
    is skipped. A child node can be referenced multiple time and counts each
    time it is referenced. A metadata entry of 0 does not refer to any child
    node.

    Part 2 of day 8.
    """
    total = 0
    d = nested_get(structure, path)
    if 1 not in d:
        total += sum(d["value"][2])
    else:
        nodes_to_add = d["value"][2]
        for n in nodes_to_add:
            if n in d:
                total += get_node_value(path + (n, ))

    return total


print("Day 8, part 1 answer:", get_node())
print("Day 8, part 2 answer:", get_node_value())
