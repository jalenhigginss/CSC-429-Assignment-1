from collections import deque

grid = [
    [1, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0], [1, 0, 1, 1, 0], [0, 0, 1, 0, 0]
]

def get_neighbors(pos):
    r, c = pos
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    results = []
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 6 and 0 <= nc < 5 and grid[nr][nc] == 0:
            results.append((nr, nc))
    return results

def search_grid(method='BFS'):
    start, goal = (5, 0), (3, 3)
    frontier = deque([start]) if method == 'BFS' else [start]
    explored = set()
    parent = {start: None}
    
    while frontier:
        curr = frontier.popleft() if method == 'BFS' else frontier.pop()
        
        if curr == goal:
            path = []
            while curr:
                path.append(curr)
                curr = parent[curr]
            return path[::-1]
            
        explored.add(curr)
        for neighbor in get_neighbors(curr):
            if neighbor not in explored and neighbor not in frontier:
                parent[neighbor] = curr
                frontier.append(neighbor)
    return None

print(f"BFS Grid Path: {search_grid('BFS')}")
print(f"DFS Grid Path: {search_grid('DFS')}")