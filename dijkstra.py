#dijkstra algo
import heapq
def dijkstra(graph, src):
    dist = {node: float('inf') for node in graph}
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        distance, node = heapq.heappop(pq)
        if distance > dist[node]:
            continue
        for v, w in graph[node]:
            if dist[node] + w < dist[v]:
                dist[v] = dist[node] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

graph = {
    'A': [('B',1),('C',4)],
    'B': [('C',2),('D',5)],
    'C': [('D',1)],
    'D': []
}
print(dijkstra(graph, 'A'))
