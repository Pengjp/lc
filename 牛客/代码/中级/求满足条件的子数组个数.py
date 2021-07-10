'''
给定数组 arr 和整数 num，共返回有多少个子数组满足如下情况：
max(arr[i...j]) - min(arr[i...j]) <= num
max(arr[i...j])表示子数组arr[i...j]中的最大值，min[arr[i...j])表示子数组arr[i...j]中的最小值。
'''
def ways(arr, num):
    l, r, res = 0, 0, 0
    qmax, qmin = [], []
    while l < len(arr):
        while r < len(arr):
            while qmax and arr[r] >= arr[qmax[-1]]:
                qmax.pop()
            qmax.append(r)
            while qmin and arr[r] <= arr[qmin[-1]]:
                qmin.pop()
            qmin.append(r)
            if arr[qmax[0]] - arr[qmin[0]] > num:
                break
            r += 1
        res += r - l
        if qmin[0] == l:
            qmin.pop(0)
        if qmax[0] == l:
            qmax.pop(0)
        l += 1
    return res

print(ways([1,2,3,4,5], 2))
