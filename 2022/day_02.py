with open("input") as f:
    l = f.read().split("\n")

def part_1():
    score = 0
    for game in l:
        info = game.split()
        opponent = "ABC".index(info[0])
        me = "XYZ".index(info[1])
        score += me + 1     # score for shape choice
        score += 3 * ((me - opponent + 1) % 3)  # score for win/draw/lose

    return score


def part_2():
    score = 0
    for game in l:
        info = game.split()
        opponent = "ABC".index(info[0])
        end = "XYZ".index(info[1])
        score += end * 3    # score for win/draw/lose
        score += (end + opponent - 1) % 3 + 1   # score for shape choice
    
    return score


print("part 1:", part_1())
print("part 2:", part_2())
