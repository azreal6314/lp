import heapq
def heuristic(start,adjacent):
    #manhattan distance
    return abs(start[0]-adjacent[0])+abs(start[1]-adjacent[1])

def astar(grid,start,goal):
    rows,columns = len(grid),len(grid[0])
    open_set =[]
    heapq.heappush(open_set,(0,start))
    came_from={}
    g_score={start : 0}

    while open_set:
        current = heapq.heappop(open_set)[1]
        if current == goal:
            path=[]
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        row ,col =current
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            neighbor = (row+dr,col+dc)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < columns:
                if grid[neighbor[0]][neighbor[1]]==0:
                    new_score = g_score[current] +1
                    if new_score < g_score.get(neighbor,float('inf')):
                        came_from[neighbor] = current
                        g_score[neighbor] = new_score
                        f = new_score+heuristic(neighbor,goal)
                        heapq.heappush(open_set,(f,neighbor))
    return None


grid = [
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,1,0],
    [0,1,0,0,0],
    [0,0,0,0,0]
]
path = astar(grid, (0,0), (4,4))
print("Path:", path)