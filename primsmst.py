import heapq

import heapq

def prims(graph, start):
    visited = set()
    min_heap = [(0, start, -1)]   # (weight, current_node, parent)

    total_cost = 0
    mst = []

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        total_cost += weight

        # store MST edge
        if parent != -1:
            mst.append((parent, node, weight))

        # push neighbors into heap
        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, node))

    print("Edges in MST:")
    for u, v, w in mst:
        print(f"{u} -- {v} == {w}")

    print("Total Cost =", total_cost)



graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print(prims(graph, 'A'))