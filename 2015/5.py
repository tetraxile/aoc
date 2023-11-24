def part_1(data: str) -> str:
    nice_count = 0
    for line in data.split("\n"):
        vowel_count = 0
        for letter in line:
            if letter in "aeiou":
                vowel_count += 1

        if vowel_count < 3:
            continue

        prev_letter = None
        has_double_letter = False
        for letter in line:
            if letter == prev_letter:
                has_double_letter = True
                break
            prev_letter = letter
        
        if not has_double_letter:
            continue

        bad_substr = False
        for substr in ("ab", "cd", "pq", "xy"):
            if substr in line:
                bad_substr = True
                break

        if bad_substr:
            continue

        nice_count += 1

    return nice_count


def part_2(data: str) -> str:
    nice_count = 0
    for line in data.split("\n"):
        double_pair = False
        for i in range(len(line)-1):
            pair = line[i:i+2]
            if line.count(pair) >= 2:
                double_pair = True
                break

        double_letter = False
        for i in range(len(line)-2):
            if line[i] == line[i+2]:
                double_letter = True
                break

        if double_pair and double_letter:
            nice_count += 1

    return nice_count
