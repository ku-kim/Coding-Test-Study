from itertools import permutations
from math import sqrt


def is_prime(num):
    if num < 2:
        return 0
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1


def solution(numbers):
    nums_set = set()

    for i in range(1, len(numbers) + 1):
        nums_set |= set(
            map(int, map(''.join, permutations(list(numbers), i))))

    answer = 0
    for num in nums_set:
        answer += is_prime(num)
    return answer
