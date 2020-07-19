# 脑图

两种

数据结构和算法脑图,  

最优题解和思路脑图

# 数据结构与算法总览

### 切题四件套 (个体)

```
1. Clarification: 
自己多看题目/ 和面试官反复沟通一下这个题目, 确保自己对题目的理解是正确的

2. Possible solutions(复数): 
所有可能的解法都过一遍, 比较不同解法的时空复杂度, 
从中找出最优的解法(一般就是时间最快的一种)

3. Coding(多写)

4. Test cases 测试样例列举几个(面试时候也测试)
```

### 五毒神掌







# 预习-- 时间复杂度和空间复杂度分析

### 主定理 -- 四种情形

+ 一维的数组进行二分查找 
+ 二叉树的遍历: 
简化的思考方式-- 不管是前序中序后序, 它遍历二叉树的时候, 每一个节点都访问一次,且仅访问一次
所以它的时间复杂度就是线性于二叉树的节点总数, O(n)
n 代表二叉树里面的树的节点总数
+ 在排好序的二维矩阵中进行二分查找
+ 归并排序

### 思考题中
+ 二叉树遍历:
```
简化的思考方式-- 不管是前序中序后序, 它遍历二叉树的时候, 每一个节点都访问一次,且仅访问一次
所以它的时间复杂度就是线性于二叉树的节点总数, O(n)
n 代表二叉树里面的树的节点总数
```
+ 图
```
图中每一个节点都访问一次,且仅访问一次,O(n)
n 代表图里面的节点总数
```
+ 搜索算法
```
DFS深度优先,BFS广度优先 时间复杂度是多少
不管是哪一个, 因为访问的节点是访问一次,
O(n)
n: 搜索空间里面的节点总数
```

# 第1周

## 第3课 数组,链表,跳表

#### 1.基本实现和特性

跳表:

一维的数据结构要加速的话 , 经常采用的方式就是升维也就是说变成二维 . 因为多个一个维度之后 , 就会有多一级的信息在里面, 这样多一级的信息就帮助我们可以很快地得到一维里面你必须挨个走才能走到的那些元素

小结中:

对于时间复杂度,尤其是数组和链表,它们的增加删除访问的时间复杂度, 一定要非常清晰,**在面试的时候经常会问**. 不同的面试题, 考察用哪一种数据结构是否考虑的得当

#### 2.实战 - 移动零

```java
//1. loop, count zeros,
//2. 开新数组, loop
//3. index ->

// java 0ms
class Solution {
    public void moveZeroes(int[] nums) {
        int j = 0; // j始终记录下一个非0元素要放的位置
        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] != 0) {
            	nums[j] = nums[i];
                if (i != j) {
                    nums[i] = 0;
                }
                j ++;
            }
        }
    }
}
// 50% , feedback
```



#### 3.实战 - 盛水最多的容器

```java
//一维数组的坐标变换 i,j

//1. 枚举: left bar x, right bar y, (x-y)*minHeight
//	O(n^2)
//2. 左右夹逼:O(n),左右边界 i,j,向中间收敛

// O(n^2)
class Solution {
    public int maxArea(int[] height) {
        int max = 0;
        for (int i = 0; i < height.length - 1; ++i) {
            for (int j = i + 1; j < height.length; ++j) {
            	int area = (j - i) * Math.min(height[i],height[j]);
                max = Math.max(max,area);
            }
        }
        return max;
    }
}

// O(n)
class Solution {
    public int maxArea(int[] height) {
    	int max = 0;
        for(int i = 0, j = height.length - 1; i < j ; ){
			int minHeight = height[i] < height[j] ? height[i ++] : height[j --];
			max = Math.max(max,(j - i + 1) * minHeight);
        }
        return max;
    }
}

class Solution {
    public int maxArea(int[] height) {
    	int max = 0;
        for(int i = 0, j = height.length - 1; i < j ; ){
            int minHeight = height[i] < height[j] ? height[i ++] : height[j --];
            int area = (j - i + 1) * minHeight;
            max = Math.max(max,area);
        }
        return max;
    }
}

```

#### 4.爬楼梯

**找 最近 重复子问题**

