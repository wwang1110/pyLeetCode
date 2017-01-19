class Solution(object):
    def removeNthFromEnd(self, head, n):
        x = head
        for i in range(n):
            if x is not None:
                x = x.next
            else:
                return head

        if x is None:
            return head.next

        x = x.next
        y = head
        
        while x is not None:
            x = x.next
            y = y.next

        y.next = y.next.next

        return head

