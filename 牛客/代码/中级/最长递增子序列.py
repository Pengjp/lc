'''
300. Longest Increasing Subsequence
'''
# O(n^2)
def method1(arr):
    dp = [1 for _ in range(len(arr))]
    for index, val in enumerate(arr[1:]):
        index += 1
        temp = 0
        for i in range(index):
            if arr[i] < val:
                temp = max(temp, dp[i])
        dp[index] += temp
    return max(dp)

#新建 ends数组
# ends[i] means smallest ending number for all Increasing Subsequences with length i+1
# 总体思路，对于当前的数，在有效区域里找到刚比当前数大的，找到了，更新那个数，找不到，扩充有效区
# 来到 4 ends = [4 ~~~] dp = [1 ~~~]
# 来到 1，在有效区内用二分找到刚比1大的位置，找到了4. 用1替换4. 代表，更新之前，所有遇到的
# 长度为 1 (i = 0, i+1 = 1), 递增子序列最小结尾是4，现在是1. ends = [1 ···], 1 包括自己
# 在内左边有0个数，所有 dp = [1, 1~~~]
# 来到 9，在有效区内没有找到比自己大的，则扩充有效区 ends = [1, 9 ~~~] 当前ends表示
# 在目前为止，所以长度为1的最小结尾是1，长度为2的最小结尾是9，所以dp = [1, 1, 2 ~~~]
# 来到2， ends= [1, 2], dp = [1,1,2,2]

def binary_search(ends,num):
    if len(ends) == 0:
        return -1
    # if len(ends) == 1:
    #     return -1 if ends[0] < num else 0
    l, r = 0, len(ends)-1
    ans = -1
    while l <= r:
        mid = int((l + r) // 2)
        if ends[mid] < num:
            l = mid + 1
        elif ends[mid] > num:
            ans = mid
            r = mid - 1
        else:
            return mid
    return ans

def method2(arr):
    dp = [None for _ in range(len(arr))]
    ends = []
    for index, val in enumerate(arr):
        pos = binary_search(ends, val)
        if pos == -1:
            ends.append(val)
            dp[index] = len(ends)
        else:
            ends[pos] = val
            dp[index] = pos + 1
    print(max(dp))

arr = [18,55,66,2,3,54]
print(method1(arr))
print(method2(arr))
