import sys
N, K = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
plugs = set()
cnt = 0
for i,val in enumerate(lst):
    # 이미 꽂혀있으면 패스
    if val in plugs:
        continue
    # 아직 다 안찼으면 넣는다.
    if len(plugs) < N: 
        plugs.add(val)
    else:
        max_id = -1
        remov = None
        for plug in plugs:
            if plug not in lst[i+1:]:
                remov = plug
                break
            else:
                for j in range(i+1,K):
                    if plug == lst[j]:
                        if j > max_id:
                            max_id = j
                            remov = plug
                        break
        plugs.remove(remov)
        plugs.add(val)
        cnt += 1
print(cnt)