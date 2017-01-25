class Solution(object):
    def rotateRight(self, head, k):
        n = 0
        p = head
        tail = head
        while p is not None:
            if p.next is None:
                tail = p
            p = p.next
            n += 1

        if n == 0 or k%n == 0:
            return head

        pre = head
        k = n-k%n-1
        while k > 0:
            pre = pre.next
            k -= 1

        tail.next = head
        head = pre.next
        pre.next = None
        return head
