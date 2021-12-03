with open("input", "r") as f:
    lines = f.readlines()

def part_1():
    h = 0
    d = 0
    aim = 0
    for line in lines:
        data = line.split()
        direc = data[0]
        x = int(data[1])
        if direc == "forward":
            h += x
        elif direc == "down":
            d += x
        elif direc == "up":
            d -= x
    return h*d


def part_2():
    h = 0
    d = 0
    aim = 0
    for line in lines:
        data = line.split()
        direc = data[0]
        x = int(data[1])
        if direc == "forward":
            h += x
            d += x * aim
        elif direc == "down":
            aim += x
        elif direc == "up":
            aim -= x
    return h*d


print("part 1:", part_1())
print("part 2:", part_2())
