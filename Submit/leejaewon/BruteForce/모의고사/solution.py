def solution(answers):
    supoja1 = [1, 2, 3, 4, 5] * (int(len(answers) / 5) + 1)
    supoja2 = [2, 1, 2, 3, 2, 4, 2, 5] * (int(len(answers) / 8) + 1)
    supoja3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (int(len(answers) / 10) + 1)
    
    result = []
    
    for i, arr in enumerate([supoja1, supoja2, supoja3]):
        count = 0
        for a, b in zip(answers, arr):
            if a == b:
                count += 1
        result.append(count)
    
    answer = []
    for i, cnt in enumerate(result):
        if cnt == max(result):
            answer.append(i+1)
    
    return answer