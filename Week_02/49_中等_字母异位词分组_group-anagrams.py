# https://leetcode-cn.com/problems/group-anagrams/


# https://leetcode-cn.com/problems/group-anagrams/solution/zi-mu-yi-wei-ci-fen-zu-by-leetcode/
# class collections.defaultdict([default_factory[, ...]])
'''
法1: 排序数组分类
复杂度: 时间复杂度 O(NKlogK) N是str的长度,而K是strs中字符串的最大长度,当我们遍历每个字符串时,
        外部循环具有的复杂度为O(N). 然后, 我们在O(KlogK)的时间内对每个字符串排序
      空间复杂度 O(NK) ,排序存储在ans中的全部信息内容

思路: 当且仅当它们的排序字符串相等时, 两个字符串是字母异位词
算法: 将键存储为散列化元组
有一点要注意：因为字典的键，必须是不可变类型，所以用tuple。
    strs = ["are", "bat", "ear", "code", "tab", "era"]
    ans = {('a','e','r'):["are","ear","era"],
           ('a','b','t'):["bat","tab"],
           ('e','c','d','o'):["code"]}
'''
import collections
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())

# dict1 = {1:"are",2:"bat",3:"code"}
# print(dict1.values()) # dict_values(['are', 'bat', 'code'])
# print(list(dict1.values())) # ['are', 'bat', 'code']
# print(dict1.items()) # dict_items([(1, 'are'), (2, 'bat'), (3, 'code')])
# print(dict1.keys()) # dict_keys([1, 2, 3])


'''
法2: 按计数分类

复杂度: 时间O(NK)  其中N是strs的长度,而K是strs中字符串的最大长度
        空间O(NK)

思路: 当且仅当它们的字符计数(每个字符的出现次数)相同时, 两个字符串是字母异位词

算法: 我们可以将每个字符串s转换为字符数count, 由26个非负整数组成, 表示a, b, c的数量等,
    我们使用这些计数作为哈希映射的基础
    在python中,表示将是一个计数的元组,例如abbcc将表示为(1,2,3,0,0,...,0),其中总共有26个条目
    ans = {(2,1,0,0,...,0):["aab","aba","baa"],
           (1,2,3,0,0,...,0):["abbccc"]} 
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())

# ----------------------------

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for item in strs:
            key = tuple(sorted(item))
            dict1[key] = dict1.get(key,[]) + [item]
        return list(dict1.values())












