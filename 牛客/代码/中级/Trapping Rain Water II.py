'''
Given an m x n integer matrix heightMap representing the height of each unit
cell in a 2D elevation map, return the volume of water it can trap after raining.
有一个二维数字表示地形，计算装水量，对角线不考虑

边框先进minheap，
while minheap not empty：
    pop 堆上面 的ele
    更新cur_max
    让ele周围的位置入heap如果之前没有加过
    对于每一个新ele，计算水量max(0, ele-cur_max)
'''
# 建立 minheap
class Node(object):
    def __init__(self, val, row, col):
        self.val = val
        self.col = col
        self.row = row
    def __lt__(self, other):
        return self.val < other.val

import heapq
def trapRainWater(heightMap):
    ROW = len(heightMap) # row
    COL = len(heightMap[0]) # col
    heap = []

    # Push all the block on the border into heap
    for i in range(ROW):
        for j in range(COL):
            if i == 0 or j == 0 or i == ROW-1 or j == COL-1:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                heightMap[i][j] = -1
    water = 0
    max_val = 0
    while heap:
        height, i, j = heapq.heappop(heap)
        max_val = max(max_val, height)
        for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            if 0 <= x < ROW and 0 <= y < COL and heightMap[x][y] != -1:
                water += max(0, max_val-heightMap[x][y])
                heapq.heappush(heap, (heightMap[x][y], x, y))
                heightMap[x][y] = -1
    return water

heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
print(trapRainWater(heightMap))
