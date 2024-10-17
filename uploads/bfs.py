graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3]
}
start = 0
queue = [start]
visited = set()
while queue:
    vertex = queue.pop(0)
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
