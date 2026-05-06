def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def kruskal(n, edges):
    edges.sort(key=lambda e: e[2])  # sort by weight
    parent = list(range(n))
    mst = []
    for u, v, w in edges:
        pu, pv = find(parent, u), find(parent, v)
        if pu != pv:      # no cycle
            parent[pu] = pv
            mst.append((u, v, w))
    return mst

edges = [(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]
print(kruskal(4, edges))