class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        temp = list()
        while head:
            temp.append(head.val)
            head = head.next
        temp.sort()
        ans = ListNode(temp.pop(), None)
        while temp:
            ans = ListNode(temp.pop(), ans)
        
