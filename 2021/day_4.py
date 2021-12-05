import numpy as np

boards = []

with open("input", "r") as f:
    call_nums = list(map(int, f.readline().split(",")))
    for i in range(100):
        f.readline()
        board = np.zeros((5,5), dtype="int")
        for j in range(5):
            board[j] = np.array(list(map(int, f.readline().split())), dtype="int")
        boards.append(board)


def bingo(board: np.ndarray) -> bool:
    if isinstance(board, int): return False
    clear = np.array([-1]*5)
    for i in range(5):
        if np.array_equal(board[i], clear) or np.array_equal(board[:,i], clear):
            return True
    return False


def score(arr, call) -> int:
    tmp = set(arr.flatten().tolist())
    tmp.remove(-1)
    return sum(tmp) * call


def find_first_bingo() -> tuple[np.ndarray, int]:
    tmp_boards = [b for b in boards]
    for call in call_nums:
        for board in tmp_boards:
            board[board == call] = -1
            if bingo(board):
                return (board, call)


def find_last_bingo() -> tuple[np.ndarray, int]:
    is_bingo = [False for b in boards]
    tmp_boards = [b for b in boards]
    for call in call_nums:
        for n, board in enumerate(tmp_boards):
            save_board = np.copy(board)
            board[board == call] = -1
            if bingo(board):
                is_bingo[n] = True
            if len([b for b in is_bingo if not b]) == 0:
                return board, call


print("part 1:", score(*find_first_bingo()))
print("part 2:", score(*find_last_bingo()))
