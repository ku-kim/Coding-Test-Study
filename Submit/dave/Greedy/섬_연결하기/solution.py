import heapq


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, costs):
    parent = [0]
    for i in range(1, n):
        parent.append(i)

    # 간선 정보를 저장할 heap을 선언한다.
    edges = []
    result = 0
    for cost in costs:
        a, b, cost = cost
        # heap을 사용하여 항상 최소 비용 간선을 추출할 수 있도록 한다.
        heapq.heappush(edges, (cost, a, b))

    # 모든 간선을 순회하면서
    while edges:
        # 가장 가중치가 낮은 간선을 선택하여
        cost, a, b = heapq.heappop(edges)

        # 해당 간선을 사용할 시 순환이 발생하는지 확인해서 순환이 발생하지 않는 경우는
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            # 간선의 가중치를 결과에 더해준다.
            result += cost

    import heapq


def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])

    return parent[node]


def union(parent, a, b):
    pa = find_parent(parent, a)
    pb = find_parent(parent, b)

    if pa > pb:
        parent[pa] = pb
    else:
        parent[pb] = pa


def solution(n, costs):
    ans = 0
    edges = list()
    # 1. 간선 데이터를 비용 오름차순으로 정렬
    # push (cost, a, b) data in heap
    for cost in costs:
        heapq.heappush(edges, (cost[2], cost[0], cost[1]))

    # parent table 초기화
    parent = dict()
    for i in range(n):
        parent[i] = i

    e_cnt = 0
    # 2. 순환이 발생하는지 확인하면서 발생하지 않는 경우만 가중치를 더해간다.
    while True:
        cost, a, b = heapq.heappop(edges)
        # 순환이 발생하지 않으면 가중치를 더하고 e_cnt + 1
        # 두 노드의 부모 테이블이 같지 않으면 순환이 발생하지 않는다.
        if find_parent(parent, a) != find_parent(parent, b):
            # a와 b를 잇는 간선을 추가한다.
            union(parent, a, b)
            ans += cost
            e_cnt += 1
        # 추가된 간선이 정점 - 1개에 도달하면 Minimum spanning tree 완성.
        if e_cnt == n - 1:
            break

    return ans
return result
