def evaluate_term(wires: dict, term: str, cache: dict):
    if term.isnumeric():
        return int(term)
    else:
        return evaluate_expr(wires, term, cache)


def evaluate_expr(wires: dict, dst: str, cache: dict) -> int:
    if dst in cache:
        return cache[dst]

    expr = wires[dst]

    if len(expr) == 1:
        out = evaluate_term(wires, expr[0], cache)
    elif len(expr) == 2:
        assert expr[0] == "NOT"
        out = evaluate_term(wires, expr[1], cache) ^ 0xffff
    else:
        lhs = evaluate_term(wires, expr[0], cache)
        rhs = evaluate_term(wires, expr[2], cache)
        
        if expr[1] == "OR":
            out = (lhs | rhs) & 0xffff
        elif expr[1] == "LSHIFT":
            out = (lhs << rhs) & 0xffff
        elif expr[1] == "RSHIFT":
            out = (lhs >> rhs) & 0xffff
        elif expr[1] == "AND":
            out = (lhs & rhs) & 0xffff

    cache[dst] = out
    return out


def part_1(data: str) -> str:
    wires = {}
    for line in data.split("\n"):
        *expr, _, dst = line.split(" ")
        wires[dst] = expr
    
    cache = {}
    return evaluate_expr(wires, "a", cache)


def part_2(data: str) -> str:
    new_signal = part_1(data)
    
    wires = {}
    for line in data.split("\n"):
        *expr, _, dst = line.split(" ")
        wires[dst] = expr
    
    wires["b"] = [str(new_signal)]

    cache = {}
    return evaluate_expr(wires, "a", cache)

