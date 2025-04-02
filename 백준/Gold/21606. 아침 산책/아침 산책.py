import sys
sys.setrecursionlimit(10**6)

N = int(input())
ck = [0] + list(map(int, sys.stdin.readline().strip()))  # 1-based index
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    visited[node] = True
    cnt = 1  # 자기 자신 포함
    for next in graph[node]:
        if not visited[next] and ck[next] == 1:
            cnt += dfs(next)
    return cnt

visited = [False] * (N + 1)
cnt_list = []
for i in range(1, N + 1):
    if not visited[i] and ck[i] == 1:
        c = dfs(i)
        cnt_list.append(c)

# 결과 계산 (이게 문제 요구사항)
answer = sum(c * (c - 1) for c in cnt_list)
answer += sum(cnt_list)  # 각 실내 노드 자기 자신만 산책하는 경우
print(answer)
