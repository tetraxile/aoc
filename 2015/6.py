import numpy as np


def part_1(data: str) -> str:
    matrix = np.zeros((1000, 1000), dtype=bool)

    for i, line in enumerate(data.split("\n")):
        parts = line.split(" ")
        if len(parts) == 4:
            state = "toggle"
        else:
            state = parts[1]

        top, left = tuple(map(int, parts[-3].split(",")))
        bottom, right = tuple(map(int, parts[-1].split(",")))
        bottom += 1
        right += 1

        if state == "on":
            matrix[top:bottom, left:right] = True
        elif state == "off":
            matrix[top:bottom, left:right] = False
        elif state == "toggle":
            matrix[top:bottom, left:right] = np.logical_not(matrix[top:bottom, left:right])

    return matrix.sum()


def part_2(data: str) -> str:
    matrix = np.zeros((1000, 1000), dtype=np.uint8)

    for i, line in enumerate(data.split("\n")):
        parts = line.split(" ")
        if len(parts) == 4:
            state = "toggle"
        else:
            state = parts[1]

        top, left = tuple(map(int, parts[-3].split(",")))
        bottom, right = tuple(map(int, parts[-1].split(",")))
        bottom += 1
        right += 1

        shape = (bottom-top, right-left)
        submatrix = matrix[top:bottom, left:right]

        if state == "on":
            np.add(submatrix, np.full(shape, 1, dtype=np.uint8), out=submatrix)
        elif state == "off":
            np.subtract(submatrix, np.full(shape, 1, dtype=np.uint8), out=submatrix, where=submatrix>0)
        elif state == "toggle":
            np.add(submatrix, np.full(shape, 2, dtype=np.uint8), out=submatrix)

    return matrix.sum()
