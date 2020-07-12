# 24. 两两交换链表中的节点 swap-nodes-in-pairs


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Here, pre is the previous node.
# Since the head doesn't have a previous node, I just use self instead.
# Again, a is the current node and b is the next node.
# To go from pre -> a -> b -> b.
# next to pre -> b -> a -> b.next, we need to change those three references.
# Instead of thinking about in what order I change them, I just change all three at once.
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next


# for those who don't understand the use of self,
# here is a version with dummy node instead

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode(0)
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return dummy.next


