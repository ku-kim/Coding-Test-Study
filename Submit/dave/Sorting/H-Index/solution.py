def solution(citations):
    citations.sort()
    h_idx = 0

    for i, v in enumerate(citations):
        paper_cnt = len(citations) - i
        if h_idx < min(citations[i], paper_cnt):
            h_idx = min(citations[i], paper_cnt)

    return h_idx

