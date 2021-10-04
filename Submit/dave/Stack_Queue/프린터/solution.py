from collections import deque


# 본인 코드
def solution(priorities, location):
    queue = deque()
    for i in range(len(priorities)):
        queue.append((priorities[i], i))

    deque_cnt = 0
    while queue:
        # 팝할 차례의 요소보다 우선순이가 높은 요소가 있는지 확인한다.
        # 처음에 max priority 요소를 찾기 위해 queue를 list로 변환 후 내장 정렬
        # api를 사용했으나, (2, 0), (2, 1), (2, 4)와 같이 정렬 될 것으로 기대했으나
        # (2, 4), (2, 1), (2, 1)과 같이 정렬되는 것을 확인했다.
        # api를 사용하려면 별도로 컴페리이터를 통해 커스터마이징 하게 정렬을 하던가
        # 아래와 같이 선형 탐색으로 max priority를 확인해야만 순서가 뒤바뀌는 실수를
        # 막을 수 있다.
        max_elem = queue[0]
        for i in range(1, len(queue)):
            if max_elem[0] < queue[i][0]:
                max_elem = queue[i]

        if max_elem[0] > queue[0][0]:
            for i in range(len(queue)):
                if queue[0][0] < max_elem[0]:
                    queue.append(queue.popleft())
                else:
                    elem = queue.popleft()
                    deque_cnt += 1
                    break
        else:
            elem = queue.popleft()
            deque_cnt += 1
        if elem[1] == location:
            return deque_cnt


# 추천 코드
def solution(priorities, location):
    # (locaion, priority) 형태의 튜플을 만들어 queue에 넣어준다.
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    answer = 0
    while queue:
        # 출력할 원소를 queue에서 꺼낸다.
        p_data = queue.popleft()
        # 큐 내부 원소 가운데 출력할 원소보다 우선순위가 높은 것이 있으면...
        if any(p_data[1] < q_data[1] for q_data in queue):
            # 출력하지 않고 queue에 다시 넣어준다.
            queue.append(p_data)
        # 출력이 진행된 경우
        else:
            # 출력 순서 카온터를 증가 시키고
            answer += 1
            # 출력된 건의 location이 지정한 location과 일치하는 경우
            if p_data[0] == location:
                # 출력 순서를 return 한다.
                return answer

