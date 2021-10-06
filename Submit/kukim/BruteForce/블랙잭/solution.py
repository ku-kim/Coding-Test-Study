"""
	문제    : 블랙잭
    유형    : 완전탐색,
	난이도  : 하
	시간    : 5m
	uri    : https://www.acmicpc.net/problem/2798
    날짜    : 1o(21.7.1)
"""

# case 1 : combination
import itertools

n, m = map(int, input().split())
cards = list(map(int, input().split()))

brute_force = [sum(card) for card in list(itertools.combinations(cards, 3)) if sum(card) <= m]
print(max(brute_force))

# case 1.1 : cumtom combination
def combinations(nums,k):
    result = []
    def dfs(elements, start):
        if len(elements) == k:
            result.append(elements[:])
        for i in range(start, len(nums)):
            elements.append(nums[i])
            dfs(elements,i+1)
            elements.pop()
    dfs([],0)
    return result

n, m = map(int, input().split())
cards = list(map(int, input().split()))

brute_force = [sum(card) for card in list(combinations(cards, 3)) if sum(card) <= m]
print(max(brute_force))



# case 2 : loop

n, m = map(int, input().split())
cards = list(map(int, input().split()))

result = []
length = len(cards)

for i in range(length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            total = cards[i] + cards[j] + cards[k]
            if total <= m:
                result.append(total)
print(max(result))