races = []

lines = open("day6.txt", "r").readlines()
for i, time in enumerate(lines[0].split("Time:        ")[1].split()):
    dist = lines[1].split("Distance:  ")[1].split()[i]
    races.append((int(time), int(dist)))

poss_times_per_race = []
for race in races:
    times = []
    for i in range(1, race[0]-1):
        if (i*(race[0]-i) > race[1]):
            times.append(i)
    poss_times_per_race.append(times)

total = len(poss_times_per_race[0])
for i in range(1, len(poss_times_per_race)):
    total *= len(poss_times_per_race[i])

print(total)

# Special race
spec_race = (59707878, 430121812131276)

counter = 0
for i in range(1, spec_race[0]-1):
    if (i*(spec_race[0]-i) > spec_race[1]):
        counter += 1

print(counter)
