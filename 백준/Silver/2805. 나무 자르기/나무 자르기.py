import sys
N, M = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()
l = len(lst) # 배열길이

pl = 0
pr = lst[-1]
while pl < pr:
    s = 0
    mid = (pl+pr)//2
    for i in lst:
        if i > mid:
            s += i - mid  
    if s == M:
        print(mid)
        break
    elif s > M : #충분하다 -> 높이를 올린다.
        pl = mid + 1
    else:
        pr = mid - 1
else:
    s = 0
    for i in lst:
        if i > pl:
            s += i - pl 
    if s < M:
        print(pl-1)
    else:
        print(pl)