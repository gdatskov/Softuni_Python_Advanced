from queue import PriorityQueue
from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


edges = int(input())
graph = {}

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(", ")]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    edge = Edge(source, destination, weight)
    graph[source].append(edge)

start = int(input())
target = int(input())

distance = [float('inf')] * len(graph)
parent = [None] * len(graph)

distance[start] = 0

pq = PriorityQueue()
pq.put((0, start))

while not pq.empty():
    min_distance, node = pq.get()
    if node == target:
        break
    for edge in graph[node]:
        new_distance = min_distance + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = node
            pq.put((new_distance, edge.destination))

if distance[target] == float("inf"):
    print("There is no such path.")
else:
    print(distance[target])

    path = deque()
    node = target
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    print(*path)





