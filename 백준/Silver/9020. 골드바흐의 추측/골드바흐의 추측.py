test = int(input())
num = []
lst = []
def find_primes(n):
    primes = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):  # √i까지만 검사
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes
num = find_primes(10000)

for _ in range(test):
    test_num = int(input())
    for index,val in enumerate(num):
        if val >= test_num/2:
            lst_1 = num[:(index+1)][::-1]
            lst_2 = num[(index):]
            break
    for val in lst_1:
        if (test_num-val) in lst_2:
            print(val,test_num-val)
            break
             
