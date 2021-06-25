def process(arr, index, rest):
    if rest < 0:
        return -1
    if index == len(arr):
        return 1
    # 是否要index位置的零食
    next1 = process(arr, index+1, rest) # 不要
    next2 = process(arr, index+1, rest-arr[index]) # 要
    if next2 == -1:
        return next1
    else:
        return next1 + next2
# 改成dp，有两个自由变量，则生成一个二维表格
def dpway(arr, w):
    n = len(arr)
    dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
    dp[n] = [1 for _ in range(w+1)] # 对应line4
    # index,rest 依赖 next1 （index+1,rest), next2(index+1, rest-arr[i])
    # 因为任意位置依赖下面一行的位置，所以是从下往上填写
    for index in range(n-1,-1,-1):
        for rest in range(w+1):
            next1 = dp[index+1][rest]
            if rest - arr[index] >= 0:
                dp[index][rest] = next1 + dp[index+1][rest - arr[index]]
            else:
                dp[index][rest] = next1
    print(dp)
    return max(dp[0])


def dpway2(arr, w):
    n = len(arr)
    dp = [1 for _ in range(w+1)]
    for index in range(n-1,-1,-1):
        temp = [0 for _ in range(w+1)]
        for rest in range(w+1):
            next1 = dp[rest]
            if rest - arr[index] >= 0:
                temp[rest] = next1 + dp[rest - arr[index]]
            else:
                temp[rest] = next1
        dp = temp
    return max(dp)
arr = [1,2,4]
rest = 10
print(process(arr,0,rest))
print(dpway(arr,rest))
print(dpway2(arr,rest))
