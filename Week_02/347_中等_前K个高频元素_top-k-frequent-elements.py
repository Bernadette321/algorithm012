# https://leetcode-cn.com/problems/top-k-frequent-elements/

'''
法1: 堆

***复杂度分析:
时间复杂度：O(Nlog(k))。
    Counter 方法的复杂度是 O(N)，
    建堆和输出的复杂度是 O(Nlog(k))。
    因此总复杂度为 O(N+Nlog(k))=O(Nlog(k))。
空间复杂度：O(N)，存储哈希表的开销。



k = 1 时问题很简单，线性时间内就可以解决。只需要用哈希表维护元素出现频率，每一步更新最高频元素即可。
当 k > 1 就需要一个能够根据出现频率快速获取元素的数据结构，这就是优先队列。
***步骤:
1. 首先建立一个元素值对应出现频率的哈希表。
    在 Python 中提供一个字典结构用作哈希表, 和在 collections 库中的 Counter 方法去构建我们需要的哈希表。
    这个步骤需要 O(N)O(N) 时间其中 NN 是列表中元素个数
2. 第二步建立堆，
    堆中添加一个元素的复杂度是 O(log(k))，要进行 N 次复杂度是 O(N)。
3. 最后一步是输出结果，复杂度为 O(klog(k))。

***python实现
在 Python 中可以使用 heapq 库中的 nlargest 方法，可以在相同时间内完成，但只需要一行代码解决。
(python的heap queue即priority queue, 背后用heap实现)

*** 注
根据复杂度分析，方法对于小 k 的情况是很优的。
但是如果 k 值很大，我们可以将算法改成删除频率最低的若干个元素。


链接：https://leetcode-cn.com/problems/top-k-frequent-elements/solution/qian-k-ge-gao-pin-yuan-su-by-leetcode/

备注:
(1)
heapq.nlargest(n, iterable, key=None)
从 iterable 所定义的数据集中返回前 n 个最大元素组成的列表。
如果提供了 key 则其应指定一个单参数的函数，用于从 iterable 的每个元素中提取比较键 (例如 key=str.lower)。
等价于: sorted(iterable, key=key, reverse=True)[:n]

(2)
Counter.most_common() uses heapq.nlargest() in it's source code.
'''
import collections
import heapq
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)

        return heapq.nlargest(k, count.keys(), key=count.get)

# nums = [1,1,1,2,2,3]
# k = 2
# count.keys() # dict_keys([1, 2, 3])
# count.get <built-in method get of Counter object at 0x7f77d55b0400>


'''
法2 直接用most_common
O(nlogn)
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i[0] for i in collections.Counter(nums).most_common(k)]


'''
优先队列
法1-1 使用Python特性 代码见第一个


法1-2 维护大小为K的堆 -- O(nlogk) 见下:
    当k比较小时合适!!!!!!!
    下面只从堆的角度考虑,从m个元素中,通过堆选出最大的K个数
    K大小的小根堆; 堆满后,若新加的数大于堆首数,弹出堆首元素 -- 弹出了m-k 个最小的
    注意: 这个是小根堆!!!
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq as hq
        lookup = Counter(nums)
        res = []
        heap = []
        for num, freq in lookup.items():
            # 如果堆满了（k个元素）
            if len(heap) == k:
                # 弹出最小频率的元组
                if heap[0][0] < freq:
                    hq.heapreplace(heap, (freq, num))
            else:
                hq.heappush(heap, (freq, num))
        while heap:
            res.append(hq.heappop(heap)[1])

        return res

# print(heap) # [(2, 2), (3, 1)]

'''
优先队列
法1-3 维护大小为n-k的堆 -- 时间复杂度O(nlog(n-k))
    当K比较大时合适!!!!!!
    当k和n相当时, 用此法
    从m个元素中, 通过堆选出最大的k个数; m-k 大小的堆 ---- 大根堆
    堆满后, 若新加的数小于堆首数, 堆首元素加入结果, 否则新加的数加入结果 ---- 选了K次最大的
    注意: 大根堆!!!
    
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq as hq
        res = []
        heap = []
        lookup = Counter(nums)
        n = len(lookup)
        for num, freq in lookup.items():
            if len(heap) == n-k:
                if heap and -heap[0][0] > freq:
                    res.append(hq.heapreplace(heap, (-freq, num))[1])
                else:
                    res.append(num)
            else:
                hq.heappush(heap, (-freq, num))
        return res















'''
附: 
'''
lista = [1,1,1,2,2,3]
count = collections.Counter(lista)
print(count) # Counter({1: 3, 2: 2, 3: 1})
print(count.items()) # dict_items([(1, 3), (2, 2), (3, 1)])
print(count.most_common(2)) # [(1, 3), (2, 2)]
for i in count.most_common(2):
    print(i[0])
# 1
# 2

for k, v in count.items():
    print(k,v)
# 1 3
# 2 2
# 3 1


