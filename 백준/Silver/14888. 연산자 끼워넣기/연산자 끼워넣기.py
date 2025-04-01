import sys
N = int(input())
lst = list(map(int,sys.stdin.readline().split()))
cal = list(map(int,sys.stdin.readline().split()))
min_v = float('inf')
max_v = -float('inf')

def dfs(n,total):
    global min_v, max_v
    if n == len(lst):
        min_v = min(min_v,total)
        max_v = max(max_v,total)
        return
    now = lst[n]
    for i, val in enumerate(cal):
        if val != 0 :
            if i == 0:
                new_total = total + now
            elif i ==1:
                new_total = total - now
            elif i == 2:
                new_total = total * now
            else:
                new_total = abs(total) // now
                if total < 0:
                    new_total = -new_total
            cal[i] -= 1
            dfs(n+1,new_total)
            cal[i]+=1
            
dfs(1,lst[0])
print(max_v)
print(min_v)