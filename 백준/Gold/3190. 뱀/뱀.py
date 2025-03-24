from collections import deque
import sys 

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
app = []
dir = []
snail = deque()
dir = deque()

n =1
status = 'r'
snail.append((1,1))
for _ in range(K):
    a, b = map(int,sys.stdin.readline().split())
    app.append((a,b))

N2 = int(sys.stdin.readline())

for _ in range(N2):
    a, b = sys.stdin.readline().split()
    dir.append((int(a),b))

while True:
    if dir:
        t = dir[0][0]
        s = dir[0][1]
    a,b = snail[0]
    if status == 'l':
        if (b-1) < 1 or (a,b-1) in snail:
            break
        snail.appendleft((a,b-1))
        if (a,b) not in app:
            snail.pop()
        else:
            app.remove((a,b))
    elif status == 'r':
        if (b+1) > N or (a,b+1) in snail:
            break
        snail.appendleft((a,b+1))
        if (a,b) not in app:
            snail.pop()
        else:
            app.remove((a,b))
    elif status == 'u':
        if (a-1) < 1 or (a-1,b) in snail:
            break
        snail.appendleft((a-1,b))
        if (a,b) not in app:
            snail.pop()
        else:
            app.remove((a,b))
    else:
        if (a+1) > N or (a+1,b) in snail:
            break
        snail.appendleft((a+1,b))
        if (a,b) not in app:
            snail.pop()
        else:
            app.remove((a,b))
    ##### 방향 전환 체크 ! ####
    if n == t:
        if status == 'l':
            if s == 'L':
                status = 'd'
            else:
                status = 'u'
        elif status == 'r':
            if s == 'L':
                status = 'u'
            else:
                status = 'd'
        elif status == 'u':
            if s == 'L':
                status = 'l'
            else:
                status = 'r'
        else:
            if s == 'L':
                status = 'r'
            else:
                status = 'l'
        dir.popleft()
    n += 1
print(n)