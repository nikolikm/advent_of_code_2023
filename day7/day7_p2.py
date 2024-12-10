# JOKER EDITION 😈
hands = [] # hand, bid, type [0=unknown, 1-7 = high card - five of a kind]
mapping = {"A": 12, "K": 11, "Q": 10, "T": 9, "9": 8, "8": 7, "7": 6,
               "6": 5, "5": 4, "4": 3, "3": 2, "2": 1, "J": 0}

for line in open("day7.txt", "r"):
    t = line.split()
    hands.append((t[0], int(t[1]), 0))

# For each hand, find out and assign its type
for i, hand in enumerate(hands):
    counts = [0]*13 # J-A, length 13

    # Get the count of each label
    for c in hand[0]:
        counts[mapping[c]] += 1

    # Get the number of jokers
    jokers = counts[0]

    # NEED this, trust me I'm smart
    counts_jokerfied = counts[1:]

    # Account for the amount of joker cards in each remaining count
    for j, count in enumerate(counts_jokerfied):
        counts_jokerfied[j] = min(5, count + jokers)

    # Five of a kind
    if (5 in counts_jokerfied):
        hands[i] = (hand[0], hand[1], 7)
        continue

    # Four of a kind
    if (4 in counts_jokerfied):
        hands[i] = (hand[0], hand[1], 6)
        continue

    # [If we're down to here, there must be only up to 2 joker cards]

    # Full house
    if ((3 in counts and 2 in counts) or (jokers == 1 and counts.count(2) == 2)):
        hands[i] = (hand[0], hand[1], 5)
        continue

    # Three of a kind
    if ((3 in counts) or (jokers == 2 and counts.count(2) == 1) or (jokers == 1 and 2 in counts)):
        hands[i] = (hand[0], hand[1], 4)
        continue

    # [If we're down to here, there must be only up to 1 joker card]

    # Two pair
    if ((counts.count(2) == 2)):
        hands[i] = (hand[0], hand[1], 3)
        continue

    # One pair
    if ((2 in counts) or (jokers == 1)):
        hands[i] = (hand[0], hand[1], 2)
        continue

    # High card
    hands[i] = (hand[0], hand[1], 1)

# Sort the hands by their type and tie-breaking criteria
hands.sort(key=lambda x: (x[2], [mapping[c] for c in x[0]]))

# Get the total winnings
total = 0
for i, hand in enumerate(hands):
    total += hand[1]*(i+1)

print(hands)
print(total)