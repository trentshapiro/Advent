from collections import Counter

with open("day07_input.txt") as f:
    a = f.readlines()
    a = [i.replace("\n", "") for i in a]

# Part 1
card_map = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

final_scores = [[], []]
for line in a:
    hand, bet = line.split(" ")

    hand_1 = [int(i) if i.isnumeric() else card_map[i] for i in hand]
    hand_2 = [i if i != 11 else 1 for i in hand_1]
    hand_aggs = [Counter(hand_1), Counter(hand_2)]

    for idx, hand in enumerate([hand_1, hand_2]):
        hand_counts = hand_aggs[idx]

        non_joker = {k: v for k, v in hand_counts.items() if k != 1}
        jokers = hand_counts[1] if 1 in hand_counts.keys() else 0

        if len(non_joker.values()) == 0:
            hand_value = 0
        elif 3 in non_joker.values() and 2 in non_joker.values():
            hand_value = 3.5
        elif len([i for i in non_joker.values() if i == 2]) > 1:
            hand_value = 2.5
        else:
            hand_value = max(non_joker.values())

        joker_value = hand_value + jokers

        final_scores[idx].append(([joker_value, *hand], bet))


for game in final_scores:
    ordered_hands = sorted(game, key=lambda x: (x[0]))
    total = 0
    for idx, i in enumerate(ordered_hands):
        total += (idx + 1) * int(i[1])
    print(total)
