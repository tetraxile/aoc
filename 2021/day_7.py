with open("input", "r") as f:
    crabs = [int(a) for a in f.readline().strip().split(",")]


def part_1():
    bestpos = float("inf")
    for i in range(min(crabs), max(crabs)+1):
        dists = [abs(c - i) for c in crabs]
        if sum(dists) < bestpos:
            bestpos = sum(dists)
    return bestpos


def part_2():
    bestpos = float("inf")
    for i in range(min(crabs), max(crabs)+1):
        dists = [(abs(c - i))*(abs(c - i)+1)//2 for c in crabs]
        if sum(dists) < bestpos:
            bestpos = sum(dists)
    return bestpos


print("part 1:", part_1())
print("part 2:", part_2())
