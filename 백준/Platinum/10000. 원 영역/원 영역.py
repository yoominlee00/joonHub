import sys
N = int(sys.stdin.readline())
l = []
stack = []
big = []

for i in range(N):
    a, r = list(map(int,sys.stdin.readline().split()))
    l.append(((i,a-r,r,0))) #시작 : 0
    l.append(((i,a+r,r,1))) #끝 :1
# l.sort(key = lambda x : (x[1],-x[3],-x[2]))
used = [False]*N
l.sort(key=lambda x: (x[1], 0 if x[3]==1 else 1, x[2] if x[3]==1 else -x[2]))
last_type = None
last_x = None

for id, x, r, type in l:
    if last_type is not None:
        if last_type == 0:
            if type == 0:
                if x == last_x :
                    used[stack[-1]] = True
                    stack.append(id)
                else:
                    stack.append(id)
            else:
                stack.pop()
        else:
            if type == 0:
                if x != last_x:
                    used[stack[-1]] = False
                    stack.append(id)
                else:
                    stack.append(id)
            else:
                if x != last_x:
                    used[stack[-1]]=False
                    stack.pop()
                else:
                    stack.pop()
    else:
        stack.append(id)
    last_type = type
    last_x =x

print(N+1+sum(used))

