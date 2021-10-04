from itertools import permutations as perm


def is_prime_number(num):
    if num < 2:
        return False
    else:
        for d in range(2, int(num ** .5) + 1):
            if num % d == 0:
                return False
    return True


def solution(numbers):
    pn_set = set()
    for l in range(1, len(numbers) + 1):
        for el in perm(numbers, l):
            num = int(''.join(el))
            if num not in pn_set:
                if is_prime_number(num):
                    pn_set.add(num)

    return len(pn_set)

