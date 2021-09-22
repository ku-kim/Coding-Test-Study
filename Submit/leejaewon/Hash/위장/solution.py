from collections import Counter
from functools import reduce

def solution(clothes):
    ## 목표: 매일 다른 옷을 입을 수 있는 경우의 수를 구한다.
    ## 1. 옷 종류마다 몇개가 있는지 확인
    ## 2. 종류마다 안입는 경우도 있으니 원래 수에 1씩 더하여 경우의 수를 구한다.
    ## 3. 아무것도 입지 않는 경우의 수는 없으니 2번 결과에서 1을 빼주고, 리턴한다.
    
    cnt = Counter([kind for item, kind in clothes])
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1)
    return answer - 1