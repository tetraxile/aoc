with open("input") as f:
    l = f.read().split("\n")


def get_priority(item: str) -> int:
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38


def part_1():
    priorities = 0
    for rucksack in l:
        a, b = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        dup, = set(a) & set(b)
        priorities += get_priority(dup)

    return priorities


def part_2():
    priorities = 0
    for group in (l[i:i+3] for i in range(0, len(l), 3)):
        a, b, c = group
        dup, = set(a) & set(b) & set(c)
        priorities += get_priority(dup)

    return priorities


print("part 1:", part_1())
print("part 2:", part_2())
