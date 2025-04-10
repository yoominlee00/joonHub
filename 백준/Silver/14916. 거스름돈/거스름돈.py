N = int(input())
total = N 

if total < 5 and total %2 ==1:
    print(-1)
else: 
    num = N // 5
    if N % 2 ==1 and num % 2 == 0:
        num -= 1
    elif N % 2 == 0 and num % 2 == 1:
        num -= 1
    total -= num*5
    num += total // 2
    print(num)