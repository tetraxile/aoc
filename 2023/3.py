from util import *


def part_1(data: str) -> str:
    numbers: list[tuple[int, list[tuple[int, int]]]] = []
    symbols: dict[tuple[int, int], str] = {}
    for r, line in enumerate(data.split("\n")):
        num = ""
        positions = []
        for c, char in enumerate(line):
            if char.isnumeric():
                num += char
                positions.append((r, c))
            elif len(num) != 0:
                numbers.append((int(num), positions))
                num = ""
                positions = []

            if char != "." and not char.isnumeric():
                symbols[(r, c)] = char

        if len(num) != 0:
            numbers.append((int(num), positions))

    total = 0

    for num, positions in numbers:
        if any(adj in symbols for pos in positions for adj in adjacents(*pos)):
            total += num

    return total


def part_2(data: str) -> str:
    numbers: list[tuple[int, list[tuple[int, int]]]] = []
    stars: list[tuple[int, int]] = []
    for r, line in enumerate(data.split("\n")):
        num = ""
        positions = []
        for c, char in enumerate(line):
            if char.isnumeric():
                num += char
                positions.append((r, c))
            elif len(num) != 0:
                numbers.append((int(num), positions))
                num = ""
                positions = []

            if char == "*":
                stars.append((r, c))

        if len(num) != 0:
            numbers.append((int(num), positions))

    total = 0

    for star_pos in stars:
        adjacent_numbers = []
        adjs = adjacents(*star_pos)
        for number, positions in numbers:
            if any(adj in positions for adj in adjs):
                adjacent_numbers.append(number)
       
        if len(adjacent_numbers) == 2:
            total += product(adjacent_numbers)

    return total
