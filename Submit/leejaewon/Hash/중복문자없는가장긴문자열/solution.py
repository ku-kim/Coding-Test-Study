def lengthOfLongestSubstring(s):
        ## 목표: 같은 문자가 없는 부분 문자열중에 가장 긴 문자열의 길이를 리턴해라
        ## 0.  used 딕셔너리, max_len, start = 0으로 할당
        ## 1. idx, char 형태로 s를 순회
        ## 2. used에 char가 있되, 현재 idx위치에 있는 문자가 start 앞쪽에 있는 문자인지 확인
            ## 2-1. 있으면, start = used[char] + 1
            ## 2-2. 없으면, max_len = max(max_len, (idx+1) - start)
        ## 3. char: idx 형태로 used에 할당
        ## 4. 1부터 3까지 반복
        
        used = dict()
        max_len = start = 0
        
        for idx, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_len = max(max_len, (idx+1) - start)
                
            used[char] = idx
                
        return max_len