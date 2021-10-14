class Solution:
        def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            vals = []
            p = head
            while p:
                vals.append(p.val)
                p = p.next
            vals.sort()
            i = 0
            p = head
            while p:
                p.val = vals[i]
                p = p.next
                i += 1
            return head
