# 盛最多水的容器


# 左右夹逼:O(n),左右边界 i,j,向中间收敛.   双指针法
# 求出当前双指针对应的容器的容量；
# 对应数字较小的那个指针以后不可能作为容器的边界了，将其丢弃，并移动对应的指针。

# 最后的答案是什么？
#答案就是我们每次以双指针为左右边界（也就是「数组」的左右边界）计算出的容量中的最大值。
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l],height[r]) * (r - l)
            ans = max(ans,area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans


