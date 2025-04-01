import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(a, b, visited, rem):
    q = deque()
    q.append((a, b))
    visited[a][b] = True  # 놓치기 쉬운 부분!

    while q:
        a, b = q.popleft()
        cnt = 0
        for i in range(4):
            new_a = a + dx[i]
            new_b = b + dy[i]
            if 0 <= new_a < N and 0 <= new_b < M:
                curr = graph[new_a][new_b]
                if curr == 0:
                    cnt += 1
                elif curr > 0 and not visited[new_a][new_b]:
                    visited[new_a][new_b] = True
                    q.append((new_a, new_b))
        rem[a][b] += cnt

def ice(n):
    rem = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    area = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and not visited[i][j]:
                area += 1
                check(i, j, visited, rem)

    if area == 0:
        return 0
    if area >= 2:
        return n

    for i in range(N):
        for j in range(M):
            graph[i][j] = max(0, graph[i][j] - rem[i][j])  # 빼고 음수 방지

    return ice(n + 1)

print(ice(0))
