with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]

line_len = len(lines[0])


def part_1():
    ones_l = [0] * line_len
    gamma = ''

    for line in lines:
        for pos, char in enumerate(line):
            if char == '1':
                ones_l[pos] += 1

    for x in range(line_len):
        if ones_l[x] > len(lines)/2:
            gamma += '1'
        elif ones_l[x] < len(lines)/2:
            gamma += '0'

    gamma = int(gamma, 2)
    epsilon = ~gamma & (2**line_len - 1)

    return gamma * epsilon


def part_2():
    l = ['', '']
    for n in [0, 1]:
        current_lines = [x for x in lines]
        for c in range(line_len):
            zeros = 0
            ones = 0
            tmp = []
            for line in current_lines:
                if line[c] == '0':
                    zeros += 1
                elif line[c] == '1':
                    ones += 1

            for line in current_lines:
                if ones >= zeros and line[c] == '01'[1-n]:
                    tmp.append(line)
                elif ones < zeros and line[c] == '01'[n]:
                    tmp.append(line)

            current_lines = tmp
            if len(tmp) == 1:
                l[n] = tmp[0]
                break

    o2, co2 = l
    return int(o2, 2) * int(co2, 2)


print("part 1:", part_1())
print("part 2:", part_2())
