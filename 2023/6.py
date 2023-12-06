from util import *

def part_1(data: str) -> str:
    lines = data.split("\n")
    times = ints(lines[0].split(":")[1])
    records = ints(lines[1].split(":")[1])

    total = 1
    for time, record in zip(times, records):
        wins = 0
        for start_time in range(time+1):
            move_time = time - start_time
            distance = move_time * start_time
            wins += distance > record

        total *= wins

    return total


def part_2(data: str) -> str:
    lines = data.split("\n")
    time = int(lines[0].split(":")[1].replace(" ", ""))
    record = int(lines[1].split(":")[1].replace(" ", ""))

    discriminant = math.sqrt(time**2 - 4*record)
    wins = 2 * math.floor(discriminant/2) + 1 + time % 2

    return wins
