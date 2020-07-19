# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
递归1 自类似94题(中序)写
'''
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

'''
递归2 自类似94题(中序)写
'''
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(cur):
            if not cur:
                return
            res.append(cur.val)
            dfs(cur.left)
            dfs(cur.right)
        res = []
        dfs(root)
        return res

'''
迭代:栈
'''
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                res.append(cur.val) ##
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return res
