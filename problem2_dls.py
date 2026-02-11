
grid = [
    [1, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0], [1, 0, 1, 1, 0], [0, 0, 1, 0, 0]
]

def dls(limit):
    start, goal = (5, 0), (3, 3)
    stack = [(start, [start], 0)]
    nodes_expanded = 0
    
    while stack:
        curr, path, depth = stack.pop()
        nodes_expanded += 1
        
        if curr == goal:
            return path, nodes_expanded
        
        if depth < limit:
            r, c = curr
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 6 and 0 <= nc < 5 and grid[nr][nc] == 0:
                    if (nr, nc) not in path:
                        stack.append(((nr, nc), path + [(nr, nc)], depth + 1))
                        
    return None, nodes_expanded

for l in [4, 8]:
    res_path, count = dls(l)
    status = "Success" if res_path else "Failed (Limit reached)"
    print(f"DLS Limit {l}: {status} | Nodes Expanded: {count}")
    if res_path: print(f"Path: {res_path}")