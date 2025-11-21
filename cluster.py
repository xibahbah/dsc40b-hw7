def cluster(graph, weights, level):
    visited = set()
    clusters = []

    for u in graph.vertices():
        if u not in visited:
            stack = [u]
            component = []
            visited.add(u)
            while stack:
                x = stack.pop()
                component.append(x)
                for y in graph.neighbors(x):
                    if y not in visited and weights(x, y) >= level:
                        visited.add(y)
                        stack.append(y)
            clusters.append(frozenset(component))

    return frozenset(clusters)
