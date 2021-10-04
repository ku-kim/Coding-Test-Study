"""
	문제    : 중복없는가장긴부분문자열
    유형    : 해시테이블
	난이도  : 중
	시간    : 
	uri    : https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
from typing import List
import collections

def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    max_length = start = 0
    for index, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_length = max(max_length, index - start + 1)
        used[char] = index

    return max_length


def lengthOfLongestSubstring(s: str) -> int:
    if not s :
        return 0
    elif len(s) == 1:
        return 1
    answer = []
    for i in range(len(s)):
        sub_set = set()
        tmp = []
        for c in s[i:]:
            print(c)
            if c not in sub_set:
                sub_set.add(c)
                tmp.append(c)
                print("c",c)
            else:
                break
        else:
            answer.append("".join(tmp))
    
    return len(max(answer, key = len))
    
s = "abcabcbb"
s = "au"

print(lengthOfLongestSubstring(s))