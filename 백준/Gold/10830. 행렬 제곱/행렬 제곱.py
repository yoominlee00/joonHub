import sys 
N, B = map(int,sys.stdin.readline().split())
lst = []

for _ in range(N):
    lst.append(list(map(int,sys.stdin.readline().split())))

def multi(a,b):
    global N
    result = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += a[i][k]*b[k][j]
            result[i][j] = result[i][j] % 1000
    return result

def main(B):
    global lst
    if B == 1:
        return [[x % 1000 for x in row] for row in lst]
    if B % 2 == 0:
        a = main(B//2)
        return multi(a,a)
    else:
        a = main(B//2)
        new = multi(a,a)
        return multi(new,lst)
    
ans = main(B)
for _ in range(N):
    print(" ".join(map(str,ans[_])))

