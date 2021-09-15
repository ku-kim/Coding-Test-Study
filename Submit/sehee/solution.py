class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        left = 0  # 부분문자열의 개수를 셀 수 있게 함
        s_dic = {}

        for right, char in enumerate(s):
            if char in s_dic and left <= s_dic[char]: # 문자열이 s_dic에 존재
                left = s_dic[char] + 1  # 이미 중복된 값의 바로 다움 값을 가리킴
                print("l",left)

            else: # 맨 처음 나온 문자열
                answer = max(answer, right - left + 1) # 길이가 더 긴 문자열 길이 측정
                print("answer", answer)

            s_dic[char] = right # 가장 최신 인덱스로 업데이트(Left 값을 갱신할 때 필요)
            print(s_dic)

        return answer




if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))