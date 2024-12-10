import math

instructions = ""
nodes = {}

for i, line in enumerate(open("day8.txt", "r")):
    if (i == 0): 
        instructions = line
        continue
    if (i == 1): continue

    t = line.split(" = ")
    t1 = t[1].split(", ")
    nodes[t[0]] = (t1[0][1:], t1[1][:-2])

curr_node = "AAA"
steps = 0

while (curr_node != "ZZZ"):
    dir = instructions[steps % (len(instructions)-1)]
    curr_node = nodes[curr_node][0] if dir == "L" else nodes[curr_node][1]
    steps += 1

print(steps)

# Part 2
curr_nodes_a = []
for node in nodes.keys():
    if node[2] == "A": curr_nodes_a.append(str(node))

loops = []
for i, node in enumerate(curr_nodes_a):
    steps = 0
    loop_start = -1

    while (True):
        dir = instructions[steps % (len(instructions)-1)]
        node = nodes[node][0] if dir == "L" else nodes[node][1]
        steps += 1

        if (node.endswith("Z")):
            if (loop_start == -1):
                loop_start = steps
            else:
                loops.append(steps - loop_start)
                break

print(math.lcm(*loops))