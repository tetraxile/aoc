with open("input") as f:
    stream = f.read().strip()


def find_marker(n: int):
    for i in range(n, len(stream)):
        if len(set(stream[i-n:i])) == n:
            return i


print("part 1:", find_marker(4))
print("part 2:", find_marker(14))
