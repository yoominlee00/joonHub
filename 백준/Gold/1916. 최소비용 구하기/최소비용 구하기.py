import sys, heapq
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
start, end = map(int,sys.stdin.readline().split())

distance = [float('inf') for _ in range(N+1)]

def bus(start):
    distance[start] = 0
    q = [(0,start)]

    while q:
        dist, curr = heapq.heappop(q)
        if distance[curr] < dist:
            continue
        for neighbor, cost in graph[curr]:
            new_cost = dist + cost
            if new_cost < distance[neighbor]:
                distance[neighbor] = new_cost
                heapq.heappush(q, (new_cost,neighbor))

bus(start)
print(distance[end])
