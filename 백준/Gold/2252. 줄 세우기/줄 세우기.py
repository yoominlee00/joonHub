import sys
N, M = map(int,sys.stdin.readline().split())
# indegree = [0]*(N+1)
lst = []
result = []
for _ in range(N+1):
    lst.append([])

for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    lst[a].append(b)
    # indegree[b] += 1


visited = [False]*(N+1)
# dfs 버전
def graph(node):
    visited[node] = True
    for i in lst[node]:
        if not visited[i]:
            graph(i)
    result.append(node)

for i in range(1,N+1):
    if not visited[i]:
        graph(i)

result.reverse()
print(' '.join(map(str,result)))