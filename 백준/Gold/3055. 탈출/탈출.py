
import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(R)]

q = deque()
s = deque()
visited = [[False]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        # 물 위치 : q에 저장
        if graph[i][j] == '*':
            q.append((i, j))
        # 두더지 위치: s에 저장
        elif graph[i][j] == 'S':
            s.append((i, j, 0))
            visited[i][j] = True

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while s:
    # 현재 물 위치 주변(.)을 물로 바꾸기
    for _ in range(len(q)):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == '.':
                    graph[nx][ny] = '*'
                    q.append((nx, ny))
    # 비버 가능한 위치, 오늘 날짜
    for _ in range(len(s)):
        x, y, day = s.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == 'D':
                    print(day + 1)
                    sys.exit()
                if graph[nx][ny] == '.' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    s.append((nx, ny, day + 1))

print("KAKTUS")
