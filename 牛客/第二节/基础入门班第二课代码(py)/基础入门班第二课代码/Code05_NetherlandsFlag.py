import random

def Swap(arr, i, j):
    arr[i],arr[j] = arr[j], arr[i]

def partition(arr, L, R,p):
    less = L - 1 #<区右边界
    more = R + 1 #>区左边界
    while L < more: #L是当前数的下标
        if arr[L] < p:
            less += 1
            Swap(arr,less,L)
            L += 1
        elif arr[L] > p :
            more -= 1
            Swap(arr,more,L)
        else :
            L += 1

    return [less + 1,more - 1]


def generateRandomArray():
    arr = [0]* 10
    for i in range(len(arr)):
        arr[i] = int(3 * random.random())

    return arr


if __name__ == "__main__":
        test = generateRandomArray()
        print(test)
        res = partition(test,0,len(test) - 1,1)
        print(test)
        print(res[0])
        print(res[1])
