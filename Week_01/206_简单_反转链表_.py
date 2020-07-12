# 反转一个单链表 reverse-linked-list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 双指针迭代iterative
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 申请两个节点, pre和cur, pre指向None
        pre = None
        cur = head
        # 遍历链表
        while cur:
            # 记录当前节点的下一个节点
            tmp = cur.next
            # 然后将当前节点指向pre
            cur.next = pre
            # pre和cur节点都前进一位
            pre, cur = cur, tmp
        return pre
