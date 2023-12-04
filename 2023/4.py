def part_1(data: str) -> str:
    total = 0
    for line in data.splitlines():
        card_id, tmp = line.split(": ")
        winning, have = tmp.split(" | ")
        winning = [int(winning[3*i:3*i+2].lstrip()) for i in range((len(winning)+1)//3)]
        have = [int(have[3*i:3*i+2].lstrip()) for i in range((len(have)+1)//3)]
        
        score = sum(num in have for num in winning)
        if score > 0:
            total += 2 ** (score-1)

    return total

def part_2(data: str) -> str:
    total = 0
    cards = {}
    for line in data.splitlines():
        card_id, tmp = line.split(": ")
        card_id = int(card_id.removeprefix("Card "))
        winning, have = tmp.split(" | ")
        winning = [int(winning[3*i:3*i+2].lstrip()) for i in range((len(winning)+1)//3)]
        have = [int(have[3*i:3*i+2].lstrip()) for i in range((len(have)+1)//3)]
        
        score = sum(num in have for num in winning)
        cards[card_id] = [score, 1]

    for card_id, (score, count) in cards.items():
        total += count
        for idx in range(card_id, card_id+score):
            cards[idx+1][1] += count

    return total
