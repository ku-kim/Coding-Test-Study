from collections import defaultdict

def solution(genres, plays):
    ## 목표: 총 재생횟수가 많은 장르부터, 각각의 장르에서 재생횟수가 많응 곡 부터, 재생횟수가 같은 곡이면 고유 번호가 낮은 곡부터 차례를 맞춰 <고유번호>를 리턴한다.
    ## 1. 장르: [(재생횟수, 고유번호)...] 형태로 딕셔너리를 만들고, 재생횟수 기준으로 정렬한다.
    ## 2. 1을 토대로 재생횟수 총합을 나타내는 딕셔너리를 만들어서 정렬한다.
    ## 3. 2번 순서대로 장르를 순회하여 원소를 뽑아 answer에 넣는다.
    
    dic = defaultdict(list)
    sum_of_plays = defaultdict(int)
    answer = []
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        dic[genre].append((play, idx))
        sum_of_plays[genre] += play
    
    arr = [sorted(val, key=lambda x: x[0], reverse=True) for val in dic.values()]
    for idx, key in enumerate(dic):
        dic[key] = arr[idx]
    
    
    for genre, _ in sorted(sum_of_plays.items(), key=lambda x: x[1], reverse=True):
        answer += list(map(lambda x: x[1], dic[genre]))[:2]
    
    return answer