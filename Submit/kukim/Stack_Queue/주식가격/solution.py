"""
	문제    : 주식가격
    유형    : 스택/큐
	난이도  : 하
	시간    : 
	uri    : https://programmers.co.kr/learn/courses/30/lessons/42584
    날짜    : 1o(21.9.2)
"""
from typing import List

#### Case 1 : 완전탐색
## 효율성 테스트 1 〉	통과 (122.67ms, 18.8MB) 
# Big-O : O(n^2)
def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            count += 1
            if prices[i] > prices[j]:
                break
        answer.append(count)
    return answer

#### case 2 : stack
## 효율성 테스트 1 〉	통과 (24.66ms, 19.3MB)
def solution(prices):
    length = len(prices)
    
    # answer을 max값으로 초기화  
    answer = [ i for i in range (length - 1, -1, -1)]
    print(answer)
    ## 주식 가격이 떨어질 경우 찾기
    stack = [0]
    for i in range (1, length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer

prices = [1,2,3,2,3]

print(solution(prices))
