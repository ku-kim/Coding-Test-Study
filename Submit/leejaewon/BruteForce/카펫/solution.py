def solution(brown, yellow):
    ## 목표: brown과 yellow를 합친 카펫의 [가로, 세로]를 리턴
    ## 1. 격자의 전체 개수를 구함
    ## 2. 격자세로의 길이를 최소 3부터 시작
    ## 3. (갈색세로 - 2) * 노란색 가로 == 노란색 개수라면, [전체개수//갈색세로, 갈색세로]를 리턴
    board = brown + yellow

    for col in range(3, board):
        if (col - 2) * (brown - (col * 2)) / 2 == yellow:
            return [board//col, col]