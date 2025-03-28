import sys
sys.setrecursionlimit(10**6)
N = int(input()) 
tree = {}
visited = [False]*N
parent = [None]*N

for _ in range(N-1):
    a, b = list(map(int,sys.stdin.readline().split()))
    tree.setdefault(a, []).append(b)
    tree.setdefault(b, []).append(a)    

def dfs(node):
    visited[node-1] = True
    for i in tree[node]:
        if not visited[i-1]:
            parent[i-1] = node
            dfs(i)
dfs(1)
print('\n'.join(map(str,parent[1:])))