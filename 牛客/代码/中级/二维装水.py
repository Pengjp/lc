'''
有一个二维数字表示地形，计算装水量，对角线不考虑

边框先进minheap，
while minheap not empty：
    pop 堆上面 的ele
    更新cur_max
    让ele周围的位置入heap如果之前没有加过
    对于每一个新ele，计算水量max(0, ele-cur_max)
'''
import heapq
# def trapRainWater(heightMap):
#     N = len(heightMap)
#     M = len(heightMap[0])
#     isEnter = set() # 记录位置
#     heap = []
#     # 加入周围
#     for col in range(M-1):
#         isEnter.add((0,col))
#         heapq.heappush(heap, heightMap[0][col])
#     for row in range(N-1):
#         isEnter.add((row,M-1))
#         heapq.heappush(heap, heightMap[row][M-1])
#     for col in range(M-1):
#         isEnter.add((,col))
#         heapq.heappush(heap, heightMap[0][col])
class Node(object):
    def __init__(self, val, col, row):
        self.val = val
        self.col = col
        self.row = row
    def __repr__(self):
        return f'value: {self.val}, position: {self.col} {self.row}'
    def __lt__(self, other):
        return self.val < other.val
heap = [Node(1,0,0), Node(5,0,1), Node(3,2,1), Node(10,5,1)]

heapq.heapify(heap)
print(heap)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
