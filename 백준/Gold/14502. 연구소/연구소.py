from collections import deque
from itertools import combinations
import copy
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

empty = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 0]
virus = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 2]

def bfs(lab_copy):
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and lab_copy[nx][ny] == 0:
                lab_copy[nx][ny] = 2
                q.append((nx, ny))
    return sum(row.count(0) for row in lab_copy)

max_safe = 0
for walls in combinations(empty, 3):
    temp_lab = copy.deepcopy(lab)
    for x, y in walls:
        temp_lab[x][y] = 1
    safe = bfs(temp_lab)
    max_safe = max(max_safe, safe)

print(max_safe)
