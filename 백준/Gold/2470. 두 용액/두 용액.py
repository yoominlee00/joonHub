import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
result = []

for id, val in enumerate(lst):
    target = -val
    pl = 0 
    pr = len(lst) - 1
    # 이분 탐색: target = -val에 가장 가까운 후보를 찾는다.
    while pl <= pr:
        mid = (pl + pr) // 2
        if lst[mid] < target:
            pl = mid + 1
        else:
            pr = mid - 1

    # 후보 인덱스는 pr와 pl이다.
    # pr와 pl 중 자기 자신(id)와 겹치지 않는, 두 용액의 합의 절댓값이 최소인 후보를 선택.
    candidate = None
    if pr >= 0 and pr != id:
        candidate = lst[pr]
    if pl < len(lst) and pl != id:
        # 두 후보가 모두 유효하면, 둘 중 합의 절댓값이 작은 것을 선택
        if candidate is None or abs(val + lst[pl]) < abs(val + candidate):
            candidate = lst[pl]
    
    # 후보가 선택되었으면 result에 (val, candidate) 쌍을 추가.
    if candidate is not None:
        result.append([val, candidate])

# result에 저장된 쌍들 중, 두 용액의 합 절댓값이 최소인 쌍을 선택
best_pair = min(result, key=lambda sub: abs(sum(sub)))
best_pair = sorted(best_pair)
print(best_pair[0], best_pair[1])
