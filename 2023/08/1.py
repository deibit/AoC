import re

lines = open("input.txt").readlines()

inst = list(lines[0].strip())


class Node:
    def __init__(self, entry):
        self.name, self.left, self.right = re.findall(r"[A-Z]{3}", entry)

    def __str__(self):
        return f"{self.name} L: {self.left} R: {self.right}"


nodes = {}
for line in lines[2:]:
    node = Node(line)
    nodes[node.name] = node

steps = 0
current = nodes["AAA"]
while True:
    if current.name == "ZZZ":
        break
    step = inst[steps % len(inst)]
    match step:
        case "L":
            current = nodes[current.left]
        case "R":
            current = nodes[current.right]
        case "_":
            print("error")
            quit()
    steps += 1


print(steps)
