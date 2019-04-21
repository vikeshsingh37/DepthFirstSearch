def dfs_connected_component_recursive(graph,start,visited=[]):
    if start not in visited:
        visited.append(start)
        for n in graph[start]:
            dfs_connected_component_recursive(graph,n,visited)  
    return visited