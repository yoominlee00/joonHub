import sys
N = int(input())
card = list(map(int, sys.stdin.readline().split()))
M = int(input())
lst = list(map(int,sys.stdin.readline().split()))
card.sort()
result = []



def find(pl,pr,n):
    while pl < pr:
        mid = (pl + pr)//2
        if card[mid] == n:
            return 1
        elif card[mid] < n:
            pl = mid +1
        else:
            pr = mid -1
    if card[pl] != n:
        return 0
    else:
        return 1

for i in lst:
    a = find(0,len(card)-1,i)
    result.append(a)

print(' '.join(map(str,result)))