# 爬楼梯
'''
# 找 最近 重复子问题

# 懵逼的时候:
# 1.暴力? 
# 2.基本情况? ->

# 泛化的思路:找 最近 重复子问题

if else, 
for while,recursion(递归) :重复

1. n=1: 1
2. n=2: 2
3. n=3: 不要人肉遍历了 f(1)+f(2)
4. n=4: f(2)+f(3)
(递推,数学归纳法)
f(n)=f(n-1)+f(n-2) :Fibonacci
'''
# 法1 O(n) 动态规划
# f(n)=f(n-1)+f(n-2) 动态规划的转移方程
#  'a' represents (n-2) and 'b' represents the (n-1)
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a
'''
1, 1, 2, 3, 5
a  b
   a  b
      a  b
         a  b
            a  b
return a
'''


#### 法3.数学公式 时间复杂度：O(logn)，pow 方法将会用去 O(logn) 的时间。

class Solution:
    def climbStairs(self, n: int) -> int:
        return int((5**.5 / 5) * (((1 + 5**.5)/2)**(n + 1) - ((1 - 5**.5)/2)**(n + 1)))


