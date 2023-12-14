from util import *
import numpy as np
from itertools import combinations


def part_1(data: str) -> str:
    return puzzle(data, 2)


def part_2(data: str) -> str:
    return puzzle(data, 1000000)


def puzzle(data: str, gap: int) -> str:
    galaxies = []
    grid = np.array([list(line) for line in data.split("\n")])
    empty = {"r": [], "c": []}
    for r, row in enumerate(grid):
        if all(char == "." for char in row):
            empty["r"].append(r)

    for c, col in enumerate(grid.transpose()):
        if all (char == "." for char in col):
            empty["c"].append(c)

    r_offset = 0
    for r, line in enumerate(grid):
        if r in empty["r"]:
            r_offset += gap-1
        c_offset = 0
        for c, char in enumerate(line):
            if c in empty["c"]:
                c_offset += gap-1
            if char == "#":
                galaxies.append((r_offset+r, c_offset+c))

    total = 0
    for (n1, (x1, y1)), (n2, (x2, y2)) in combinations(enumerate(galaxies), 2):
        dist = abs(y2-y1) + abs(x2-x1)
        total += dist

    return total
