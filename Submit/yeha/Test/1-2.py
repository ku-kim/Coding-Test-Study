"""
(1) arr를 첫번째: 종료 시간, 두번째: 시작 시간에 맞추어 정렬한다
(2) 원소를 돌며 시작 시간이 종료 시간보다 늦는지 확인한다
(3) 늦는다면 prev_end를 이전 종료 시간으로 갱신한다. count를 하나 센다. 

"""

def solution(arr):
    arr.sort(key = lambda x: (x[1], x[0]))
    # print(max(arr)[1])

    count = 1
    prev_end = arr[0][1]
    for meet in arr[1:]:
        if prev_end <= meet[0]:
            count += 1
            prev_end = meet[1]
    return count