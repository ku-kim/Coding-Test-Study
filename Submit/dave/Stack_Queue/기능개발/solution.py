from math import ceil


def solution(progresses, speeds):
    answer = []
    stack = []
    for i in range(len(progresses) - 1, -1, -1):
        stack.append(ceil((100 - progresses[i]) / speeds[i]))

    while stack:
        top = stack[-1]
        count = 0
        for i in range(len(stack) - 1, -1, -1):
            if stack[i] <= top:
                count += 1
                stack.pop()
            else:
                break
        answer.append(count)
    return answer

