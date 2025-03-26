import sys

M, N, L = map(int,sys.stdin.readline().split())
hunt = list(map(int,sys.stdin.readline().split()))
hunt.sort()
animal = []
cnt = 0

for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    animal.append((x,y))

def find(pl,pr,x):
    while pl <= pr:
        mid = (pl+pr)//2
        if hunt[mid] == x:
            return mid
        elif hunt[mid] < x:
            return find(mid+1,pr,x)
        else:
            return find(pl,mid-1,x)
    if pl >= len(hunt):
        return pr
    elif pr <= 0:
        return pl
    elif len(hunt)>1 and abs(hunt[pr]-x) >= abs(hunt[pr+1]-x):
        return pr+1
    else:
        return pr
    
for x, y in animal:
    hunt_id = find(0,len(hunt)-1,x)
    if abs(hunt[hunt_id] - x) + y <= L:
        cnt+=1
print(cnt)