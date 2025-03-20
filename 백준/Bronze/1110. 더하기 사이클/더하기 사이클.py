N =int(input())
def cycle(a,cnt):
    if cnt != 0 and a == N :
        print(cnt)
        return 
    if len(str(a)) == 1:
        st = '0'+str(a)
    else:
        st = str(a)
    sum = str(int(st[-2]) + int(st[-1])) 
    new = st[-1] + sum[-1] 
    new_int = int(new)
    cnt +=1
    cycle(new_int,cnt)
cycle(N,0)

