def solution(citations):
    citations.sort()

    for i in range(len(citations)):
        answer = len(citations) - i
        if citations[i] >= answer:
            return answer
    return 0