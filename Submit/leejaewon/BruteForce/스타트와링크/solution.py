## 목표: 스타트팀의 능력치와 링크팀의 능력치의 차이가 최소가 되는 값을 리턴
## 1. 0부터 N까지 N/2개씩 짝지어 조합을 구한다.
## 2. 조합을 차례로 순회한다. (스타트 팀이라고 가정)
## 3. 스타트팀에 없는 사람들은 링크팀으로 생성
## 4. 두 팀의 능력치를 S에서 찾아 합산 (permutations)
import sys
from itertools import combinations, permutations

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

arr = list(combinations(range(N), N//2))
answer = 10000
for start, link in zip(arr[:len(arr)//2], list(reversed(arr[len(arr)//2:]))):
    start_ability = sum([S[i][j] for i, j in permutations(start, 2)])
    link_ability = sum([S[i][j] for i, j in permutations(link, 2)])
    answer = min(answer, abs(start_ability - link_ability))

print(answer)