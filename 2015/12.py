import json


def sum_node(node: list | dict | str | int, red: bool = False):
    if isinstance(node, list):
        return sum(sum_node(child, red) for child in node)
    elif isinstance(node, dict):
        if red and "red" in node.values():
            return 0
        return sum(sum_node(child, red) for child in node.values())
    elif isinstance(node, str):
        return 0
    elif isinstance(node, int):
        return node

    assert False


def part_1(data: str) -> str:
    return sum_node(json.loads(data))

def part_2(data: str) -> str:
    return sum_node(json.loads(data), red=True)
