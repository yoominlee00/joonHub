import sys
N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int,sys.stdin.readline().split())))

visited = [False]*N
path = []
val_lst =[]

def dfs(n,val):
    if n == N and lst[path[n-1]][path[0]] != 0:
        val += lst[path[n-1]][path[0]]
        val_lst.append(val)
        # print(path)
        return
    
    for i in range(N):
        if not visited[i]:
            if len(path) >= 1 and lst[path[n-1]][i] == 0:
                continue 
            visited[i] = True
            path.append(i)
            if len(path) >= 2 :
                val_new = val + lst[path[n-1]][path[n]]
            else:
                val_new = val
            dfs(n+1,val_new)
            path.pop()
            visited[i] = False


dfs(0,0)
print(min(val_lst))