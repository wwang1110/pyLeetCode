class Solution(object):
    def deleteDuplicates(self, head):
        p = head
        while p is not None:
            q = p.next
            while q is not None and q.val == p.val:
                q = q.next
            p.next = q
            if p is not None:
                p = p.next
        return head

