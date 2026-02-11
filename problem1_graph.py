from collections import deque

graph = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}

def search_graph(method='BFS'):
    start, goal = 'A', 'E'
    frontier = deque([start]) if method == 'BFS' else [start]
    explored = set()
    parent = {start: None}
    
    while frontier:
        node = frontier.popleft() if method == 'BFS' else frontier.pop()
         
        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1]
             
        explored.add(node)
         
        for neighbor in graph[node]:
            if neighbor not in explored and neighbor not in frontier:
                parent[neighbor] = node
                frontier.append(neighbor)
    return None

print(f"BFS Graph Path: {search_graph('BFS')}")
print(f"DFS Graph Path: {search_graph('DFS')}")