from utils.f import readinput, readtest

entries = readinput(__file__).split("\n")
# entries = readtest(__file__).split("\n")
# entries = [e for e in entries if e]

assigns = {}
memo = {}

for line in entries:
    expr, op = map(str.strip, line.split("->"))
    assigns[op] = expr


def solve(op):
    if op.isnumeric():
        return int(op)

    if op in memo:
        return memo[op]

    value = assigns[op]

    if value.isnumeric():
        return int(value)
    else:
        if "AND" in value:
            op1, _, op2 = value.split()
            memo[op] = solve(op1) & solve(op2)
        elif "OR" in value:
            op1, _, op2 = value.split()
            memo[op] = solve(op1) | solve(op2)
        elif "LSHIFT" in value:
            op1, _, op2 = value.split()
            memo[op] = solve(op1) << int(op2) & 65535
        elif "RSHIFT" in value:
            op1, _, op2 = value.split()
            memo[op] = solve(op1) >> int(op2) & 65535
        elif "NOT" in value:
            _, op = value.split()
            memo[op] = ~solve(op) & 65535
        else:
            memo[op] = solve(value)

        return memo[op]


# t = ["x", "y", "d", "f", "g", "h", "i"]
# for i in t:
#     print(solve(i))

print(solve("a"))
