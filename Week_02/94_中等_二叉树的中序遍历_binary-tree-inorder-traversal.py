# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
法1: 递归
时间复杂度: O(n), n为节点数, 访问每个节点恰好一次


递归遍历:
+ 前序遍历: 打印-左-右
+ 中序遍历: 左-打印-右
+ 后序遍历: 左-右-打印

+ 中止条件: 当前节点为空时
+ 函数内: 递归的调用左节点, 打印当前节点, 再递归调用右节点



递归1: 二叉树遍历最易理解和实现版本
'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # 中序递归
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

'''
递归2: 递归2: 通用模板,可以适用不同的题目,添加参数,增加返回条件,修改进入递归条件,自定义返回值

时间复杂度:O(n)
空间复杂度:O(h)，h是树的高度
'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(cur):
            if not cur:
                return
            # 中序递归
            # 按照 左 - 打印 - 右 的方式遍历
            dfs(cur.left)
            res.append(cur.val)
            dfs(cur.right)
        res = []
        dfs(root)
        return res


'''
迭代: 栈
时间复杂度:O(n)
空间复杂度:O(h)，h是树的高度


递归实现时，是函数自己调用自己，一层层的嵌套下去，
操作系统/虚拟机自动帮我们用**栈**来保存了每个调用的函数，
现在我们需要自己模拟这样的调用过程。
递归的调用过程是不断往左边走，当左边走不下去了，就打印节点，并转向右边，然后右边继续这个过程。
我们在迭代实现时，就可以用栈来模拟上面的调用过程。

'''
# 模板
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root
        # 中序，模板：先用指针找到每颗子树的最左下角，然后进行进出栈操作
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res



# 参考链接: https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/dong-hua-yan-shi-94-er-cha-shu-de-zhong-xu-bian-li/
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while stack or root:
            # 不断往左子树方向走，每走一次就将当前节点保存到栈中
            # 这是模拟递归的调用
            if root:
                stack.append(root)
                root = root.left
            # 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
            # 然后转向右边节点，继续上面整个过程
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res

