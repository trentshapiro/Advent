from collections import Counter

with open("day04_input.txt") as f:
    a = f.readlines()
    a = [i.replace('\n','') for i in a]

total = 0
results = {}

for idx, line in enumerate(a):
    cards = line.split(": ")[-1]
    wins = [int(i.strip()) for i in cards.split(" | ")[0].split(" ") if i != '']
    draws = [int(i.strip()) for i in cards.split(" | ")[1].split(" ") if i != '']

    matches = []
    for draw in draws:
        if draw in wins:
            matches.append(draw)
    
    line_total = 0
    for x, match in enumerate(matches):
        if x == 0:
            line_total += 1
        else:
            line_total = line_total * 2
    total+= line_total

    results[idx+1] = [i for i in range(idx+2,idx+len(matches)+2)]

print(f"part 1 total: {total}")


def get_card_winnings(input_card, results) -> list[int]:
    input_card_wins = results[input_card]
    total_cards_won = []
    if input_card_wins == []:
        return [0]
    else:
        for card in input_card_wins:
            total_cards_won.extend([card,*get_card_winnings(card,results)])
    return total_cards_won

all_winnings = [i for i in results.keys()]
for card_num, _ in enumerate(a):
    all_winnings.extend(get_card_winnings(card_num+1,results))

counts = Counter([i for i in all_winnings if i>0])

print(f"part 2 total: {sum(counts.values())}")
