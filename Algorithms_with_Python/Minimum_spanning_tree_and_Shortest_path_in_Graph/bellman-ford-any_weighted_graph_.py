from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


nodes = int(input())
edges = int(input())

graph = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    edge = Edge(source, destination, weight)
    graph.append(edge)

start = int(input())
target = int(input())

distance = [float('inf')] * (nodes + 1)
distance[start] = 0

parent = [None] * (nodes + 1)

# algorithm
for _ in range(nodes - 1):
    updated = False
    for edge in graph:
        if distance[edge.source] == float('inf'):
            continue
        new_distance = distance[edge.source] + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = edge.source
            updated = True
    if not updated:
        break

# cycle detection:
for edge in graph:
    new_distance = distance[edge.source] + edge.weight
    if new_distance < distance[edge.destination]:
        print("Negative Cycle Detected")
        break
else:
    path = deque()
    node = target

    while node is not None:
        path.appendleft(node)
        node = parent[node]

    print(*path)
    print(distance[target])
