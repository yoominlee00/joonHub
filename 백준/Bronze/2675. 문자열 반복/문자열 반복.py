case_num = int(input())
for _ in range(case_num):
    iter, char = input().split()
    print("".join(list(map(lambda x : x*int(iter),list(char)))))