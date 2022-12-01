with open("input") as f:
    a = [sum(map(int, elf.strip().split("\n"))) for elf in f.read().split("\n\n")]

print("part 1:", max(a))
print("part 2:", sum(sorted(a)[-3:]))
