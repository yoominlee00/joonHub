import sys

lst = sys.stdin.readlines()
a = list(map(int, lst))
total = sum(a)
found = False
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if total - a[i] - a[j] == 100:
            first = a[i]
            second = a[j]
            a.remove(first)
            a.remove(second)
            found =True
            break
    if found:
        break

a.sort()
for num in a:
    print(num)