class Solution(object):
    def mergeTwoLists(self, l1, l2):
        l3 = p = ListNode(0)
        i = l1
        j = l2

        while i is not None or j is not None:
            if i is not None and j is not None:
                if i.val < j.val:
                    p.next = i
                    i = i.next
                else:
                    p.next = j
                    j = j.next
            elif i is not None and j is None:
                p.next = i
                i = i.next
            elif i is None and j is not None:
                p.next = j
                j = j.next
            p = p.next

        return l3.next
