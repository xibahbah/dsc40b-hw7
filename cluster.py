def cluster(graph, weights, level):
    visited = set()
    clusters = []

    for u in graph.nodes:
        if u not in visited:
            stack = [u]
            comp = []
            visited.add(u)
            while stack:
                x = stack.pop()
                comp.append(x)
                for y in graph.neighbors(x):
                    if y not in visited and weights(x, y) >= level:
                        visited.add(y)
                        stack.append(y)
            clusters.append(frozenset(comp))

    return frozenset(clusters)
