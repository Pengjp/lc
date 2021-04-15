import queue as Q

def sortedArrDistanceLessK(arr,k):
    heap = Q.PriorityQueue()
    index = 0
    n = min(len(arr),k)
    while index < n:
        heap.put(arr[index])
        index += 1
    i = 0
    while index < len(arr):
        heap.put(arr[index])
        arr[i] = heap.get()
        index += 1
        i += 1
    while not heap.empty():
        arr[i] = heap.get()
        i += 1

if __name__ == "__main__":
    heap = Q.PriorityQueue()
    heap.put(8)
    heap.put(4)
    heap.put(4)
    heap.put(9)
    heap.put(10)
    heap.put(3)
    while not heap.empty():
        print(heap.get())

