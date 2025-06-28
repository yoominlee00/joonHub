import sys
while True:
    lst = list(map(int,sys.stdin.readline().split()))
    num = lst[0]
    ll = []
    def check(ll,n):
        if len(ll) == 6 or n == num+1:
            if len(ll) == 6:
                print(' '.join(ll))
            return
        ll.append(str(lst[n]))
        check(ll,n+1)
        ll.pop()
        check(ll,n+1)
    
    check(ll,1)  
    print(' ')    
    if len(lst) == 1 and lst[0] == 0: 
        break