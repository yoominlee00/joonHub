import sys

T = int(input())

def check(a,b):
    strike = 0
    ball = 0
    for i,ival in enumerate(str(a)):
        for j, jval in enumerate(str(b)):
            if ival == jval:
                if i == j:
                    strike += 1
                else:
                    ball += 1
    return strike, ball
nums = []
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i ==j or j ==k or k ==i:
                continue
            else:
                nums.append(int(str(i)+str(j)+str(k)))


ans = []
for t in range(T):
    a, strike, ball = map(int,sys.stdin.readline().split())
    new_ans = []
    for num in nums:
        st, ba = check(num,a)
        if strike == st and ball == ba:
            if t == 0:
                ans.append(num)
            else:
                if num in ans:
                    new_ans.append(num)
    if t != 0:
        ans = new_ans

print(len(ans))
    

    
