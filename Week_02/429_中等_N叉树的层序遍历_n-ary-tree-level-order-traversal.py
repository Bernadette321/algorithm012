# https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/

'''
法1: 利用 队列 实现广度优先搜索

时间复杂度：O(n)。n 指的是节点的数量。
空间复杂度：O(n)。

我们要构造一个 sub-lists 列表, 其中每个sub-list 是树中一行的值
行应该按从上到下的顺序排列

因为我们从根节点开始遍历树, 然后向下搜索最接近根节点的节点, 这是广度优先搜索
我们适用队列来进行广度优先搜索, 队列具有先进先出的特性

!!!!!在这里使用栈是错误的选择, 栈应用于深度优先搜索

# 详细图片讲解: https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/solution/ncha-shu-de-ceng-xu-bian-li-by-leetcode/
我们可以看到它从左到右, 并且从上到下顺序遍历节点

下一步: 研究如何在这个算法基础上保存每一层的列表,并且在根节点为空时正常工作

再构造下一层的列表时，我们需要创建新的子列表，然后将该层的所有节点的值插入到列表中。
一个很好的方法时在 while 循环体开始时记录队列的当前大小 size。
然后用另一个循环来处理 size 数量的节点。这样可以保证 while 循环在每一次迭代处理一层。

使用队列十分重要，如果使用 Vector，List，Array 的话，我们删除元素需要 O(n) 的时间复杂度。
而队列删除元素只需要 O(1) 的时间。

'''
import collections
from typing import List
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = collections.deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            result.append(level)
        return result


'''
法2: 简化的广度优先搜索

时间复杂度：O(n)。n 指的是节点的数量。
空间复杂度：O(n)，我们的列表包含所有节点。
'''


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        result = []
        previous_layer = [root]

        while previous_layer:
            current_layer = []
            result.append([])
            for node in previous_layer:
                result[-1].append(node.val)
                current_layer.extend(node.children)
            previous_layer = current_layer
        return result

'''
法3: 递归

我们可以使用递归来解决这个问题，通常我们不能使用递归进行广度优先搜索。
这是因为广度优先搜索基于队列，而递归运行时使用堆栈，适合深度优先搜索。

'''

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def traverse_node(node, level):
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            for child in node.children:
                traverse_node(child, level + 1)

        result = []
        if root is not None:
            traverse_node(root, 0)
        return result

# 链接：https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/solution/ncha-shu-de-ceng-xu-bian-li-by-leetcode/




