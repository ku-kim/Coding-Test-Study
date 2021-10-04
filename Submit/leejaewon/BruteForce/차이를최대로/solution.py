import sys
from itertools import permutations

## 목표: arr의 순서를 바꿔 가면서 주어진 식의 최대 값을 리턴
## 1. arr의 순열을 구한다.
## 2. 각각의 순열을 주어진 식으로 변형해서 합을 산출한다.
## 3. answer = max(answer, 2번값)으로 최대값을 구한다.
## 4. 2, 3번을 반복한다.
n = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
answer = 0

for p in permutations(arr, n):
    answer = max(answer, sum(map(lambda x: abs(x[0] - x[1]), zip(p, p[1:]))))

print(answer)