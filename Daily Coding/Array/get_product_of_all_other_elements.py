'''
Input: Array [1,2,3,4,5]
要求：返回一个数列，新数列的每个位置上是原数列所有其他位置数字的成绩
Output: [120, 60, 40, 30, 24]

'''
def getProduct(arr):
    n = len(arr)
    left = [None] * n
    right = [None] * n
    left[0] = right[-1] = 1
    ans = [None] * n

    for i in range(1, n):
        left[i] = left[i-1] * arr[i-1]
    for j in reversed(range(n-1)):
        right[j] = right[j+1] * arr[j+1]
    for m in range(n):
        ans[m] = left[m] * right[m]
    return ans



a1 = [0,1,2,3,4]
assert getProduct(a1) == [24,0,0,0,0]
a1 = [0,0,2,3,4]
assert getProduct(a1) == [0,0,0,0,0]
a1 = [1,2,3,4,5]
assert getProduct(a1) == [120, 60, 40, 30, 24]
