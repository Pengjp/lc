'''
给定一个字符串的数组strs，请找到一种拼接顺序，使得所有的字符串拼接起来组成的字符串是所有
可能性中字典序最小的，并返回这个字符串。
'''
class Cust(object):
    def __init__(self,val):
        self.val = val
    def __lt__(self, other):
        return self.val + other.val < other.val + self.val

arr = ["b","ba"]
ans = ''.join([i.val for i in sorted([Cust(i) for i in arr])])
print(ans)

from functools import cmp_to_key

def minString(strs):
    strs = sorted(strs,key=cmp_to_key(lambda x,y: -1 if x+y < y+x else 1))
    return ''.join(strs)

s1 = ["abc","de"]
assert(minString(s1)=='abcde')
assert(minString(['b','ba'])=='bab')
