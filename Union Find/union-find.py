class UnionFind:
    def __init__(self, points):
        self.fatherMap = {}
        self.rankMap = {}
        for i in points:
            self.fatherMap[i] = i
            self.rankMap[i] = 1

    def findHead(self, ele):
        if ele in self.fatherMap:
            path = []
            while ele != self.fatherMap[ele]:
                path.append(ele)
                ele = self.fatherMap[ele]
            while path:
                self.fatherMap[path.pop()] = ele
            return ele

    def isSameSet(self, a, b):
        if a in self.fatherMap and b in self.fatherMap:
            if self.findHead(a) == self.findHead(b):
                print(a, b, 'are in same set')
            else:
                print(a, b, 'are not in same set')

    def union(self, a, b):
        if a in self.fatherMap and b in self.fatherMap:
            aF = self.findHead(a)
            bF = self.findHead(b)
            # print(a,'father is',aF)
            # print(b,'father is',bF)
            if aF != bF:
                # 把数量小的集合的头拼在数量大的集合
                aRank = self.rankMap[aF]
                bRank = self.rankMap[bF]
                big = aF if aRank >= bRank else bF
                small = aF if big == bF else bF
                self.fatherMap[small] = big
                self.rankMap[big] += self.rankMap[small]
                del self.rankMap[small]

UF = UnionFind(['a', 'b', 'c', 'd', 'e'])
UF.isSameSet('a', 'b')
UF.union('a','b')
print(UF.rankMap)
UF.isSameSet('a', 'b')
UF.union('b','c')
UF.isSameSet('a', 'b')
UF.isSameSet('a', 'c')
UF.isSameSet('c', 'b')
UF.union('d','e')
UF.isSameSet('a', 'd')
UF.union('d','b')
UF.isSameSet('a', 'd')
print(UF.rankMap)
