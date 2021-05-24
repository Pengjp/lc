import heapq
# Min heap
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

# Max heap
class Node(object):
    def __init__(self, val, col, row):
        self.val = val
        self.col = col
        self.row = row
    def __repr__(self):
        return f'value: {self.val}, position: {self.col} {self.row}'
    def __lt__(self, other):
        return self.val > other.val
heap = [Node(1,0,0), Node(5,0,1), Node(3,2,1), Node(10,5,1)]

heapq.heapify(heap)
print(heap)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
