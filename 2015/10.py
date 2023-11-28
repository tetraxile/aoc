def part_1(data: str) -> str:
    digits = data
    next_digits = ""
    for i in range(40):
        prev_char = digits[0]
        run_length = 0
        for char in digits + "x":
            if char == prev_char:
                run_length += 1
            else:
                next_digits += f"{run_length}{prev_char}"
                run_length = 1

            prev_char = char

        digits = next_digits
        next_digits = ""

    return len(digits)


def part_2(data: str) -> str:
    digits = data
    next_digits = ""
    for i in range(50):
        prev_char = digits[0]
        run_length = 0
        for char in digits + "x":
            if char == prev_char:
                run_length += 1
            else:
                next_digits += f"{run_length}{prev_char}"
                run_length = 1

            prev_char = char

        digits = next_digits
        next_digits = ""

    return len(digits)
