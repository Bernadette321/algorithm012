# https://leetcode-cn.com/problems/two-sum/description/


'''
哈希 O(n)
'''
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] in dict1:
                return [dict1[nums[i]], i]
            else:
                dict1[target - nums[i]] = i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, num in enumerate(nums):
            if d.get(num) == None:
                d[target - num] = index
            else:
                return [d.get(num),index]

# lista = ['a','b']
# for i, x in enumerate(lista):
#     print(i,x)
# # 0 a
# # 1 b