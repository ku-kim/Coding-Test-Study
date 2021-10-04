from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_queue = deque([0] * bridge_length)
    truck_queue = deque(truck_weights)

    e_time = 0
    # sum(bridge_queue) != 0 or truck_queue 계속 시간 카운팅.
    while truck_queue:
        # 다리의 허용 하중을 초과하여 truck_queue에서 pop할 수 없으면
        # bridge_queue에는 0을 insert 한다.
        bridge_queue.popleft()
        if sum(bridge_queue) + truck_queue[0] <= weight:
            bridge_queue.append(truck_queue.popleft())
        else:
            bridge_queue.append(0)

        # 모든 트럭이 출발하기 전까지 매초 카운팅 한다.
        e_time += 1
    # 모든 트럭이 출발한 시점에 count + bridge_queue 요소의 수가 최종 결괏값이 되겠다.
    for i in range(len(bridge_queue) - 1, -1, -1):
        if bridge_queue[i] > 0:
            e_time += (i + 1)
            break

    answer = e_time
    return answer

