from functools import cmp_to_key

def minString(strs):
    strs = sorted(strs,key=cmp_to_key(lambda x,y: -1 if x+y < y+x else 1))
    return ''.join(strs)

s1 = ["abc","de"]

assert(minString(s1)=='abcde')
