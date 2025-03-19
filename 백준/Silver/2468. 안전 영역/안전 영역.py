import sys
sys.setrecursionlimit(100000)
N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

all_values = [lst[i][j] for i in range(N) for j in range(N)]
if not all_values:
    print(0)
    sys.exit()

max_height = max(all_values)
min_height = min(all_values)

count_lst = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def rain(x,y,h):
    visited[x][y] = True
    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]
        if 0<= nx < N and 0<= ny < N:
            if visited[nx][ny] == False and lst[nx][ny] > h:
                rain(nx,ny,h)

for h in range(min_height-1, max_height+1):
    visited = [[False]*N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False and lst[i][j] > h:
                rain(i,j,h)
                count+=1
    count_lst.append(count)

print(max(count_lst))
