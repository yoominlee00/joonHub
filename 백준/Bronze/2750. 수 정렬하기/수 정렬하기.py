num = int(input())
list = []
for _ in range(num):
    list.append(int(input()))
list.sort()
for _ in list:
    print(_)
