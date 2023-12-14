from util import *
import enum
import numpy as np

def part_1(data: str) -> str:
    lines = data.split("\n")
    h, w = len(lines), len(lines[0])
    grid = np.empty((h, w), dtype=object)
    start = None

    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == "S":
                start = (r, c)
                continue

            grid[r, c] = {
                "|": [(r-1, c), (r+1, c)],
                "-": [(r, c-1), (r, c+1)],
                "L": [(r-1, c), (r, c+1)],
                "J": [(r-1, c), (r, c-1)],
                "7": [(r, c-1), (r+1, c)],
                "F": [(r, c+1), (r+1, c)],
                ".": []
            }[char]

    grid[start] = [adj for adj in adjacents(*start) if start in grid[adj]]

    pos = start
    history = {pos}
    while True:
        dirs = list(filter(lambda adj: adj not in history, grid[pos]))
        if len(dirs) == 0:
            break

        pos = dirs[0]
        history.add(pos)

    return len(history) // 2


def part_2(data: str) -> str:
    lines = data.split("\n")
    h, w = len(lines), len(lines[0])
    adj_grid = np.empty((h, w), dtype=object)
    pipe_grid = np.empty((h, w), dtype=str)
    start = None

    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == "S":
                start = (r, c)
                continue

            pipe_grid[r, c] = char
            adj_grid[r, c] = {
                "|": [(r-1, c), (r+1, c)],
                "-": [(r, c-1), (r, c+1)],
                "L": [(r-1, c), (r, c+1)],
                "J": [(r-1, c), (r, c-1)],
                "7": [(r, c-1), (r+1, c)],
                "F": [(r, c+1), (r+1, c)],
                ".": []
            }[char]

    # determine what pipe the S is covering
    start_adjs = [adj for adj in adjacents(*start) if start in adj_grid[adj]]
    adj_grid[start] = [adj for adj in adjacents(*start) if start in adj_grid[adj]]
    relative_start = tuple(sorted((adj[0]-start[0], adj[1]-start[1]) for adj in start_adjs))
    pipe_grid[start] = {
        ((-1, 0), (1, 0)): "|",
        ((0, -1), (0, 1)): "-",
        ((-1, 0), (0, 1)): "L",
        ((-1, 0), (0, -1)): "J",
        ((0, -1), (1, 0)): "7",
        ((0, 1), (1, 0)): "F"
    }[relative_start]

    # find all main loop pipes
    history = set()
    dirs = [start]
    while len(dirs) != 0:
        pos = dirs[0]
        history.add(pos)
        dirs = list(filter(lambda adj: adj not in history, adj_grid[pos]))

    # remove all junk pipes
    grounds = set()
    for r in range(h):
        for c in range(w):
            if (r, c) not in history:
                adj_grid[r, c] = []
                pipe_grid[r, c] = "."
                grounds.add((r, c))
            elif pipe_grid[r, c] == ".":
                grounds.add((r, c))

    # count the ground squares inside the main pipe loop
    total = 0
    for r, c in sorted(grounds):
        inside = False
        to_right = pipe_grid[r, c+1:]
        i = 0
        while i < len(to_right):
            if to_right[i] == "|":
                inside = not inside
            elif to_right[i] == "L":
                i += 1
                while to_right[i] == "-":
                    i += 1
                if to_right[i] == "7":
                    inside = not inside
            elif to_right[i] == "F":
                i += 1
                while to_right[i] == "-":
                    i += 1
                if to_right[i] == "J":
                    inside = not inside
            i += 1
        
        total += inside
                
    return total
        

