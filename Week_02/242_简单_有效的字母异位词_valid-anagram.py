# https://leetcode-cn.com/problems/valid-anagram/description/
# https://leetcode.com/problems/valid-anagram/

# -cn
'''
法1 排序

时间复杂度：O(nlogn)，

假设 t 是 s 的长度，排序成本 O(nlogn) 和比较两个字符串的成本O(n)。
排序时间占主导地位，总体时间复杂度为 O(nlogn)。
'''
# 通过将 ss 的字母重新排列成 tt 来生成变位词。
# 因此，如果 TT 是 SS 的变位词，对两个字符串进行排序将产生两个相同的字符串。
# 此外，如果 ss 和 tt 的长度不同，tt 不能是 ss 的变位词，我们可以提前返回。


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

## 注:
# python的list.sort, sorted的内部实现机制:Timsort,最坏时间复杂度O(nlogn)
# Timsort是结合了merge sort和insertion sort而得出的排序算法. 该算法找到数据中已经排好序的块-分区，每一个分区叫一个run，然后按规则合并这些run。
# Pyhton自从2.3版以来一直采用Timsort算法排序


'''
法2: 哈希表

时间复杂度O(n).  外面需要一层循环; 访问计数器表是一个固定的时间操作。
空间复杂度O(1)

算法：

1. 为了检查 tt 是否是 ss 的重新排列，我们可以计算两个字符串中每个字母的出现次数并进行比较。
   因为 SS 和 TT 都只包含 A-ZA−Z 的字母，所以一个简单的 26 位计数器表就足够了。
2. 我们需要两个计数器数表进行比较吗？
   实际上不是，
   因为我们可以用一个计数器表计算 ss 字母的频率，用 tt 减少计数器表中的每个字母的计数器，然后检查计数器是否回到零。

'''
# https://leetcode-cn.com/problems/valid-anagram/solution/you-xiao-de-zi-mu-yi-wei-ci-by-leetcode/
# 根据官方java改编
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = [0] * 26
        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1
        for count in counter:
            if count != 0:
                return False
        return True


# 3. 或者我们可以先用计数器表计算 s，然后用 t 减少计数器表中的每个字母的计数器。
#    如果在任何时候计数器低于零，我们知道 tt 包含一个不在 ss 中的额外字母，并立即返回 FALSE。
# 根据官方java改编
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table = [0] * 26
        for item in s:
            table[ord(item) - ord('a')] += 1
        for item in t:
            table[ord(item) - ord('a')] -= 1
            if table[ord(item) - ord('a')] < 0:
                return False
        return True

'''
进阶：
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

解答：
使用哈希表而不是固定大小的计数器。想象一下，分配一个大的数组来适应整个 Unicode 字符范围，这个范围可能超过 100万。
哈希表是一种更通用的解决方案，可以适应任何字符范围。
'''

# ------------
'''
国际站高票代码
https://leetcode.com/problems/valid-anagram/discuss/66499/Python-solutions-(sort-and-dictionary).
'''
## 注: 字典的get()函数 返回指定键的值,如果值不在字典中返回默认值
# dict.get(key,default=None)
# key 要查找的键,  default 如果指定键的值不存在时,返回该默认值
# dict1 = {'age':20,'name':'zhangsan'}
# print(dict1.get('a',0)) # 0
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1, dict2 = {}, {}
        for item in s:
            dict1[item] = dict1.get(item, 0) + 1
        for item in t:
            dict2[item] = dict2.get(item, 0) + 1
        return dict1 == dict2

# 自己写一个字典
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         dict1 = {}
#         for i in range(len(s)):
#             dict1[s[i]] = dict1.get(s[i], 0) + 1
#             dict1[t[i]] = dict1.get(t[i], 0) - 1
#         for x in dict1:
#             if dict1[x] != 0:
#                 return False
#         return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1, dict2 = [0] * 26, [0] * 26
        for item in s:
            dict1[ord(item) - ord('a')] += 1
        for item in t:
            dict2[ord(item) - ord('a')] += 1
        return dict1 == dict2

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# ----
# 比较快的
# 40多ms  打败90%以上
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        import collections
        return collections.Counter(s) == collections.Counter(t)
# 40多ms  打败90%以上
## 注: ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
#      ascii_lowercase -- a string containing all ASCII lowercase letters
import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return all([s.count(c) == t.count(c) for c in string.ascii_lowercase])
















