import sys
from collections import deque
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
indegree = [0]*(N+1)
stack = []
for _ in range(M):
    b, a, c = map(int,sys.stdin.readline().split())
    # b를만들기 위해 a가 c 개 필요하다.
    graph[a].append((b,c))
    indegree[b] += 1
##count[x][y] : x 만들기 위해 필요한 y 부품개수
count = [[0] * (N+1) for _ in range(N+1)]
q= deque()

# 진입차수 0 인거 q에 넣고, count 자기자신 -> 1
# 진입차수 0 : 기본 부품 ! 이외에 것들은 모두 0으로 처리 : 필요없음
for i in range(1,N+1):
    if indegree[i] == 0:
        # index만 넣는다.
        q.append(i)
        count[i][i] = 1

while q:
    now = q.popleft()
    for next, cnt in graph[now]:
        #### 이부분이해하기 !####
        for i in range(1,N+1):
            count[next][i] += count[now][i] * cnt
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)
            
for i in range(1, N+1):
    if count[N][i] > 0:
        print(i, count[N][i])


