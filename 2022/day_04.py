with open("input") as f:
    l = f.read().strip().split("\n")


def part_1():
    contained = 0

    for pair in l:
        a, b = map(lambda k: list(map(int, k.split("-"))), pair.split(","))

        if b[0] <= a[0] and b[1] >= a[1] or b[0] >= a[0] and b[1] <= a[1]:
            contained += 1

    return contained


def part_2():
    overlap = 0

    for pair in l:
        a, b = map(lambda k: list(map(int, k.split("-"))), pair.split(","))

        for i in range(a[0], a[1]+1):
            if b[0] <= i <= b[1]:
                overlap += 1
                break

    return overlap


print("part 1:", part_1())
print("part 2:", part_2())
