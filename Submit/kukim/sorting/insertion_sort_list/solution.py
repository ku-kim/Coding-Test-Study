"""
	문제    : 삽입정렬, 링크드리스트에서
    유형    : 정렬, 링크드리스트
	난이도  : 중, medium
	시간    : 20m
	uri    : https://leetcode.com/problems/insertion-sort-list/
    날짜    : 1x(21.10.10)
"""

'''
    1. 삽입 결과를 저장할 노드 생성
    2. 입력된 노드 데이터를 반복하며 결과 노드에 적절한 위치에 삽입
    3. 2번 단계 반복 종료 되면 정렬된 노드 확인 가능
    
    e.g.
    input = [4,3,5] 와 result = []
        1. 입려된 노드 중 첫 번째 4가 result = [4]에 들어감
        2. 두번째 요소 3이 마찬가지로 result의 값과 비교하여 데이터 삽입
            result = [3,4]
        3. 마지막 요소 5가 result 순회하며 마지막에 삽입 
'''

from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def print(self):
        node = self
        while node:
            print(node.val)
            node = node.next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode() # 결과 노드 생성
        curr = head # curr에 현재 위치 저장
        
        while curr:
            prev = answer
            while prev.next and prev.next.val < curr.val: # 결과 값이 현재 값보다 작을 때 까지 순회
                prev = prev.next
            
            next = curr.next
            curr.next = prev.next # curr.next 값을 결과에 저장하기 위해 None 값을 넣어 연결 끊기
            prev.next = curr # prev.next에 값 넣기

            curr = next
        return answer.next

head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
answer = Solution()
answer.insertionSortList(head).print()

#print(head.val)