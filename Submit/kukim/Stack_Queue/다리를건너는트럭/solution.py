"""
	문제    : 다리를 지나는 트럭
    유형    : 스택/큐
	난이도  : 하, lv2
	시간    : 30m
	uri    : https://programmers.co.kr/learn/courses/30/lessons/42583
    날짜    : 1x(21.9.8)
"""
# 최선의 경우 : case 4 O(n) 으로 해결

from typing import List
#### case 1 : list() + sum()
## 테스트케이스 5 : 9229ms
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_queue = [0 for _ in range(bridge_length)]
    # print(bridge_queue)
    while bridge_queue:
        time += 1
        bridge_queue.pop(0)
        if truck_weights:
            if sum(bridge_queue) + truck_weights[0] <= weight:
                bridge_queue.append(truck_weights.pop(0))
            else:
                bridge_queue.append(0)
    return time
    
#### case 2 : deque() + sum()
## 테스트케이스 5 : 시간초과
## why ? -> deque() 자료구조에서 sum() 매서드는 일반 리스트 sum() 보다 더 오래걸림 (더블링크드리스트 구조라 합이 더 오래걸리는 듯)
## 해결 : sum()를 매번하지않고 case 3 처럼 합을 변수로 설정하여 구하기
from collections import deque
def solution(bridge_length: int, weight: int, truck_weights: List[int]) -> int:
    truck_weights = deque(truck_weights)
    bridge_queue = deque([0] * bridge_length)

    time = 0
    while bridge_queue:
        time += 1
        bridge_queue.popleft()
        if truck_weights:
            if sum(bridge_queue) + truck_weights[0] <= weight:
                print(bridge_queue, truck_weights[0])
                bridge_queue.append(truck_weights.popleft())
            else:
                bridge_queue.append(0)
    return time

#### case 3 : list() + sum() X
## 테스트 5 〉	통과 (299.29ms, 10.3MB)
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_queue = [0 for _ in range(bridge_length)]
    bridge_weight = 0
    while bridge_queue:
        time += 1
        bridge_weight -= bridge_queue.pop(0)
        if truck_weights:            
            if truck_weights and bridge_weight + truck_weights[0] <= weight:
                new_truck = truck_weights.pop(0)
                bridge_weight += new_truck
                bridge_queue.append(new_truck)
            else:
                bridge_queue.append(0)
    return time

#### case 4 : deque + sum() X
## 테스트 5 〉	통과 (51.65ms, 10.3MB)
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_queue = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    bridge_weight = 0
    while bridge_queue:
        time += 1
        bridge_weight -= bridge_queue.popleft()
        if truck_weights:            
            if truck_weights and bridge_weight + truck_weights[0] <= weight:
                new_truck = truck_weights.popleft()
                bridge_weight += new_truck
                bridge_queue.append(new_truck)
            else:
                bridge_queue.append(0)
    return time

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]	
print(solution(bridge_length, weight, truck_weights))

