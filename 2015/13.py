from itertools import permutations


def part_1(data: str) -> str:
    lut = {}
    for line in data.split("\n"):
        p1, tmp = line.split(" would ")
        tmp, p2 = tmp[:-1].split(" happiness units by sitting next to ")
        sign, amount = tmp.split(" ")
        change = int(amount) * (-1 if sign == "lose" else 1)

        if p1 not in lut:
            lut[p1] = {}

        lut[p1][p2] = change

    names = list(lut)
    best = float("-inf")
    for perm in permutations(names):
        total = 0
        for i in range(0, -len(perm), -1):
            p1 = perm[i]
            p2 = perm[i-1]
            total += lut[p1][p2] + lut[p2][p1]
        best = max(best, total)

    return best


def part_2(data: str) -> str:
    lut = {}
    for line in data.split("\n"):
        p1, tmp = line.split(" would ")
        tmp, p2 = tmp[:-1].split(" happiness units by sitting next to ")
        sign, amount = tmp.split(" ")
        change = int(amount) * (-1 if sign == "lose" else 1)

        if p1 not in lut:
            lut[p1] = {}

        lut[p1][p2] = change

    names = list(lut) + ["tetra"]
    lut["tetra"] = {}

    for name in names:
        lut[name]["tetra"] = 0
        lut["tetra"][name] = 0

    best = float("-inf")
    for perm in permutations(names):
        total = 0
        for i in range(0, -len(perm), -1):
            p1 = perm[i]
            p2 = perm[i-1]
            total += lut[p1][p2] + lut[p2][p1]
        best = max(best, total)

    return best
