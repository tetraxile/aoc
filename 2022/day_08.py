import numpy as np

with open("input") as f:
    l = f.read().strip().split("\n")
    w, h = len(l[0].strip()), len(l)

    grid = np.empty((h, w), dtype=np.uint8)
    for r, line in enumerate(l):
        for c, char in enumerate(line.strip()):
            grid[r, c] = int(char)


def is_visible(y: int, x: int) -> bool:
    height = grid[y, x]
    to_edges = (grid[y, :x], grid[:y, x], grid[y, x+1:], grid[y+1:, x])

    return any(len(path) == 0 or max(path) < height for path in to_edges)


def scenic_score(y: int, x: int) -> int:
    height = grid[y, x]
    lines_of_sight = (grid[y, :x][::-1], grid[:y, x][::-1], grid[y, x+1:], grid[y+1:, x])

    score = 1
    for line in lines_of_sight:
        distance = 0
        for tree in line:
            distance += 1
            if tree >= height:
                break
        score *= distance
    
    return score


def part_1():
    h, w = grid.shape
    return sum(is_visible(r, c) for r in range(h) for c in range(w))


def part_2():
    h, w = grid.shape
    out = 0

    for r in range(h):
        for c in range(w):
            out = max(out, scenic_score(r, c))
        
    return out


print("part 1:", part_1())
print("part 2:", part_2())
