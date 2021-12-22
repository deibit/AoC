import pprint

with open('input', 'r') as f:
    data = [c for c in f.read().split()]

    def add(G, f, t):
        if G.get(f):
            G[f].add(t)
        else:
            G[f] = {t}

    G = {}
    for conn in data:
        fr0m, to = conn.split('-')
        add(G, fr0m, to)
        add(G, to, fr0m)

    p = pprint.PrettyPrinter(indent=4)
    #p.pprint(G)

    paths = []

    def explore(G, node, path=[], consent=True):
        path = path[:]
        path.append(node)
        for sibling in G[node]:
            if sibling not in path or sibling.isupper():
                explore(G, sibling, path, consent)
            elif sibling not in ['start', 'end'] and sibling in path and sibling.islower() and consent:
                explore(G, sibling, path, False)

        if node == 'end':
            paths.append(path)

    explore(G, "start")
    # p.pprint(paths)
    print(len(paths))
