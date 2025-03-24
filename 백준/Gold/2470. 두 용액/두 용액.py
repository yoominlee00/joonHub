import sys
N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()
result = []

for id, val in enumerate(lst):
    pl = 0 
    pr = N-1
    while pl <= pr:
        mid = (pl+pr)//2
        if (lst[mid] + val) > 0:
            pr = mid - 1
        else:
            pl = mid +1  
    # 후보군은 pl,pr


    if pr < 0:
        if pl != id:
            result.append([lst[pl], val])
        else:
            result.append([lst[pl+1], val])
    elif pl >= N:
        if pr != id:
            result.append([lst[pr], val])
        else:
            result.append([lst[pr-1], val])
    elif pl == id:
        result.append([lst[pr], val])
    elif pr == id:
        result.append([lst[pl], val])
    elif abs(val + lst[pl]) >= abs(val + lst[pr]):
        result.append([lst[pr], val])
    else:
        result.append([lst[pl], val])


print(" ".join(map(str, sorted(min(result, key=lambda sub: abs(sum(sub)))))))