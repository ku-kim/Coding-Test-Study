"""
피자를 순서대로 하나씩 취해서, 넣을 수 있는 최대 깊이 즉,
넣으려는 피자 직경보다 작은 직경의 오븐 층 + 1층에 넣는다.

모든 오븐 층을 다 사용하고 피자가 남는 경우 또는 피자를 넣을 수 있는
직경의 오븐층이 없는 경우는 0을 출력한다.

모든 피자를 오븐에 넣은 경우 마지막 피자가 들어간 오븐 층을 출력한다.
"""
D, N = map(int, input().split())
oven_diameters = dict()
idx = 1
for od in map(int, input().split()):
    oven_diameters[idx] = od
    idx += 1
pizza_diameters = list(map(int, input().split()))
e = D + 1
for pd in pizza_diameters:
    if e == 1:
        print(0)
        break
    is_in_oven = False
    for i in range(1, e):
        if oven_diameters[i] < pd:
            is_in_oven = True
            e = i
            break
    else:
        is_in_oven = True
        e = i - 1
    if not is_in_oven:
        print(0)
        break
else:
    print(i - 1)
