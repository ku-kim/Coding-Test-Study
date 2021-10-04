# product를 사용하면 시간초과에 걸린다.
# from itertools import product
#
#
# N = int(input())
# s = []
# for p in product(['1', '2', '3'], repeat=N):
#     is_right_seq = True
#     for i in range(N - 1):
#         for j in range(i + 2, N + 1):
#             if p[i:(i + j) // 2] == p[(i + j) // 2:j]:
#                 is_right_seq = False
#                 break
#         if not is_right_seq:
#             break
#     else:
#         print(''.join(p))
#         break


"""
1   2   1   2   1
                3
            3   1
                2
        3   1   2
                3
            2   1
                3
    3   1   2   1
                3
            3   1
                2
        2   1   2
                3
            3   1
                2
back tracking으로 접근해보자.
새롭게 추가된 요소를 기준으로 인덱스를 앞으로 옮겨가면서
{추가된 요소 ~ 인덱스} 와 {인덱스 ~ (추가된 요소 ~ 인덱스 사이의 거리만큼 떨어진 인덱스)} 를 비교하여
모두 동일하지 않은 경우에 한해 좋은 수열로 판정.
"""
N = int(input())

def check(num):
    length = len(num)
    for idx in range(1, length//2 + 1):
        if num[-idx:] == num[-(idx*2):-idx]:
            return False
    else:
        return True

def get_good_seq(N, seq):
    if len(seq) == N:
        return seq
    for last_num in '123':
        seq.append(last_num)
        is_good_seq = check(seq)
        if is_good_seq:
            get_good_seq(N, seq)
            if len(seq) == N:
                return seq
            else:
                seq.pop()
                continue
        else:
            seq.pop()


print(''.join(get_good_seq(N, ['1'])))

