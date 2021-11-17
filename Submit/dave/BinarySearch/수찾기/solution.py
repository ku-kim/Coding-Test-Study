from collections import defaultdict

# solution1: with binary search
N = int(input())
A = list(map(int, input().split()))
M = int(input())
A.sort()

for num in list(map(int, input().split())):
    s_idx = 0
    e_idx = N - 1
    is_find = False
    while s_idx <= e_idx:
        m_idx = s_idx + (e_idx - s_idx) // 2
        if A[m_idx] == num:
            print(1)
            is_find = True
            break
        elif A[m_idx] > num:
            e_idx = m_idx - 1
        else:
            s_idx = m_idx + 1
    if not is_find:
        print(0)


# solution2: with hash
"""
딕셔너리 하나 선언하고 선형으로 A에 저장될 데이터를 인덱스화 시킨다.
찾고자 하는 데이터를 인덱스로 접근해서 키에러 = 0 아니면 1 출력한다.
"""
N = int(input())
A = dict()
for n in map(int, input().split()):
    A[n] = n
M = int(input())
for fn in map(int, input().split()):
    try:
        if A[fn]:
            print(1)
    except KeyError:
        print(0)

