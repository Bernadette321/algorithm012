# https://leetcode-cn.com/problems/permutations/
from typing import List

'''
法1: 回溯

这个问题可以看作有 nn 个排列成一行的空格，我们需要从左往右依此填入题目给定的 nn 个数，每个数只能使用一次。
那么很直接的可以想到一种穷举的算法，即从左往右每一个位置都依此尝试填入一个数，看能不能填完这 n 个空格，
在程序中我们可以用「回溯法」来模拟这个过程。
'''
# https://leetcode-cn.com/problems/permutations/solution/quan-pai-lie-by-leetcode-solution-2/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res


'''
法2: 
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return list(permutations(nums))