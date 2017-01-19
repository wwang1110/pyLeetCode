class Solution(object):
    def swapPairs(self, head):
        def swap(head):
            if head is None or head.next is None:
                return head
            q = swap(head.next.next)
            p = head.next
            head.next = q
            p.next = head
            return p
        return swap(head)
