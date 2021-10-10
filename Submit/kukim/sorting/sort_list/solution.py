"""
	문제    : 정렬, 링크드리스트에서
    유형    : 정렬, 링크드리스트
	난이도  : 중, medium
	시간    : 20m
	uri    : https://leetcode.com/problems/sort-list/
    날짜    : 1o(21.10.10)
"""

from typing import List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        
        tmp.sort()
        answer = tmp_answer = ListNode()
        for value in tmp:
            tmp_answer.next = ListNode(value)
            tmp_answer = tmp_answer.next
        return answer.next