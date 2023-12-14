from functools import reduce
from itertools import combinations, permutations
import math
import operator
import re
import sys
import typing


class Vec2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f"<{self.x}, {self.y}>"

    def tuple(self) -> tuple[int, int]:
        return (self.x, self.y)

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vec2(self.x * scalar, self.y * scalar)

    def mag(self) -> float:
        return math.sqrt(self.dot(self))

    def dot(self, other) -> int:
        return self.x * other.x + self.y * other.y


class Vec3:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def __repr__(self) -> str:
        return f"<{self.x}, {self.y}, {self.z}>"

    def tuple(self) -> tuple[int, int]:
        return (self.x, self.y, self.z)

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)

    def mag(self) -> float:
        return math.sqrt(self.dot(self))

    def dot(self, other) -> int:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vec3(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x
        )


def product(it) -> int | float:
    return reduce(operator.mul, it, 1)


def adjacents(r: int, c: int) -> list[tuple[int, int]]:
    return [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c+1), (r+1, c+1), (r+1, c), (r+1, c-1), (r, c-1)]


def ints(s: str) -> list[int]:
    pattern = re.compile(r"(-?\d+)")
    return list(map(int, pattern.findall(s)))


def chunks(it: list, size: int):
    for i in range(0, len(it), size):
        yield it[i:i+size]


def windows(it: typing.Iterable, size: int) -> typing.Iterator:
    for i in range(len(it) - size + 1):
        yield it[i:i+size]


def count_unique(it: typing.Iterable) -> dict:
    counts = {}
    for item in it:
        if item not in counts:
            counts[item] = 1
        else:
            counts[item] += 1

    return counts
