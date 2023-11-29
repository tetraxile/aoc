from itertools import combinations


def part_1(data: str) -> str:
    containers = list(sorted((int(line) for line in data.split("\n")), reverse=True))
    n = 150
    combs = [c for k in range(1, len(containers)+1) for c in combinations(containers, k) if sum(c) == n]
    return len(combs)


def part_2(data: str) -> str:
    containers = list(sorted((int(line) for line in data.split("\n")), reverse=True))
    n = 150
    combs = [c for k in range(1, len(containers)+1) for c in combinations(containers, k) if sum(c) == n]
    min_length = min(map(len, combs))

    return len(list(filter(lambda k: len(k) == min_length, combs)))
