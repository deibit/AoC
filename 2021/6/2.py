'''
    Awesome problem

    This was not the final version. The former one was based on brute force, as 1.py is.
    It happens that the interesting thing is the states and just counting the number of
    fish are on a certain state is the key.

    This problem illustrate the importance of understand the statment before attacking
    and starting coding. All is input and rules.

'''

def set_states(lanterns):
    states = [0 for _ in range(9)]
    for lantern in lanterns:
        states[lantern] += 1
    return states

with open('input', 'r') as f:
    lanterns = [int(n) for n in f.readlines()[0].strip().split(',')]

states = set_states(lanterns)

top = len(states)

for day in range(256):
    new_borns = states[0]
    for pos in range(top):
        states[pos] = states[(pos+1) % top]
    states[6] += new_borns
    states[8] = new_borns

print(sum(states))
