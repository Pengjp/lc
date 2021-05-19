# 如果自由使用arr[index]的面值，组成rest这么多钱，返回方法数
def recursive(arr, index, rest):
    if index == len(arr):
        return 1 if rest == 0 else 0
    ways = 0
    zhang = 0
    while zhang * arr[index] <= rest:
        # 已经到搞定了当前的index，需要计算下一个位置
        ways += recursive(arr, index+1, rest-zhang*arr[index])
        zhang += 1
    return ways
'''
两个可变参数，index，rest
变化范围，index: 0 - len(arr)-1
         rest: 0 - sum
这个例子中，dp表的大小为 4*11 （0-3） * （0-11）
该问题在补充dp表任意一个位置index ！= len(arr)的位置的时候，每一列依赖的数值不一样，由面额决定
但是在从左往右填表的时候，只需要加上rest-当前面额的位置的数值
dp[index][rest] = dp[index+1][rest] + dp[index+1][rest-arr[index]]
'''
def dp(arr, aim):
    N = len(arr)
    dp = [[0 for _ in range(aim+1)] for _ in range(N+1)]
    # 根据base case
    dp[N][0] = 1
    # 从下往上fill
    for i in range(N-1,-1,-1):
        for rest in range(aim+1):
            dp[i][rest] = dp[i+1][rest]
            if rest - arr[i] >= 0: # 不越界，加上本行的下一个
                dp[i][rest] += dp[i][rest-arr[i]]
    return dp[0][aim] #根据主函数返回 print(recursive(arr, 0, sum))
arr = [5, 2, 3]
sum = 10
print(recursive(arr, 0, sum))
print(dp(arr,sum))
