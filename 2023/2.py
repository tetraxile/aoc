from util import *


def part_1(data: str) -> str:
    total = 0
    bag = {"red": 12, "green": 13, "blue": 14}
    for line in data.split("\n"):
        game_id, subsets = line.removeprefix("Game ").split(": ")
        game_id = int(game_id)
        subsets = [[cube.split() for cube in subset.split(", ")] for subset in subsets.split("; ")]

        if any(int(count) > bag[colour] for subset in subsets for count, colour in subset):
            continue

        total += game_id

    return total
                

def part_2(data: str) -> str:
    total = 0
    for line in data.split("\n"):
        game_id, subsets = line.removeprefix("Game ").split(": ")
        game_id = int(game_id)
        subsets = [[cube.split() for cube in subset.split(", ")] for subset in subsets.split("; ")]

        min_cubes = {"red": 0, "green": 0, "blue": 0}

        for subset in subsets:
            for count, colour in subset:
                count = int(count)
                if count > min_cubes[colour]:
                    min_cubes[colour] = count

        total += product(min_cubes.values())

    return total
