"""

I really dislike how this problem has to be solved in Part.2

Nevertheless, its very instructive and as usually fun to solve.

Every **A has a cycle. You have to detect when this cycle happens and 

calculate the lcm of all of them. 

This is the iteration where all the **A would be finish on a **Z.

So, its not solved by carefully reading the statement.

It's also not solved by skimming throught the input.

It is solved by inspecting the output and figuring out there is a cycle.

"""


import math
import re

lines = open("input.txt").readlines()
inst = list(lines[0].strip())


class Node:
    def __init__(self, entry):
        self.name, self.left, self.right = re.findall(r"\w{3}", entry)

    def __str__(self):
        return f"{self.name} L: {self.left} R: {self.right}"


nodes = {}
for line in lines[2:]:
    node = Node(line)
    nodes[node.name] = node


results = []
A_nodes = [node for node in nodes.values() if node.name.endswith("A")]
l_inst = len(inst)
for node in A_nodes:
    step = 0
    current = node
    while True:
        movement = inst[step % l_inst]
        step += 1
        # print(f"iteration: {step} inst: {movement} -> {[n.name for n in A_nodes]}")
        match movement:
            case "L":
                current = nodes[current.left]
            case "R":
                current = nodes[current.right]
        if current.name.endswith("Z"):
            # print(f"found Z for {node.name} with {current.name}")
            break
    results.append((step, current.name))

for_mdc = []
for result in results:
    for_mdc.append(result[0])
print(math.lcm(*for_mdc))
