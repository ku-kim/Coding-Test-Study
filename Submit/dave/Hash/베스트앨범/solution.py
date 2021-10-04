def solution(genres, plays):
    ans = []
    # 장르별 총재생 수 딕셔너리 생성
    play_total_cnt_by_genre = dict()
    genres_set = set(genres)
    for genre in genres_set:
        play_total_cnt_by_genre.setdefault(genre, 0)

    for i in range(len(genres)):
        play_total_cnt_by_genre[genres[i]] += plays[i]

    play_cnt_list_by_genre = dict()
    for key in play_total_cnt_by_genre:
        play_cnt_list_by_genre.setdefault(play_total_cnt_by_genre[key], [])

    for elem in zip(genres, plays):
        key = play_total_cnt_by_genre[elem[0]]
        play_cnt_list_by_genre[key].append(elem[1])

    idxes_by_play_count = dict()
    for i in range(len(plays)):
        if plays[i] not in idxes_by_play_count:
            idxes_by_play_count.setdefault(plays[i], [i])
        else:
            idxes_by_play_count[plays[i]].append(i)
    sorted_genres = sorted(play_cnt_list_by_genre, reverse=True)
    for key in sorted_genres:
        # 장르별 최대 두 곡까지 출력
        max_len = 2
        if len(play_cnt_list_by_genre[key]) < 2:
            max_len = len(play_cnt_list_by_genre[key])
        # 장르별 곡을 재생 수 내림 차순 정렬
        play_cnt_list_by_genre[key].sort(reverse=True)
        # print(play_cnt_list_by_genre[key])
        # print(idxes_by_play_count[play_cnt_list_by_genre[key][0]])
        for play_cnt in play_cnt_list_by_genre[key]:
            # print(play_cnt)
            for elem in idxes_by_play_count[play_cnt]:
                ans.append(elem)
                max_len -= 1
            if max_len == 0:
                break

    return ans
