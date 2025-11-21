def biggest_descendent(graph, root, value):
    biggest = {}
    def dfs(u):
        m = value[u]
        for v in graph.neighbors(u):
            mv = dfs(v)
            if mv > m:
                m = mv
        biggest[u] = m
        return m
    dfs(root)
    return biggest
