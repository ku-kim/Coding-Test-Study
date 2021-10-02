from itertools import permutations

def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

def solution(numbers):
    s = set()
    for i in range(1, len(numbers) + 1):
        s |= set(map(lambda x: int(''.join(x)), permutations(numbers, i)))
    
    return len([num for num in s if isPrime(num)])