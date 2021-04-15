class HeapSort:
    def __init__(self,arr):
        self.arr = arr
        self.heapSort()
    def heapInsert(self,index):
        while arr[index] > arr[(index-1)//2] :
            if index == 0:
                break
            arr[index], arr[(index-1)//2] = arr[(index-1)//2], arr[index]
            index = (index-1)//2
    def heapify(self,index,heapsize):
        left = 2*index+1
        while left < heapsize:
            # 两个孩子中找到较大的那个
            largest = left+1 if left+1 < heapsize and arr[left+1] > arr[left] else left
            # 较大的孩子和父节点比较
            largest = largest if arr[largest] > arr[index] else index
            # 最大是自己，无需下沉
            if largest == index:
                break
            arr[largest],arr[index] = arr[index],arr[largest]
            index = largest
            left = 2*index+1
    def heapSort(self):
        # O(NlogN)
        # for i in range(len(arr)):
        #     self.heapInsert(i)
        # O(N)
        for i in range(len(arr)-1,-1,-1):
            self.heapify(i,len(arr))
        heapsize = len(arr)
        # swap first and last item
        arr[0],arr[heapsize-1] = arr[heapsize-1],arr[0]
        heapsize -= 1
        while heapsize > 0:
            self.heapify(0,heapsize)
            arr[0],arr[heapsize-1] = arr[heapsize-1],arr[0]
            heapsize -= 1

# arr = [3,1,4,2,7,6]
# t = HeapSort(arr)
# print(t.arr)


def compare(x, y):
    return x[0] - y[0]

data = [(4, None), (3, None), (2, None), (1, None)]
from functools import cmp_to_key
print(sorted(data, key=cmp_to_key(compare)))

[(1, None), (2, None), (3, None), (4, None)]


def heapify(arr,n,index):
    left = 2*index + 1
    largest = left+1 if left+1 < n and arr[left+1] > arr[left]

arr = [3,1,4,2,7,6]

def heapify(arr,index,size):
    left = 2*index + 1
    while left < size:
        largest = left
        if left+1 < size and arr[left+1] > arr[left]:
            largest = left + 1
        if not arr[largest] > arr[index]:
            break
        arr[largest], arr[index] = arr[index], arr[largest]
        index = largest
        left = 2*index + 1


def heapSort(arr=arr):
    for i in range(len(arr)-1,-1,-1):
        heapify(arr,i,len(arr))
    heapsize = len(arr)
    # swap first and last item
    arr[0],arr[heapsize-1] = arr[heapsize-1],arr[0]
    heapsize -= 1
    while heapsize > 0:
        heapify(arr,0,heapsize)
        arr[0],arr[heapsize-1] = arr[heapsize-1],arr[0]
        heapsize -= 1
heapSort()
print(*arr)
