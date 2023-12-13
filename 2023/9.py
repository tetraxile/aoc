from util import *

def part_1(data: str) -> str:
    total = 0
    for line in data.split("\n"):
        sequences = [ints(line)]
        while any(t != 0 for t in sequences[-1]):
            sequences.append([b-a for a, b in windows(sequences[-1], 2)])
        
        sequences[-1].append(0)
        for i in range(len(sequences) - 2, -1, -1):
            sequences[i].append(sequences[i][-1] + sequences[i+1][-1])

        total += sequences[0][-1]

    return total

def part_2(data: str) -> str:
    total = 0
    for line in data.split("\n"):
        sequences = [ints(line)]
        while any(t != 0 for t in sequences[-1]):
            sequences.append([b-a for a, b in windows(sequences[-1], 2)])
        
        sequences[-1].insert(0, 0)
        for i in range(len(sequences) - 2, -1, -1):
            sequences[i].insert(0, sequences[i][0] - sequences[i+1][0])

        total += sequences[0][0]

    return total
