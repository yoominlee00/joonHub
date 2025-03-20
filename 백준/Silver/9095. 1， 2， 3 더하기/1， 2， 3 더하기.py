num =int(input())
def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1)*n

for _ in range(num):
    N = int(input())
    max_1 = N
    max_2 = int(N//2)
    max_3 = int(N//3)
    result_ =0
    for i in range(max_3+1):
        for j in range(max_2+1):
            total = N- i*3-j*2
            if (total)>=0:
                k = total
                result = factorial((i+j+k))/factorial(i)/factorial(j)/factorial(k)
                result_ +=result
    print(int(result_))
    


