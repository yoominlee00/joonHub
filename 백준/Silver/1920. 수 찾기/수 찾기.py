import sys
N1 = int(input())
l1 = list(map(int,list(input().split())))
N2 = int(input())
l2 = list(map(int,list(input().split())))

l1.sort()
for key in l2:
    pl = 0
    pr = len(l1)-1
    while True:
        mid = ( pl + pr )//2
        m = l1[mid]
        if m == key:
            print(1)
            break
        elif m > key:
            pr = mid -1
        else:
            pl = mid + 1
        if pl > pr:
            print(0)
            break 