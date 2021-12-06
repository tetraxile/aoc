with open("input", "r") as f:
    a = f.readline().strip()
    fishes = [a.count(str(i)) for i in range(9)]


def fishes_after_n_days(n: int) -> int:
    tmp_fishes = fishes[:]
    for i in range(n):
        n_reproduce = tmp_fishes[0]
        for j in range(8):
            tmp_fishes[j] = tmp_fishes[j+1]
        tmp_fishes[6] += n_reproduce
        tmp_fishes[8] = n_reproduce
    return sum(tmp_fishes)


print("part 1:", fishes_after_n_days(80))
print("part 2:", fishes_after_n_days(256))
