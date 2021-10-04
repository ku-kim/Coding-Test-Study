from collections import defaultdict


def solution(clothes):
    answer = 1
    c_dict = defaultdict(lambda: 1)
    for c in clothes:
        c_dict[c[1]] += 1
    
    for key in c_dict:
        answer *= c_dict[key]
    
    return answer - 1
