import random

#某个数现在处在index位置，往上继续移动
def heapInsert(arr, index):
    while arr[index] > arr[int((index - 1) / 2)]:
        Swap(arr,index,int((index-1)/2))
        index = int((index - 1) / 2)


def Swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

#某个数在index位置，能否往下移动
def heapify(arr, index, heapSize):
    left = index * 2 + 1 #左孩子的下标
    while left < heapSize: #下方还有孩子的时候
        #两个孩子中，谁的值大，把下标给largest
        largest = 0
        if left + 1 < heapSize and arr[left + 1] > arr[left]:
            largest = left + 1
        else :
            largest = left
        #父和较大的孩子之间，谁的值大，把下标给larges
        if arr[largest] > arr[index]:
            largest = largest
        else:
            largest = index
        if largest == index : break
        Swap(arr,largest,index)
        index = largest
        left = index * 2 + 1


def HeapSort(arr):
    if len(arr) < 2:
        return ;
    for i in  range(len(arr)):
        heapInsert(arr,i)
    heapSize = len(arr)
    heapSize -= 1
    Swap(arr,0,heapSize)
    while heapSize > 0:
        heapify(arr,0,heapSize)
        heapSize -= 1
        Swap(arr,0,heapSize)

def comparator(arr):
    sorted(arr)

def copyArray(arr):
    if arr == None:
        return None
    res = [0]*(len(arr))
    for i in range(len(arr)):
        res[i] = arr[i]
    return res

def isEqual(arr1,arr2):
    if ((arr1 == None and arr2 != None)) or ((arr1 != None and arr2 == None)):
        return False
    if arr1 == None and arr2 == None:
        return True
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True
def printArray(arr):
    if arr == None:
        return
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print("")
def generateRandomArray(maxSize,maxValue):
    arr = [0]* int((maxSize + 1) * random.random())
    for i in range(len(arr)):
        arr[i] = int(((maxValue + 1) * random.random()) - (int(maxValue * random.random())))

    return arr


if __name__ == "__main__":
    testTime = 5000
    maxSize = 100
    maxValue = 100
    succeed = True
    for i in range(testTime):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = copyArray(arr1)
        HeapSort(arr1)
        comparator(arr2)
        if isEqual(arr1, arr2) == False:
            succeed = False
            printArray(arr1)
            printArray(arr2)
            break
    if succeed == False:
        print("Nice!")
    else:
        print("Fucking fucked")
    arr = generateRandomArray(maxSize, maxValue)
    printArray(arr)
    HeapSort(arr)
    printArray(arr)


