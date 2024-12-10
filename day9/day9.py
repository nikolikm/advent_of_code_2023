histories = []
total = 0
total_2 = 0

for line in open("day9.txt", "r"):
    history = []
    history_initial = []
    for x in line.split():
        history_initial.append(int(x))
    history.append(history_initial)
    histories.append(history)


# Get and store the difference sequences for each history
for h, history in enumerate(histories):
    move_on = False
    sequence_to_diff = history[0]

    while (not move_on):
        diffs = []

        for i in range(1, len(sequence_to_diff)):
            diffs.append(sequence_to_diff[i] - sequence_to_diff[i-1])

        # Add these diffs to the history
        histories[h].append(diffs)

        # Stop once the diffs consist of all 0s
        if not any(diffs):
            diffs.append(0)
            diffs.insert(0, 0);
            move_on = True
        else:
            sequence_to_diff = diffs

# Extrapolate the next number in each sequence backwards, for each history
for h, history in enumerate(histories):
    for i in range(len(history)-2, -1, -1):
        histories[h][i].append(history[i][-1] + history[i+1][-1])
        histories[h][i].insert(0, history[i][0] - history[i+1][0])

# Get the totals
for history in histories:
    total += history[0][-1]
    total_2 += history[0][0]

print(total)
print(total_2)
