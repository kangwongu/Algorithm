def bfs(graph, start_node):
    visited = []
    need_visited = []
    
    need_visited.append(start_node)
    while need_visited:
        node = need_visited.pop(0)
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
            
    return visited
