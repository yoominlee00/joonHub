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
    return pl 
    
for x, y in animal:
    id = find(0,len(hunt)-1,x)
    for i in [id - 1, id]:  # 두 후보 다 확인
        if 0 <= i < len(hunt):
            if abs(hunt[i] - x) + y <= L:
                cnt += 1
                break
        
print(cnt)