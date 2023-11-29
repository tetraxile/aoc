from util import *

def part_1(data: str) -> str:
    fmt = parse_fmt_string("{name:a}: capacity {capacity:i}, durability {durability:i}, flavor {flavor:i}, texture {texture:i}, calories {calories:i}")

    ingredients = [parse_string(fmt, line) for line in data.split("\n")]

    n = 100
    best = 0
    perms = ((k, j, i, n-i-j-k) for k in range(n+1) for j in range(n-k+1) for i in range(n-j-k+1))
    for perm in perms:
        capacity = max(0, sum(perm[i]*ingredients[i]["capacity"] for i in range(len(perm))))
        durability = max(0, sum(perm[i]*ingredients[i]["durability"] for i in range(len(perm))))
        flavor = max(0, sum(perm[i]*ingredients[i]["flavor"] for i in range(len(perm))))
        texture = max(0, sum(perm[i]*ingredients[i]["texture"] for i in range(len(perm))))

        best = max(best, capacity*durability*flavor*texture)

    return best

def part_2(data: str) -> str:
    fmt = parse_fmt_string("{name:a}: capacity {capacity:i}, durability {durability:i}, flavor {flavor:i}, texture {texture:i}, calories {calories:i}")

    ingredients = [parse_string(fmt, line) for line in data.split("\n")]

    n = 100
    best = 0
    perms = ((k, j, i, n-i-j-k) for k in range(n+1) for j in range(n-k+1) for i in range(n-j-k+1))
    for perm in perms:
        calories = sum(perm[i]*ingredients[i]["calories"] for i in range(len(perm)))
        if calories != 500:
            continue

        capacity = max(0, sum(perm[i]*ingredients[i]["capacity"] for i in range(len(perm))))
        durability = max(0, sum(perm[i]*ingredients[i]["durability"] for i in range(len(perm))))
        flavor = max(0, sum(perm[i]*ingredients[i]["flavor"] for i in range(len(perm))))
        texture = max(0, sum(perm[i]*ingredients[i]["texture"] for i in range(len(perm))))

        best = max(best, capacity*durability*flavor*texture)

    return best
