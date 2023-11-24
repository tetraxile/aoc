def part_1(data: str) -> str:
    floor = 0
    for char in data:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

    return floor

def part_2(data: str) -> str:
    floor = 0
    for pos, char in enumerate(data):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        
        if floor == -1:
            return pos + 1
