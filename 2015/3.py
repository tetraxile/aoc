from util import *


def part_1(data: str) -> str:
    pos = Vec2(0, 0)
    houses = {pos.tuple()}

    for c in data:
        if c == "^":
            pos.y += 1
        elif c == "v":
            pos.y -= 1
        elif c == ">":
            pos.x += 1
        elif c == "<":
            pos.x -= 1

        houses.add(pos.tuple())

    return len(houses)


def part_2(data: str) -> str:
    santa_pos = Vec2(0, 0)
    robo_pos = Vec2(0, 0)
    houses = {santa_pos.tuple(), robo_pos.tuple()}

    is_robo = False

    for c in data:
        pos = robo_pos if is_robo else santa_pos

        if c == "^":
            pos.y += 1
        elif c == "v":
            pos.y -= 1
        elif c == ">":
            pos.x += 1
        elif c == "<":
            pos.x -= 1

        houses.add(pos.tuple())

        is_robo = not is_robo

    return len(houses)
