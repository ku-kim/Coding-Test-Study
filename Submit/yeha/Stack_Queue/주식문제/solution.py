
# 3
def solution(prices):
    length = len(prices)

    # answer를 가질 수 있는 최대값으로 초기화
    answer = [i for i in range(length - 1, -1, -1)]
    print(answer)
    # 주식 가격이 떨어질 경우 찾기
    stack = [0]
    for i in range(1, length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer


# # 2
# def solution(prices):
#     answer = [0] * len(prices)
#     stack = [0]

#     for i in range(1, len(prices)):
#         if prices[i] < prices[stack[-1]]:
#             for j in stack[::-1]:
#                 if prices[i] < prices[j]:
#                     answer[j] = i - j
#                     stack.remove(j)
#                 else:
#                     break
#         stack.append(i)
#     for i in range(0, len(stack) - 1):
#         answer[stack[i]] = len(prices) - stack[i] - 1
#     return answer

# # 1
# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         count = 0
#         for j in range(i + 1, len(prices)):
#             count += 1
#             if prices[i] > prices[j]:
#                 break
#         answer.append(count)