```python
# 懵逼的时候:
# 1.暴力? 
# 2.基本情况?->

# 泛化的思路:找 最近 重复子问题

if else, 
for while,recursion(递归) :重复

1. n=1: 1
2. n=2: 2
3. n=3: 不要人肉遍历了 f(1)+f(2)
4. n=4: f(2)+f(3)
(递推,数学归纳法)
f(n)=f(n-1)+f(n-2) :Fibonacci

# 可以不用数组,就保存它的最近的三个值
class Solution:
    def climbStairs(self, n: int) -> int:
        if (n <= 2): 
            return n
        f1, f2, f3 = 1, 2, 3
        for i in range(3,n+1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3
```



优化思想: 升维,一维升二维; 空间换时间

### 总结思路:找重复性

#### 5.3数之和

##### 简单版: 两数之和



```java
// a + b + c = 0
// a + b = -c (target)
// 1. 暴力求解: 三重循环
```





#### 6.Linked List

解法非常固定,主要是孰能生巧

面试前再写一遍Linked List

##### 特殊: 环形链表 

有些思维上的巧妙性

```java
// 1. 暴力法 遍历链表  hash/set
// 2. 快慢指针 有些思维上的巧妙性
```



## 第四课 栈, 队列, 双端队列, 优先队列

#### 1.栈和队列的实现与特性

+ stack栈: FILO,  添加删除O(1), 查询为O(n)

+ queue队列: 先来先出, 添加删除O(1), 查询为O(n)

+ 双端队列Deque: Double-End Queue:

​		(一个queue和stack的结合体)

​		添加删除O(1), 查询为O(n)



priority queue复杂度分析:一般来说,它的实现是Binary Search Tree那一行



python  heap queue 即priority queue, 背后用heap实现

高性能的container库: 这个库里面有所有高级的容器应该怎么用



-------------------------

##### python

deque对象 

https://docs.python.org/zh-cn/3/library/collections.html#collections.deque

```python
class collections.deque([iterable[, maxlen]])

append(x)
添加 x 到右端。

appendleft(x)
添加 x 到左端。

clear()
移除所有元素，使其长度为0.

copy()
创建一份浅拷贝。

count(x)
计算 deque 中元素等于 x 的个数。

extend(iterable)
扩展deque的右侧，通过添加iterable参数中的元素。

extendleft(iterable)
扩展deque的左侧，通过添加iterable参数中的元素。注意，左添加时，在结果中iterable参数中的顺序将被反过来添加。

index(x[, start[, stop]])
返回 x 在 deque 中的位置（在索引 start 之后，索引 stop 之前）。 返回第一个匹配项，如果未找到则引发 ValueError。

insert(i, x)
在位置 i 插入 x 。
如果插入会导致一个限长 deque 超出长度 maxlen 的话，就引发一个 IndexError。

pop()
移去并且返回一个元素，deque 最右侧的那一个。 如果没有元素的话，就引发一个 IndexError。

popleft()
移去并且返回一个元素，deque 最左侧的那一个。 如果没有元素的话，就引发 IndexError。

remove(value)
移除找到的第一个 value。 如果没有的话就引发 ValueError。

reverse()
将deque逆序排列。返回 None 。

rotate(n=1)
向右循环移动 n 步。 如果 n 是负数，就向左循环。
如果deque不是空的，向右循环移动一步就等价于 d.appendleft(d.pop()) ， 向左循环一步就等价于 d.append(d.popleft()) 。

Deque对象同样提供了一个只读属性:
maxlen
Deque的最大尺寸，如果没有限定的话就是 None 。

除了以上操作，deque 还支持迭代、封存、len(d)、reversed(d)、copy.copy(d)、copy.deepcopy(d)、成员检测运算符 in 以及下标引用例如通过 d[0] 访问首个元素等。 索引访问在两端的复杂度均为 O(1) 但在中间则会低至 O(n)。 如需快速随机访问，请改用列表。
Deque从版本3.5开始支持 __add__(), __mul__(), 和 __imul__() 。
```

示例

