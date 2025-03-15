a,b = map(list,input().split())
print(max("".join(a[::-1]),"".join(b[::-1])))