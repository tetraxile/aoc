import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Seg:
    def __init__(self, a, b):
        self.a = a
        self.b = b

segs = []
with open("input", "r") as f:
    for line in f.readlines():
        start, end = line.split(" -> ")
        start = Point(*map(int, start.split(",")))
        end = Point(*map(int, end.split(",")))
        segs.append(Seg(start, end))

def part_1():
    grid = np.zeros((1000,1000), dtype="int")
    for seg in segs:
        if seg.a.x == seg.b.x or seg.a.y == seg.b.y:
            diffx = seg.b.x - seg.a.x
            diffy = seg.b.y - seg.a.y
            stepx = 1 if diffx > 0 else -1 if diffx < 0 else 0
            stepy = 1 if diffy > 0 else -1 if diffy < 0 else 0
            for i in range(max(abs(diffx),abs(diffy))+1):
                grid[seg.b.y - i*stepy, seg.b.x - i*stepx] += 1
    return len(grid[grid >= 2])

def part_2():
    grid = np.zeros((1000,1000), dtype="int")
    for seg in segs:
        diffx = seg.b.x - seg.a.x
        diffy = seg.b.y - seg.a.y
        stepx = 1 if diffx > 0 else -1 if diffx < 0 else 0
        stepy = 1 if diffy > 0 else -1 if diffy < 0 else 0
        for i in range(max(abs(diffx),abs(diffy))+1):
            grid[seg.b.y - i*stepy, seg.b.x - i*stepx] += 1
    return len(grid[grid >= 2])



print("part 1:", part_1())
print("part 2:", part_2())
