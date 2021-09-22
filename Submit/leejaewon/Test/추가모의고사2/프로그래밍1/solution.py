def dfs(land, row, col, answer, case):
    if row  == len(land)-1:
        answer.append(case)
        return answer
    
    cols = [i for i in range(4) if i != col]

    dfs(land, row + 1, cols[0], answer, case + [land[row+1][cols[0]]])
    dfs(land, row + 1, cols[1], answer, case + [land[row+1][cols[1]]])
    dfs(land, row + 1, cols[2], answer, case + [land[row+1][cols[2]]])
    
    
def solution(land):
    ## 목표: 칸을 밟고 얻는 최대 점수를 구하여 리턴 (단, 한 행에서 밟은 열을, 다음 행에서 밟을 수 없다.)
    ## 풀이: DFS
    ## 1. DFS로 경우의 수를 구하고
        ## 1-1. dfs(land, 이동할 열의 위치, 이동할 행의 위치(depth), answer, case)
        ## 1-2. 매개변수로 받은 열 위치를 제외한 나머지 열 위치를 리스트로 뽑는다.
        ## 1-3. case에 land[행][열]을 담는다.
        ## 1-3. dfs로 다음행 이동
        ## 1-4. depth + 1 == len(land)면 answer.append(case)
        
    ## 2. max로 제일 높은 값 추출
    
    answer = []
    
    for i in range(4):
        dfs(land, 0, i, answer, [land[0][i]])
    
    return max(map(sum, answer))