def part_1(data: str) -> str:
    total = 0
    for line in data.split("\n"):
        first_num = None
        last_num = 0
        for char in line:
            if char.isnumeric() and first_num is None:
                first_num = char
            if char.isnumeric():
                last_num = char

        num = int(first_num + last_num)
        total += num

    return total


def part_2(data: str) -> str:
    total = 0
    digits = "123456789"
    names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in data.split("\n"):
        first_digit = None
        last_digit = None

        for i, char in enumerate(line):
            if first_digit is None:
                if char in digits:
                    first_digit = char
                else:
                    for name in names:
                        if char == name[0] and i + len(name) <= len(line) and line[i:i+len(name)] == name:
                            first_digit = str(names.index(name) + 1)

            if char in digits:
                last_digit = char
            else:
                for name in names:
                    if char == name[0] and i + len(name) <= len(line) and line[i:i+len(name)] == name:
                        last_digit = str(names.index(name) + 1)
        
        num = int(first_digit + last_digit)
        total += num

    return total
