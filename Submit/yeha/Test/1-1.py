"""
(1) start로 시작 위치를 표시한다
(2) stations를 차례대로 돌며,
    기지국이 설치되어 있지 않은 거리(현재 위치 - 시작 위치 - 전파 범위(w))를
    전파가 닿는 범위(w * 2 + 1)로 나눈다
    이 값이 해당 거리에 필요한 기지국의 개수며, answer에 더해준다 
    만약 0보다 작다면 max함수에 의해 아무 것도 더해지지 않는다 
        소수점이 나올 경우 올림한다
(3) stations를 다 돌고 난 후 기지국이 설치되어 있지 않은 거리가 존재할 때, 
    기지국이 설치되어 있지 않은 거리(총 길이 - 현재 위치 + 1)를
    전파가 닿는 범위로(w * 2 + 1)로 나눈다 
    마찬가지로 올림하여 더한다 
"""
import math

def solution(n, stations, w):
    answer = 0

    start = 1
    for station in stations:
        answer += max(math.ceil((station - start - w) / (w * 2 + 1)), 0)
        start = station + w + 1

    if n >= start:
        answer += math.ceil((n - start + 1) / (w * 2 + 1))
    
    return answer
