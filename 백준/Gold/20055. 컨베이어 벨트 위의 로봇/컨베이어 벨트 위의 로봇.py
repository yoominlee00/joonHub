import sys
from collections import deque

N,K = map(int,sys.stdin.readline().split())
A_lst = list(map(int,sys.stdin.readline().split()))
cnt = 0
level = 0
start = 0
robots = [False]*2*N

while cnt <K :
    #1번 회전
    if start == 0:
        start = 2*N -1
    else:
        start -=1
    end = (start+N-1)
    if end >= 2*N:
        end -= 2*N

    if robots[end]:
        robots[end] = False

    #2번 이동
    for i in range(end,end-N,-1):
        if i < 0:
            i += 2*N
        val = robots[i]
        if val == True:
            next = (i+1)%(2*N)
            if not robots[next]: 
                if A_lst[next] > 0:
                    A_lst[next] -= 1
                    robots[i] = False
                    # 끝이 아니면 올리기
                    if end != (i+1)%(2*N):
                        robots[next] = True
    #3번 이동
    if not robots[start] and A_lst[start] > 0:
        robots[start] = True
        A_lst[start] -= 1
     
    cnt = 0
    for i in A_lst:
        if i == 0:
            cnt += 1

    level += 1    
    if cnt >= K:
        print(level)
        break

                
