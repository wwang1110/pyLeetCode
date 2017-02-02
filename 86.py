class Solution(object):
    def partition(self, head, x):
        left = ListNode(0)
        l = left
        right = ListNode(0)
        r = right
        p = head
        while p is not None:
            if p.val < x:
                l.next = p
                l = l.next
            else:
                r.next = p
                r = r.next
            p = p.next
        l.next = right.next
        r.next = None
        return left.next

