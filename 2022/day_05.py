def parse_layout(layout: str) -> list[str]:
    lines = layout.split("\n")
    num_stacks = (len(lines[0])+1)//4
    stacks = ["" for _ in range(num_stacks)]

    for line in lines[-2::-1]:
        crates = [line[i+1] for i in range(0, num_stacks*4, 4)]
        for s, crate in enumerate(crates):
            if crate != " ":
                stacks[s] += crate

    return stacks


def part_1(layout: list[str], procedure: list[str]):
    for step in procedure:
        tokens = step.split()
        amount, from_, to = int(tokens[1]), int(tokens[3])-1, int(tokens[5])-1

        layout[to] += layout[from_][:-amount-1:-1]
        layout[from_] = layout[from_][:-amount]

    return "".join(stack[-1] for stack in layout)


def part_2(layout, procedure):
    for step in procedure:
        tokens = step.split()
        amount, from_, to = int(tokens[1]), int(tokens[3])-1, int(tokens[5])-1

        layout[to] += layout[from_][-amount:]
        layout[from_] = layout[from_][:-amount]

    return "".join(stack[-1] for stack in layout)


with open("input") as f:
    layout, procedure = f.read().strip().split("\n\n")
    layout = parse_layout(layout)
    procedure = procedure.split("\n")

print("part 1:", part_1(layout[:], procedure))
print("part 2:", part_2(layout[:], procedure))
