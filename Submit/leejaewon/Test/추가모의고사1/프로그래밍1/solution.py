from collections import deque

def solution(n, stations, w):
    ## 목표: 추가로 기지국을 설치했을 때, 아파트 전체에 전파가 도달 할 수 있는 최대 기지국 개수를 리턴
    ## - 입력값이 2억 이하이므로, LogN이나 N으로 풀어야할 것 같음 -> DP 혹은 그리드, 이진탐색
    ## 1. idx:True형태의 딕셔너리 생성해서 base에 할당, stations을 deque로 저장
    ## 2. stations에서 1개 pop()
    ## 3. base[pop한 값]이 False이면 Continue
    ## 4. station을 포함한 +w, -w의 범위를 base에서 False로 만든다. (단, base의 범위 0부터 n까지만 생각한다.)
    ## 5. base에서 True값 위치를 stations에 넣는다.
    ## 6. base가 전부 False가 될 때까지 2-5번 반복
    
    stations = deque(stations)
    base = {i+1: True for i in range(n)}
    
    while all(base):
        while stations:
            s = stations.popleft()

            for i in range(s-w, s+w+1):
                base[i] = False

        stations += deque([key for key, val in base.items() if val])
        
    print(base)