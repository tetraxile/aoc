from util import *

def part_1(data: str) -> str:
    fmt = parse_fmt_string("Sue {idx:i}: {item1:a}: {count1:i}, {item2:a}: {count2:i}, {item3:a}: {count3:i}")
    aunts = [parse_string(fmt, line) for line in data.split("\n")]

    info = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

    for aunt in aunts:
        items = {aunt["item1"]: aunt["count1"], aunt["item2"]: aunt["count2"], aunt["item3"]: aunt["count3"]}
        
        if all(count == info[item] for item, count in items.items()):
            return aunt["idx"]

def part_2(data: str) -> str:
    fmt = parse_fmt_string("Sue {idx:i}: {item1:a}: {count1:i}, {item2:a}: {count2:i}, {item3:a}: {count3:i}")
    aunts = [parse_string(fmt, line) for line in data.split("\n")]

    info = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

    for aunt in aunts:
        items = {aunt["item1"]: aunt["count1"], aunt["item2"]: aunt["count2"], aunt["item3"]: aunt["count3"]}
        
        correct = 0
        for item, count in info.items():
            if item in items:
                if item in ("cats", "trees"):
                    correct += items[item] > count
                elif item in ("pomeranians", "goldfish"):
                    correct += items[item] < count
                else:
                    correct += items[item] == count

        if correct == 3:
            return aunt["idx"]
