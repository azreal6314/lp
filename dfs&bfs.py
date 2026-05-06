#recursive dfs
def dfs(node,result,vst,adj):
    vst[node]=1
    result.append(node)
    for n in adj[node]:
        if vst[n]==0:
            dfs(n,result,vst,adj)

node=0
result=[]
no_of_nodes=5
visited=[0]*(no_of_nodes+1)
adj=[[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
dfs(0,result,visited,adj)
print("dfs traversal")
print(result)




## recursive bfs
from collections import deque
def bfs_recursive(adj,visited,queue,ans):
    if not queue:
        return

    node=queue.popleft()

    ans.append(node)
    for neighbor in adj[node]:
        if visited[neighbor] == 0:
            visited[neighbor]=1
            queue.append(neighbor)

        bfs_recursive(adj,visited,queue,ans)

def bfs(start,adj):
    n = len(adj)
    start = 0
    queue = deque()
    queue.append(start)
    visited = [0] * (n + 1)
    visited[start] = 1
    result = []
    bfs_recursive(adj,visited,queue,result)
    return result

adj=[[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
print("bfs traversal")
print(bfs(0,adj))