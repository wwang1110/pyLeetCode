class Solution(object):
    def deleteDuplicates(self, head):
        l = ListNode(0)
        l.next = head
        p = l
        while p is not None and p.next is not None:
            q = p.next
            dup = False
            while q.next is not None and q.val == q.next.val:
                dup = True
                q = q.next
            if dup == True:
                p.next = q.next
            else:
                p = p.next
        return l.next