from collections import deque

def solution(arr):
    ## 목표: 회의실을 사용할 수 있는 최대 팀 수를 반환
    ## 풀이: 입력값 개수가 10만이하 N이나 N*LogN으로 풀이 -> 힙, 우선순위큐, 정렬, DP(X), 다익스트라(X)
    ## 1. arr을 시작시간, 종료시간 기준순으로 정렬한다.
    ## 2. arr을 deque(arr)로 재할당하고, stack = [arr.popleft()]
    ## 3. arr[0][0]이 stack[-1][1] 보다 크거나 같으면 stack.append(arr.popleft())
    ## 4. 아니면 그냥 arr.popleft()
    ## 5. arr에 원소가 없어질때까지 3-4번 반복
    ## 6. stack의 길이 반환
    
    arr.sort(key=lambda x: (x[0], x[1]))
    arr = deque(arr)
    stack = [arr.popleft()]
    
    while arr:
        if stack[-1][1] <= arr[0][0]:
            stack.append(arr.popleft())
        else:
            arr.popleft()
    
    return len(stack)