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


# A_nodes = [node for node in nodes.values() if node.name.endswith("A")]
# step = 0
# a_node = A_nodes[0]
# cycle = []
# print(f"solving cycle for {a_node.name}")
# while True:
#     current_direction = inst[step % len(inst)]
#     step += 1
#     match current_direction:
#         case "L":
#             cycle.append((a_node.name, "L"))
#             a_node = nodes[a_node.left]
#         case "R":
#             cycle.append((a_node.name, "R"))
#             a_node = nodes[a_node.right]
#     if len(cycle) > len(set(cycle)):
#         print(f"Found cycle for with {step}")
#         for elem in cycle:
#             print(elem)

results = []
A_nodes = [node for node in nodes.values() if node.name.endswith("A")]
l_inst = len(inst)
for node in A_nodes:
    step = 0
    current = node
    while True:
        movement = inst[step % l_inst]
        step += 1
        print(f"iteration: {step} inst: {movement} -> {[n.name for n in A_nodes]}")
        match movement:
            case "L":
                current = nodes[current.left]
            case "R":
                current = nodes[current.right]
        if current.name.endswith("Z"):
            print(f"found Z for {node.name} with {current.name}")
            break
    results.append((step, current.name))
print(results)
quit()

step = 0
l_inst = len(inst)
A_nodes = [node for node in nodes.values() if node.name.endswith("A")]
while not all([n.name.endswith("Z") for n in A_nodes]):
    movement = inst[step % l_inst]
    step += 1
    print(f"iteration: {step} inst: {movement} -> {[n.name for n in A_nodes]}")

    for idx in range(0, len(A_nodes)):
        current = A_nodes[idx]
        match movement:
            case "L":
                new = nodes[current.left]
                if not new in A_nodes:
                    A_nodes[idx] = new
                else:
                    A_nodes.remove(new)
            case "R":
                new = nodes[current.right]
                if not new in A_nodes:
                    A_nodes[idx] = new
                else:
                    A_nodes.remove(new)
            case "_":
                print("error")
                quit()
print([n.name for n in A_nodes])

print(step)
