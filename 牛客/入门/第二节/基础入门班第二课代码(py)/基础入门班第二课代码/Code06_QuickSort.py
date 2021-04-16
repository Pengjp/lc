import random

def Swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

#这是一个处理arr[l..r]的函数
#默认以arr[r]做划分，arr[r] -> p     <p   ==p   >p
#返回等于区域(左边界，右边界), 所以返回一个长度为2的数组res, res[0] res[1]
def partition(arr, L, R):
    less = L - 1 #<区右边界
    more = R #>区左边界
    while L < more: #L表示当前数的位置   arr[R]  ->  划分值
        if arr[L] < arr[R]: #当前数   <  划分值
            less += 1
            Swap(arr,less,L)
            L += 1
        elif arr[L] > arr[R] :#当前数   >  划分值
            more -= 1
            Swap(arr,more,L)
        else :
            L += 1
        Swap(arr,more,R)
        return  [less + 1,more]


def QuickSort(arr,L,R):
    if L < R:
        Swap(arr,L + (int(random.random() * (R-L + 1))),R)
        p = partition(arr,L,R)
        QuickSort(arr,L,p[0] - 1)
        QuickSort(arr,p[1] + 1,R)

def quickSort(arr):
    if len(arr) < 2:
        return 
    QuickSort(arr,0,len(arr) - 1)

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
        quickSort(arr1)
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
    quickSort(arr)
    printArray(arr)


