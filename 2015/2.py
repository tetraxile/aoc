def part_1(data: str) -> str:
    total = 0
    for line in data.split("\n"):
        l, w, h = map(int, line.split("x"))

        surface_area = 2*l*w + 2*w*h + 2*h*l
        min_l, min_w = sorted((l, w, h))[:2]
        extra = min_l * min_w

        total += surface_area + extra

    return total

def part_2(data: str) -> str:
    total = 0
    for line in data.split("\n"):
        l, w, h = map(int, line.split("x"))

        min_l, min_w = sorted((l, w, h))[:2]
        perimeter = 2 * (min_l + min_w)
        volume = l * w * h

        total += perimeter + volume

    return total
