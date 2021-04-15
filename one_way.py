from collections import Counter
def one_way(s1,s2):
    d = Counter(s1)
    for w in s2:
        if w in d:
            d[w] -= 1
        else:
            d[w] = 1
    r = 0
    # return d
    for key,value in d.items():
        r += abs(value)
    return r <=  2
print(one_way('pale','ple'))
print(one_way('pales','pale'))
print(one_way('pale','bale'))
print(one_way('pale','bake'))
print(one_way('balee','bakee'))
