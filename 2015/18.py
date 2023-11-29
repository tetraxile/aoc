from PIL import Image
import numpy as np


class Matrix:
    def __init__(self, raw):
        self.raw = raw
        self.shape = raw.shape

    @classmethod
    def parse(cls, data: str):
        lines = data.split("\n")
        h = len(lines)
        w = len(lines[0])
        matrix = np.zeros((h, w), dtype=bool)

        for r, line in enumerate(lines):
            for c, char in enumerate(line):
                if char == "#":
                    matrix[r, c] = True
                elif char == ".":
                    matrix[r, c] = False
                else:
                    assert False
    
        return cls(matrix)

    def print(self):
        out = []
        for r in range(self.shape[0]):
            for c in range(self.shape[1]):
                out.append("#" if self.raw[r, c] else ".")
            out.append("\n")
        print("".join(out))

    def step(self):
        new_matrix = np.zeros(self.shape, dtype=bool)
        padded = np.pad(self.raw, 1, constant_values=(0,))
        for r in range(self.shape[0]):
            for c in range(self.shape[1]):
                neighbours = sum(padded[adj] for adj in Matrix.get_adjacents(r+1, c+1))
                if self.raw[r, c]:
                    new_matrix[r, c] = neighbours in (2, 3)
                else:
                    new_matrix[r, c] = neighbours == 3
    
        self.raw = new_matrix

    @staticmethod
    def get_adjacents(r: int, c: int) -> list[tuple[int, int]]:
        return [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c+1), (r+1, c+1), (r+1, c), (r+1, c-1), (r, c-1)]

    def count_lights(self):
        return self.raw.sum()

    def set_corners(self):
        self.raw[0, 0] = True
        self.raw[0, self.shape[1]-1] = True
        self.raw[self.shape[0]-1, 0] = True
        self.raw[self.shape[0]-1, self.shape[1]-1] = True


def part_1(data: str) -> str:
    matrix = Matrix.parse(data)
    for i in range(100):
        matrix.step()

    return matrix.count_lights()


def part_2(data: str) -> str:
    matrix = Matrix.parse(data)
    matrix.set_corners()

    for i in range(100):
        matrix.step()
        matrix.set_corners()

    return matrix.count_lights()
