import sys
N = int(sys.stdin.readline())
l = []
stack = []
radius = [0]*N
cnt = 0
for i in range(N):
    a, r = list(map(int,sys.stdin.readline().split()))
    l.append(((i,a-r,r,0))) #시작 : 0
    l.append(((i,a+r,r,1))) #끝 :1

l.sort(key=lambda x: (x[1], 0 if x[3]==1 else 1, x[2] if x[3]==1 else -x[2]))
last_type = None
last_x = None

for id, x, r, type in l:
    if type == 0:
        stack.append(id)
    elif type == 1:
        if radius[id] == r:
            cnt +=1
        stack.pop()
        if stack:
            radius[stack[-1]] += r
    
        
print(cnt+1+N)