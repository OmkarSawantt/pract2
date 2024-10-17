graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3]
}
start = 0
stack = [start]
visited = set()
while stack:
    vertex = stack.pop()  
    if vertex not in visited:
        print(vertex, end=" ")  
        visited.add(vertex)  
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                stack.append(neighbor)
