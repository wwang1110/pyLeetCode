class Solution(object):
    def reverseBetween(self, head, m, n):
        def revert(p, r):
            if r != p:
                revert(p.next, r).next = p
            return p
        h = ListNode(0)
        h.next = head

        p = h
        for i in range(n):
           p = p.next 
        r1 = p
        r2 = r1.next

        p = h
        for i in range(m-1):
            p = p.next
        l1 = p
        l2 = l1.next

        revert(l2, r1)
        l1.next = r1
        l2.next = r2
        return h.next


