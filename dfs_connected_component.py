def dfs_connected_component(graph,start):
    stack = [start]
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for n in graph[node]:
                stack.append(n)
    return visited