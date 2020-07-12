# 移动零
from typing import List


# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         j = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[j] = nums[i]
#                 if i != j:
#                     nums[i] = 0
#                 j += 1
# [1,2,0,8,9] 存在问题: 1自我交换,2自我交换
                
'''        
j=0,i=0 [0,1,0,3,12], 
j=0,i=1 [1,0,0,3,12],
j=1,i=2 [1,0,0,3,12],
j=1,i=3 [1,3,0,0,12],
j=2,i=4 [1,3,12,0,0],
'''       
     


# 1. 时间O(n), 空间O(1)
# 两次遍历
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 第一次遍历的时候,j指针记录非零的个数,只要是非零的统统都赋给nums[j]
        j = 0 # j始终记录下一个非0元素要放的位置
        for i in range(len(nums)):
            if nums[i]:
                nums[j] = nums[i]
                j += 1
        # 非0元素统计完了,剩下的都是0了
        # 所以第二次遍历把末尾的元素都赋为0即可
        for i in range(j,len(nums)):
            nums[i] = 0


#2. 一次遍历
# 这里参考了快速排序的思想，快速排序首先要确定一个待分割的元素做中间点x，然后把所有小于等于x的元素放到x的左边，大于x的元素放到其右边。
# 这里我们可以用0当做这个中间点，把不等于0(注意题目没说不能有负数)的放到中间点的左边，等于0的放到其右边。
# 这的中间点就是0本身，所以实现起来比快速排序简单很多，我们使用两个指针i和j，只要nums[i]!=0，我们就交换nums[i]和nums[j]

# 优化前 (图) 
# 帮助理解优化代码,此代码不记忆
#class Solution:
#    def moveZeroes(self, nums: List[int]) -> None:
#        """
#        Do not return anything, modify nums in-place instead.
#        """
#        # 两个指针 i 和 j
#        j = 0
#        for i in range(len(nums)):
#            if nums[i]:
#                nums[j],nums[i] = nums[i],nums[j]
#                j += 1
# j=0,i=0 [1,1,0,3,12] 交换
# j=1,i=1 [1,1,0,3,12] 交换
# j=2,i=2 [1,1,0,3,12]
# j=2,i=3 [1,1,3,0,12] 交换
# j=3,i=4 [1,1,3,12,0] 交换

##### 2:
# 优化:
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i > j: # 优化
                    nums[j],nums[i] = nums[i],0
                j += 1
# 其实优化的地方就是: 它避免了数组开头是非零元素的交换也就是阻止（i==j）时交换。
# 当i > j 时，只需要把 i 的值赋值给j 并把原位置的值置0。同时这里也把交换操作换成了赋值操作，减少了一条操作语句，理论上能更节省时间。

# 3
### * count 0
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count=nums.count(0)
        nums[:]=[i for i in nums if i != 0]
        nums+=[0]*count


