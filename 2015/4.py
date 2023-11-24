from hashlib import md5

def part_1(data: str) -> str:
    i = 1
    while True:
        test = data + str(i)
        test_hash = md5(test.encode()).hexdigest()
        if test_hash.startswith("00000"):
            break

        i += 1

    return i


def part_2(data: str) -> str:
    i = 1
    while True:
        test = data + str(i)
        test_hash = md5(test.encode()).hexdigest()
        if test_hash.startswith("000000"):
            break

        i += 1

    return i
