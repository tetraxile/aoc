def check_password(password: str) -> bool:
    for letter in "iol":
        if letter in password:
            return False

    increasing_straight = False
    for subseq in [password[i:i+3] for i in range(len(password)-2)]:
        if ord(subseq[1]) - ord(subseq[0]) == 1 and ord(subseq[2]) - ord(subseq[1]) == 1:
            increasing_straight = True
            break

    if not increasing_straight:
        return False

    pairs = [password[i:i+2] for i in range(len(password)-1)]
    i = 0
    pair_count = 0
    while i < len(pairs):
        pair = pairs[i]
        if pair[0] == pair[1]:
            pair_count += 1
            i += 1
        i += 1

    return pair_count >= 2


def next_password(password: str) -> str:
    password = list(password)
    for i in range(-1, -len(password)-1, -1):
        if password[i] != "z":
            password[i] = chr(ord(password[i]) + 1)
            return "".join(password)
        password[i] = "a"

    assert False


def part_1(data: str) -> str:
    password = data
    while not check_password(password):
        password = next_password(password)

    return password


def part_2(data: str) -> str:
    password = data
    while not check_password(password):
        password = next_password(password)

    password = next_password(password)
    while not check_password(password):
        password = next_password(password)

    return password
