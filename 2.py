class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l3h = None
        flag = 0
        while l1 is not None or l2 is not None:
            num = 0
            if l1 is not None:
                num += l1.val
                l1 = l1.next
            if l2 is not None:
                num += l2.val
                l2 = l2.next
            num = flag + num
            flag = num / 10
            num = num % 10
            if l3h is None:
                l3h = l3 =  ListNode(num)
            else:
                l3.next = ListNode(num)
                l3 = l3.next
        if flag > 0:
            l3.next = ListNode(flag)
        return l3h


