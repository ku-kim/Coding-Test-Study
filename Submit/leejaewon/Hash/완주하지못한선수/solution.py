def solution(participant, completion):
    ## 목표: p와 c를 비교하여 완주하지 못한 선수를 리턴한다.
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    else:
        return participant[-1]