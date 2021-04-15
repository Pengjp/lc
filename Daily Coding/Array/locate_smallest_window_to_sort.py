'''
Input: [3,7,5,6,9]
Output: (1,3)
要求：给定一个数列，返回一个数组，该数组表示为了让输入数列成为有序数列最小的需要排序
     的范围， 若该数组已经有序，则返回 (-1, -1)
'''
def window(arr):
    begin, end = -1,-1
    rmax, rmin = -1e10, 1e10
    for i in range(len(arr)):
        rmax = max(arr[i], rmax)
        if arr[i] < rmax:
            end = i
    for i in range(len(arr)-1,-1,-1):
        rmin = min(arr[i],rmin)
        if arr[i] > rmin:
            begin = i
    return (begin, end)

arr = [3,7,5,6,9]
assert window(arr) == (1,3)
arr = [3,6,7,5,9]
assert window(arr) == (1,3)
arr = [5,3,7,6,9]
assert window(arr) == (0,3)
arr = [1,2,3]
assert window(arr) == (-1,-1)
arr = [1]
assert window(arr) == (-1,-1)
arr = [1,2,4,3]
assert window(arr) == (2,3)
arr = [4,3,2,1]
assert window(arr) == (0,3)