```python
>>> from collections import deque
>>> d = deque('ghi')                 # make a new deque with three items
>>> for elem in d:                   # iterate over the deque's elements
...     print(elem.upper())
G
H
I

>>> d.append('j')                    # add a new entry to the right side
>>> d.appendleft('f')                # add a new entry to the left side
>>> d                                # show the representation of the deque
deque(['f', 'g', 'h', 'i', 'j'])

>>> d.pop()                          # return and remove the rightmost item
'j'
>>> d.popleft()                      # return and remove the leftmost item
'f'
>>> list(d)                          # list the contents of the deque
['g', 'h', 'i']
>>> d[0]                             # peek at leftmost item
'g'
>>> d[-1]                            # peek at rightmost item
'i'

>>> list(reversed(d))                # list the contents of a deque in reverse
['i', 'h', 'g']
>>> 'h' in d                         # search the deque
True
>>> d.extend('jkl')                  # add multiple elements at once
>>> d
deque(['g', 'h', 'i', 'j', 'k', 'l'])
>>> d.rotate(1)                      # right rotation
>>> d
deque(['l', 'g', 'h', 'i', 'j', 'k'])
>>> d.rotate(-1)                     # left rotation
>>> d
deque(['g', 'h', 'i', 'j', 'k', 'l'])

>>> deque(reversed(d))               # make a new deque in reverse order
deque(['l', 'k', 'j', 'i', 'h', 'g'])
>>> d.clear()                        # empty the deque
>>> d.pop()                          # cannot pop from an empty deque
Traceback (most recent call last):
    File "<pyshell#6>", line 1, in -toplevel-
        d.pop()
IndexError: pop from an empty deque

>>> d.extendleft('abc')              # extendleft() reverses the input order
>>> d
deque(['c', 'b', 'a'])
```

#### 2.实战 - 有效的括号

+ 为什么这个题目可以用栈来解决
+ 什么样的题目可以用栈来解决

如果一个东西具有所谓的**最近相关性**的话,用**栈**解决

现实中看什么情况用栈这种逻辑来解决
(鸟:飞机的发明    
洋葱->反映到工程中,从外向内或从内向外逐渐扩散, 最外层和最外层是一对,最内层和最内层是一对->最近相关性->栈)

先来后到->队列

```java
// 1. 暴力:O(n^2) 不断replace匹配的括号 ->""
// a. ()[]{}
// b. ((({[]}))) -> ((({}))) -> ((())) -> (()) -> () -> 空 -> True

// 2. stack
// 如果是左括号就压到栈里去, 
// 如果是右括号就和栈顶元素进行匹配
// 匹配的上的话,就是正负抵消了,把栈顶元素移出栈
// 不然的话就是不合法
// 一直如此操作
// 直到最后整个栈为空,就说明完全匹配了

```

#### 3.最小栈

面试: 

只用栈实现队列: 用两个栈

用队列实现栈: 用两个队列

#### 4.柱状图中最大的矩形

```python
# 暴力1 O(n^3)  
for i -> 0,n-2
	for j -> i+1, n-1
    	(i,j) -> 最小高度(一层循环) , area
        update max-area
# 暴力2 暴力法的加速
不用枚举左边界, 只要枚举它的棒子的高度
for i -> 0,n-1 以i这根棒子作为它的高度
	找到 left bound, right bound
    area = height[i] * (right - left)
    update max-area

# 栈stack O(n)
# 维护一个栈, 里面的元素是从小到大来进行排列的 ,因为这样的话就可以有效地知道它的左边界在什么地方
# 从小到大指的是从栈底到栈顶去
# 如何从小到大: 就是在入栈的时候要进行一些处理
# 每次入栈,都检查和栈顶元素比,是否大于栈顶元素,如果大于栈顶元素就放入栈,不然的话就要进行一些出栈操作了
```

### 要滚瓜烂熟的i, j: 

```
i,j不断往左右两边扩散
i,j往中间推近,最后相遇
i,j写两个嵌套的循环枚举所有i,j的情况

```

#### 5.滑动窗口最大值

sliding window的题目: 用一个队列去处理, 双端队列

```python
# 1. 暴力 O(n^k)

# 2.deque O(n)  "单调队列"

class Solution:
    def maxSlidingWindow(self,nums: List[int], k: int) -> List[int]:
        res = []
        if nums != []:
            tmp_max = max(nums[0:k])
            for i in range(len(nums)-(k-1)):
                tmp_max = max(nums[i:i+k])
                res.append(tmp_max)
        return res
            
            
```



