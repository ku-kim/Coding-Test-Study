from collections import deque

def solution(bridge_length, weight, truck_weights):
    ## 목표: 모든 트럭이 다리를 건너는데 걸리는 최소 초를 구해야함.
    ## 1. 다리에 트럭이 있다면 각각의 원소에 (무게, 위치+1)로 맵핑
    ## 2. 다리를 지나가는 중인 트럭들의 무게 + 대기열 첫번째 트럭의 무게 합을 구함
    ## 3. 합이 weigh보다 큰지 확인
        ## 3-1. 크면, 대기중인 트럭이 다리로 진입 불가능
        ## 3-2. 작으면, 대기열 첫 번째 트럭이 다리로 진입 (무게, 위치(최초 1))
    ## 4. sec += 1
    ## 5. 다리의 length보다 큰 위치 값을 가지는 트럭은 다리에서 제거
    ## 6. 다리와 트럭 대기열에 값이 없을 때까지 1에서 5 반복
    
    trucks = deque(truck_weights)
    bridge = []
    sec = 0
    
    while trucks or bridge:
        if bridge:
            bridge = list(map(lambda x: (x[0], x[1] + 1), bridge))
        
        if trucks and sum([w for w, _ in bridge]) + trucks[0] <= weight:
            bridge.append((trucks.popleft(), 1))
        
        sec += 1
        if bridge[0][1] >= bridge_length:
            bridge = bridge[1:]
            
    return sec + 1