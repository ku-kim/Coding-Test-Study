"""
1. 첫 시도
(1) 최대값을 score에, 인덱스를 pre_index에 저장함
(2) 원소를 돌며 각 원소에 score의 값을 더함. 
    단, index가 같은 경우 score의 좌/우 값을 더함 <- 좌/우가 항상 최대값이 아니라 틀림
2. 아래 코드  
(1) 1열의 같은 인덱스를 제외한 원소들 중 최대값을 2열 각 원소에 더함
(2) 4열까지 같은 방법 반복  

"""

def solution(land):
    for i in range(len(land) - 1):
        land[i + 1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i + 1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i + 1][2] += max(land[i][1], land[i][0], land[i][3])
        land[i + 1][3] += max(land[i][1], land[i][2], land[i][0])

    return max(land[-1])