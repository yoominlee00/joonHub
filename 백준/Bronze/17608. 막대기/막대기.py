import sys
N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.read().splitlines()))
pop = 0
cnt = 1
for _ in range(N):
    if _ > 0:
        new_pop = lst.pop()
        if new_pop > pop:
            cnt +=1
            pop = new_pop
    else:
        pop = lst.pop()
print(cnt)