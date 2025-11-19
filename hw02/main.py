from collections import deque

def bfs_path(graph, s, t):
    """Return a shortest path (fewest edges) from s to t as a list of nodes.

    If s == t, return [s]. If s or t not in graph, return None.
    """
    if s not in graph or t not in graph:
        return None
    if s == t:
        return [s]

    queue = deque([s])
    visited = {s}
    parent = {s: None}

    while queue:
        current = queue.popleft()
        if current == t:
            break
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    if t not in parent:
        return None

    path = []
    node = t
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]