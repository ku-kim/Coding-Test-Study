"""
	문제    : 베스트앨범
    유형    : 해쉬
	난이도  : 중 lv3
	시간    : 20m
	uri    : https://programmers.co.kr/learn/courses/30/lessons/42579
"""

from collections import defaultdict
import itertools
def solution(genres, plays):
    genres_total_counts = defaultdict(int)
    genres_counts = defaultdict(list)
    
    i = 0
    for genre, play in zip(genres, plays):
        genres_total_counts[genre] += play 
        genres_counts[genre].append([play, i])
        i += 1
    
    answer = []
    for genre in sorted(genres_total_counts.items(),key = lambda x: x[1], reverse = True):
        data = sorted(genres_counts[genre[0]], key = lambda x: x[0], reverse = True)
        
        # for case in data[0:2]:
        #     answer.append(case[1])
        answer.append([case[1] for case in data[0:2]])
    # return answer
    return list(itertools.chain(*answer))