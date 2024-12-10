RED_CUBE_LIMIT = 12
GREEN_CUBE_LIMIT = 13
BLUE_CUBE_LIMIT = 14

total = 0
powers = 0

for line in open("./day2.txt", "r"):
    cube_maxes = {"red": 0, "green": 0, "blue": 0}
    game_id = 0
    temp = line.split(": ")

    # Get the game's ID
    game_id = int(temp[0].split()[1])

    # Split up all the hands
    hands = temp[1].split(";")
    
    # Update the max cube counts for each color
    for hand in hands:
        cubes = hand.split(", ")

        for cube in cubes:
            temp = cube.split()
            if (cube_maxes[temp[1]] < int(temp[0])): 
                cube_maxes[temp[1]] = int(temp[0])
            
    # Find the powers
    powers += cube_maxes["red"] * cube_maxes["green"] * cube_maxes["blue"]

    # Make sure no hands have cubes over the limit
    if (cube_maxes["red"] > RED_CUBE_LIMIT):
        continue

    if (cube_maxes["green"] > GREEN_CUBE_LIMIT):
        continue

    if (cube_maxes["blue"] > BLUE_CUBE_LIMIT):
        continue;

    # Add to the total
    total += game_id

print(total)
print(powers)