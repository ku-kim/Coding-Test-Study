def solution(prices):
    '''
    stack을 사용한 solution을 요약하면 다음과 같다.
        1. 주가의 하락이 발견되면 현재 인덱스 - 1 부터 현재 주가 이상의 주가가 나올 때까지
           인덱스를 줄여가며 현재 인덱스의 주가 미만의 주가들의 인덱스에 해당하는 유지시간을 확정한다.
        2. 모든 prices 요소를 탐색한 뒤 stack에 남은 데이터를 top에서 부터 하나 씩 pop해가면서
           pieses의 마지막 인덱스로 부터 얼마나 떨어져 있는지를 확인한다. 마지막 인덱스로 부터 떨어진
           거리를 n이라 하면 pop한 인덱스에 해당하는 주가 유지 시간이 n이 된다.
    :param prices:
    :return:
    '''
    answer = [0] * len(prices)
    stack = []

    # 주가 리스트의 원소를 선형탐색 하면서 다음 로직을 실행한다.
    for curr_idx in range(len(prices)):
        try:    # stack이 비었을 경우에 대한 예외처리를 한다.
            # 현재 인덱스의 주가 < 이전 인덱스의 주가 즉, 주가가 하락하면
            # stack에 저장된 이전 주가들을 가르키는 인덱스를 거슬러 올라가면서
            # 현재 주가 이하의 주가가 나올 때까지 혹은 stack이 비워질 때까지
            # 다음을 실행한다.
            while prices[curr_idx] < prices[stack[-1]]:
                # 이전 주가 인덱스를 stack에서 꺼내고
                prev_idx = stack.pop()
                # 현재 주가 인덱스 - 이전 주가 인덱스 의 결과가 이전 주가가 유지된 시간 이 되므로
                # 결괏값 리스트의 prev_idx에 해당하는 요소에 curr_idx - prev_idx 값을 넣어준다.
                answer[prev_idx] = curr_idx - prev_idx
                # 이 while문이 반복됨에 따라 현재 주가 인덱스에서 1초씩 멀어진다. 따라서 주가 유지 시간이 길어지게 된다.
        except IndexError:
            pass
        # 현재 주가 인덱스를 stack에 push한다.
        stack.append(curr_idx)

    # 이제 stack에 남아 있는 정보를 하나씩 꺼내면서 그 인덱스가 마지막 인덱스로부터 얼마나 떨어져 있는지를 계산하여
    # 결괏값 리스트의 요소 가운데 꺼낸 인덱스에 해당하는 요소의 값으로 update 해준다.
    while stack:
        prev_idx = stack.pop()
        answer[prev_idx] = len(prices) - 1 - prev_idx

    return answer

