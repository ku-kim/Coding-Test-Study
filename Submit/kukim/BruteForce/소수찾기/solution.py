"""
	문제    : 소수찾기
    유형    : 수학, 구현
	난이도  : 하
	시간    : 15m
	uri    : https://pr ogrammers.co.kr/learn/courses/30/lessons/42839
    날짜    : 1o(21.6.23)
"""
from typing import List
import itertools

def is_prime(n):
    if n == 1 or n ==0:
        return False
    for i in range(2, (n//2) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    
    result = []
    for i in range(1, len(numbers) + 1):
        #result.append(list(map(list,itertools.permutations(numbers,i))))
        result.append(list(itertools.permutations(numbers,i)))
    nums = set()
    for n in result:
        for m in n:
            nums.add(int("".join(m)))
    
    count = 0
    for i in nums:
        if is_prime(i):
            count += 1
    return count

print(solution("17"))