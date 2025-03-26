s = input()
stack = []

for ch in s:
    if ch == '(' or ch == '[':
        stack.append(ch)
    elif ch == ')':
        tmp = 0
        while stack:
            top = stack.pop()
            if top == '(':
                stack.append(2 if tmp == 0 else 2 * tmp)
                break
            elif type(top) == int:
                tmp += top
            else:
                print(0)
                exit()
        else:
            print(0)
            exit()
    elif ch == ']':
        tmp = 0
        while stack:
            top = stack.pop()
            if top == '[':
                stack.append(3 if tmp == 0 else 3 * tmp)
                break
            elif type(top) == int:
                tmp += top
            else:
                print(0)
                exit()
        else:
            print(0)
            exit()

# 최종 검사
res = 0
for val in stack:
    if type(val) == int:
        res += val
    else:
        print(0)
        exit()

print(res)
