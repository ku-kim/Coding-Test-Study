def solution(prices):
    ## 목표: prices의 원소마다 가격이 떨어지지 않은 시간이 얼마나 되나
    ## 1. prices를 순회한다.
    ## 2. 원소의 index를 stack에 추가한다.
    ## 3. 근데, 현재 주가보다 크면 stack에서 계속 pop시킨다.
    ## 4. pop할때마다 현재 주가의 위치에서 pop하는 주가의 시점을 빼서 얼마나 주가가 떨어지지 않았는지 answer에 할당
    ## 5. 1에서 4번을 prices의 길이만큼 반복
    ## 6. stack에 값이 남아있으면 주가가 떨어진적 없었다는 의미이므로, (prices의 길이 - 1) - stack에서 pop한 값
    stack = []
    answer = [0] * len(prices)
    
    for idx, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = idx - j
            
        stack.append(idx)
    
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - j - 1
    
    return answer