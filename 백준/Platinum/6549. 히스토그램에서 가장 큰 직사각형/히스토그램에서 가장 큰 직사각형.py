import sys

def max_s(pl,pr):
    global lst
    mid = (pl + pr)//2
    if pl +1  == pr:
        return max(lst[pl], lst[pr], min(lst[pl], lst[pr]) * 2)
    if pl == pr:
        return lst[pl]
    
    s1 = max_s(pl,mid)
    s2 = max_s(mid+1,pr)
    
    l = mid
    r = mid+1
    m = min(lst[l],lst[r])
    s = m*2
    while l > pl or r < pr:
        if r < pr and (l == pl or lst[l - 1] < lst[r + 1]):
            r += 1
            m = min(m, lst[r])
        else:
            l -= 1
            m = min(m, lst[l])
        s = max(s, m * (r - l + 1))


    return max(s1,s2,s)
    
while True:
    lst = list(map(int,sys.stdin.readline().split()))
    if lst[0] == 0:
        break
    N = lst[0]
    lst = lst[1:]
    print(max_s(0,len(lst)-1))
    

