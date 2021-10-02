from collections import Counter
from heapq import heappush, heappop

def minSetSize(arr):
    ## 목표: 원소를 삭제해서 arr의 크기가 반이 될 수 있는 최소 원소집합을 구하여 집합크기를 리턴
    ## 1. (원소, 개수) 형태로 딕셔너리 만들기
    ## 2. "개수"만 따로 뽑아서 최대힙으로 만듦
    ## 3. 최대힙에서 원소를 하나 뽑을 때마다 count += 1
    ## 4. arr의 길이가 절반이하로 떨어지면 멈추고 count 리턴
    
    length = len(arr)
    maxheap = []
    count = 0
    
    for el in Counter(arr).values():
        heappush(maxheap, -el)
    
    while len(arr) / 2 < length:
        length += heappop(maxheap)
        count += 1
    
    return count