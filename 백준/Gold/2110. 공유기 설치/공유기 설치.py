######문제 핵심#####공유기 설치 가능 최소 거리##########
import sys
N,C = map(int,sys.stdin.readline().split())


lst = list(map(int,sys.stdin.read().splitlines()))
lst.sort()
pl = 0
pr = lst[-1]-lst[0]

while pl < pr: 
    stack = []
    mid = (pl+pr)//2
    cnt = 1
    stack.append(lst[0])
    ## 목표 최소길이 보다 길면 ? 설치
    for i in range(N-1):
        if (lst[i+1]-stack[-1]) >= mid:
            stack.append(lst[i+1])
            cnt +=1
        else:
            continue
    if cnt >= C:
        pl = mid +1
    else:
        pr = mid -1


stack = []
stack.append(lst[0])
cnt = 1

for i in range(N-1):
    if (lst[i+1]-stack[-1]) >= pl:
        stack.append(lst[i+1])
        cnt +=1
    else:
         continue
if cnt < C:
    print(pl-1)
else:
    print(pl)
 