# 第2周

## 第5课 哈希表,映射,集合

### 哈希表

```
对于不同的要存储的数据,它经过哈希函数之后,会得到一个相同的值:  哈希碰撞
工程上常用的方式:再增加一个维度,这个位置存多个数.也就是从这里开始拉出来一个链表: 拉链式解决冲突法

O(1) 可以查询到它的位置, 但是如果很多的元素都积累在相同的位置,这时候它的查询时间就要遍历链表, 所以如果链表很长的话,它就会效率进行退化,退化到所谓的O(n)的级别,
但是如果设计的比较好的话,哈希函数它的碰撞的概率很小

所以在平均时刻的话,我们可以认为,整个哈希函数的查询它是O(1)
```

从哈希表抽象而来: map, set, 对应于python的话就是dict,set

时间复杂度分析部分, 如果是TreeMap或者叫TreeSet的话,看Red-Black Tree那一行. 这些高级语言他们的TreeMap和TreeSet都是使用红黑树来实现的,它是严格平衡的红黑树,在所有的操作里的话都是O(logn)的时间复杂度来实现的.



### 实战

##### 1.有效的字母异位词

```
1. 暴力, sort ,  sorted_str 相等? O(nlogn)
2. hash, map --> 统计每个字符的频次
```

##### 2.加强版:  49-字母异位词分组

```

```

##### 3.1-两数之和

```
哈希表法O(n)
a,b --> a+b==target -->
for each a:
	check (target - a) exists in nums[哈希表的运用将这一层的复杂度变为O(1)]
	

```

## 第6课 树,二叉树,二叉搜索树

如果要加速:升维, 常见的二维:树,图

图和树最关键的一个差别是: 看有没有环

### 二叉树

```
二叉树的儿子节点只有两个:左儿子,右儿子
```

##### 示例代码

```python
class TreeNode: 
    def __init__(self, val): 
        self.val = val 
        self.left, self.right = None, None
```

##### 遍历: 基于递归    

```
1. 前序pre-order: 根-左-右
2. 中序in-order: 左-根-右
3. 后序post-order: 左-右-根

```

##### 示例代码

```python
def preorder(self, root): 
    if root: 
        self.traverse_path.append(root.val) 
        self.preorder(root.left) 
        self.preorder(root.right)
        
def inorder(self, root):
    if root: 
        self.inorder(root.left) 
        self.traverse_path.append(root.val) 
        self.inorder(root.right)
        
def postorder(self, root):
    if root: 
        self.postorder(root.left) 
        self.postorder(root.right) 
        self.traverse_path.append(root.val)
    
```



基于递归的原因:

```
树的定义本身的话,它没法有效地进行所谓的循环,
后面会讲到,也可以强行循环,比如用广度优先遍历,但是很多情况下,你会发现它的这种结构的话,写循环相对比较麻烦, 而写递归调用相对比较简单
```

完全无序时候, 查询只能遍历,O(n)





### 二叉搜索树Binary Search Tree

##### 易错点: 

一棵空树也是二叉搜索树,
**"所有节点"(PPT)  错误方法: 写代码只比较左儿子和右儿子**

![image-20200715232559333](https://i.loli.net/2020/07/15/ZrKBNShD1RjIxet.png)

重复性

中序遍历: 升序遍历

----



如果删的不是叶子节点: 需要拉一个垫背的-->一般来说,选它右子树里面最小的节点



### 实战

树的面试题解法一般都是递归的

```
第5题:广度优先遍历,后面有更详细的讲解
```

# 第6课 堆和二叉堆,图

### 实战

##### 40最小的K个数

```
1. sort: O(nlogn)
2. heap: 每次加进入O(nlogk)
3. quick-sort

```

##### 滑动窗口

```
1. 双端队列
2. 堆
```

##### 前K个高频元素

```
logn --> 二叉堆, 二叉搜索树, 二分查找, 排序...

步骤1 统计频次(用哈希表) O(n)
步骤2 排序频次, 大顶堆
步骤3 筛出前K个,result
```





