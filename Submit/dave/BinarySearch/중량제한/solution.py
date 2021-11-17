"""
풀이1: Binary Search를 사용하여 해결.
    1. 주어진 다리 정보를 정렬하되 하중 기준으로 오름차순 정렬한다.
    2. 가장 낮은 하중 < 가장 높은 하중를 만족하는 동안
       가장 낮은 하중 ~ 가장 높은 하중의 중간 값 이상의 다리로만 BFS를 진행
        if 섬1에서 섬2까지 탐색 가능:
            가장낮은 하중 = 중간하중 + 1 로 변경 후 2번 진행
        else:
            가장높은 하중 = 중간하중 - 1로 변경 후 2번 진행


풀이2: union find를 사용하여 해결.
    1. 간선정보를 하중 기준 내림차순으로 정렬
    2. 가장 높은 하중의 간선 부터 모든 간선에 대해 다음과 같이 처리
        1. 간선의 노드들을 union하여 연결함.
        2. 시작 섬과, 도착 섬의 부모 노드를 각각 find parent하여 동일한 루트 노드이면 연결이 된 것이므로
           선택한 간선의 하중이 찾는 답이 된다. 따라서 루프를 종료하고 현재 간선의 하중을 출력해주면 된다.


test case1
3 3
1 2 2
3 1 3
2 3 2
1 3

expected: 3

test case2
9 9
1 4 11
1 5 2
4 5 4
4 3 10
4 2 7
5 2 10
5 6 13
3 2 9
2 6 8
1 6

expected: 9
"""
import heapq
from collections import deque
import sys

f_input = sys.stdin.readline


def is_conn(al, m):
    visited = [0] * (N + 1)
    queue = deque()
    queue.append(i1)
    visited[i1] = 1

    while queue:
        ci = queue.popleft()
        for ni, w in al[ci]:
            if visited[ni] == 0 and w >= m:
                if ni == i2:
                    return True
                queue.append(ni)
                visited[ni] = 1

    return False


def solution_with_binarysearch():
    a_list = [[] for _ in range(N + 1)]  # adjacency list
    max_weight = 0
    for A, B, C in bridges:
        a_list[A].append([B, C])
        a_list[B].append([A, C])
        if max_weight < C:
            max_weight = C

    min_weight = 1
    while min_weight <= max_weight:
        mid_weight = min_weight + (max_weight - min_weight) // 2
        if is_conn(a_list, mid_weight):
            min_weight = mid_weight + 1
        else:
            max_weight = mid_weight - 1

    return max_weight


def union(parent, N1, N2):
    p1 = find_parent(parent, N1)
    p2 = find_parent(parent, N2)
    if p1 < p2:
        parent[p2] = p1
    else:
        parent[p1] = p2


def find_parent(parent, N):
    if parent[N] != N:
        parent[N] = find_parent(parent, parent[N])

    return parent[N]


def solution_with_unionfind():
    parent = dict()
    for i in range(N + 1):
        parent[i] = i

    heap = list()
    for A, B, C in bridges:
        heapq.heappush(heap, [-C, A, B])

    while heap:
        C, A, B = heapq.heappop(heap)
        union(parent, A, B)
        if find_parent(parent, i1) == find_parent(parent, i2):
            return -C


N, M = map(int, f_input().split())
bridges = [list(map(int, f_input().split())) for _ in range(M)]
i1, i2 = map(int, f_input().split())

print(solution_with_binarysearch())
print(solution_with_unionfind())

