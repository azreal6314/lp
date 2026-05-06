import heapq

def prim(graph, start):
    visited = set()
    mst_cost = 0
    pq = [(0, start)]   # (weight, node)
    while pq:
        weight, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        mst_cost += weight
        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, neighbor))
    return mst_cost


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print(prim(graph, 'A'))