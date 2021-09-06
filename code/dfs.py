def dfs(graph, start_node):
    need_visit = []
    visited = []
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
            
    return visited
