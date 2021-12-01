def compare_two_offset(arr: list, offset: int) -> int:
    n = 0
    for i in range(len(arr) - offset):
        a = int(arr[i])
        b = int(arr[i+offset])
        if b > a:
            n += 1
    return n


with open("input", "r") as f:
    lines = f.readlines()

print("part 1:", compare_two_offset(lines, 1))
print("part 2:", compare_two_offset(lines, 3))
