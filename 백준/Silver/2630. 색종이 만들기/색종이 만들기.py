import sys
N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(list(map(int,sys.stdin.readline().split())))
wh=0
bl=0


def check(N,a,b):
    global wh, bl 
    sum1, sum2, sum3, sum4 = 0, 0, 0, 0
    d = N//2
    dd = d*d
    for i in range(b,b + d):
        sum1 += sum(lst[i][a:a+d])
        sum2 += sum(lst[i][a+d:a+N])
    for i in range(b+d,b+N):
        sum3 += sum(lst[i][a:a+d])
        sum4 += sum(lst[i][a+d:a+N])

    if (sum1+sum2+sum3+sum4) == N*N:
        bl +=1
        return
    elif (sum1+sum2+sum3+sum4) == 0:
        wh +=1
        return

    if sum1 == 0:
        wh+=1
    elif sum1 == dd:
        bl+=1
    else:
        check(d,a,b)

    if sum2 == 0:
        wh+=1
    elif sum2 == dd:
        bl+=1
    else:
        check(d,a+d,b)

    if sum3 == 0:
        wh+=1
    elif sum3 == dd:
        bl+=1
    else:
        check(d,a,b+d)

    if sum4 == 0:
        wh+=1
    elif sum4 == dd:
        bl+=1
    else:
        check(d,a+d,b+d)



check(N,0,0)
print(wh)
print(bl)