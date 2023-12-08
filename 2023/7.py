from util import *
from functools import cmp_to_key


def compare_hands(hand1: str, hand2: str, part2: bool = False) -> int:
    cards1 = hand1[0]
    cards2 = hand2[0]

    card_order = "AKQJT98765432" if not part2 else "AKQT98765432J"
    types = {
        (5,): 6,           # five of a kind
        (1, 4): 5,         # four of a kind
        (2, 3): 4,         # full house
        (1, 1, 3): 3,      # three of a kind
        (1, 2, 2): 2,      # two pair
        (1, 1, 1, 2): 1,   # one pair
        (1, 1, 1, 1, 1): 0 # high card
    }

    if not part2:
        counts1 = tuple(sorted(count_unique(cards1).values()))
        counts2 = tuple(sorted(count_unique(cards2).values()))
    else:
        counts1 = list(sorted(count_unique(cards1.replace("J", "")).values()))
        counts2 = list(sorted(count_unique(cards2.replace("J", "")).values()))

        if len(counts1) == 0:
            counts1 = (5,)
        else:
            counts1[-1] += cards1.count("J")
        
        if len(counts2) == 0:
            counts2 = (5,)
        else:
            counts2[-1] += cards2.count("J")
        
        counts1 = tuple(counts1)
        counts2 = tuple(counts2)

    type1 = types[counts1]
    type2 = types[counts2]

    if type1 != type2:
        return type1 - type2
    else:
        for i in range(len(cards1)):
            card1 = card_order.index(cards1[i])
            card2 = card_order.index(cards2[i])
            if card1 != card2:
                return card2 - card1
        
        return 0


def part_1(data: str) -> str:
    hands = [(line[:5], int(line[6:])) for line in data.split("\n")]
    hands.sort(key=cmp_to_key(compare_hands))
    return sum((i+1) * bid for i, (cards, bid) in enumerate(hands))


def part_2(data: str) -> str:
    hands = [(line[:5], int(line[6:])) for line in data.split("\n")]
    hands.sort(key=cmp_to_key(lambda hand1, hand2: compare_hands(hand1, hand2, part2=True)))
    return sum((i+1) * bid for i, (cards, bid) in enumerate(hands))
