hands = [] # hand, bid, type [0=unknown, 1-7 = high card - five of a kind]
mapping = {"A": 12, "K": 11, "Q": 10, "J": 9, "T": 8, "9": 7, "8": 6,
               "7": 5, "6": 4, "5": 3, "4": 2, "3": 1, "2": 0}

for line in open("day7.txt", "r"):
    t = line.split()
    hands.append((t[0], int(t[1]), 0))

# For each hand, find out and assign its type
for i, hand in enumerate(hands):
    counts = [0]*13 # 2-A, length 13

    # Get the count of each label
    for c in hand[0]:
        counts[mapping[c]] += 1

    # Five of a kind
    if (5 in counts):
        hands[i] = (hand[0], hand[1], 7)
        continue

    # Four of a kind
    if (4 in counts):
        hands[i] = (hand[0], hand[1], 6)
        continue

    # Full house
    if (3 in counts and 2 in counts):
        hands[i] = (hand[0], hand[1], 5)
        continue

    # Three of a kind
    if (3 in counts):
        hands[i] = (hand[0], hand[1], 4)
        continue

    # Two pair
    if (counts.count(2) == 2):
        hands[i] = (hand[0], hand[1], 3)
        continue

    # One pair
    if (2 in counts):
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

print(total)