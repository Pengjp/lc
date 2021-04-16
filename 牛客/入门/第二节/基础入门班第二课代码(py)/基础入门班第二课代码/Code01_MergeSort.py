import random
def merge(arr, L, mid, R):
    help = [0]*(R-L+1)
    i = 0
    p1 = L
    p2 = mid + 1
    while p1 <= mid and p2 <= R:
        if arr[p1] <= arr[p2]:
            help[i] = arr[p1]
            i += 1
            p1 += 1
        else:
            help[i] = arr[p2]
            i += 1
            p2 += 1
    while p1 <= mid:
        help[i] = arr[p1]
        i += 1
        p1 += 1
    while p2 <= R:
        help[i] = arr[p2]
        i += 1
        p2 += 1
    for i in range(0,len(help)):
        arr[L + i] = help[i]


def process(arr, L, R):
    if L == R:
        return
    mid = L + ((R - L) >> 1)
    process(arr,L,mid)
    process(arr,mid + 1,R)
    merge(arr,L,mid,R)


def mergeSort(arr):
    if len(arr) < 2:
        return
    process(arr,0,len(arr)-1)

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
        mergeSort(arr1)
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
    mergeSort(arr)
    printArray(arr)


