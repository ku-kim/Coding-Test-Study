class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        appeared = dict()       # 이미 사용된 문자와 그 인덱스를 저장할 딕셔너리
        max_len = 0      # 최장 길이를 저장할 변수를 선언하고 0으로 초기화
        left = 0            # 현재 부분문자열의 가장 왼쪽 인덱스

        # 문자열의 모든 문자를 인덱스 순으로 순회하면서
        for idx, ch in enumerate(s):
            # 현재 문자가 사용된적이 있고 그 인덱스가 부분 문자열의 가장 왼쪽 인덱스보다 오른쪽에 있는 경우
            if ch in appeared and left <= appeared[ch]:
                # 가장 왼쪽 인덱스를 중복이 발견된 문자의 바로 오른쪽 인덱스로 설정한다.
                left = appeared[ch] + 1
            # 현재 판정중인 문자의 앞쪽 부분 문자열 안에서 중복 문자가 발견되지 않았거나 있더라도 현재 left보다
            # 왼쪽에 있는 경우.
            else:
                # 현재까지의 최장 길이와 left ~ 현재 index 까지의 길이를 비교하여 더 큰 길이를 최장 길이로 한다.
                max_len = max(max_len, idx - left + 1)

            # 현재 문자와 인덱스를 used에 저장한다.
            appeared[ch] = idx

        return max_len

