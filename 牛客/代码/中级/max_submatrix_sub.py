'''
转换二维到一维
假设矩阵的大小是3 × 4
对于每一列，求出1列的最大累加和，
然后1和2列加一起，变成一列，求出最大累加和
然后1，2的和加上3，变成一列，求出最大累加和

对于第二列，求出最大累加和
然后2 3 加一起，求出最大累加和

然后第三列求出最大累加和
'''
def maxSubArray(nums):
    ans = -999999
    cur = 0
    for i in nums:
        cur += i
        ans = max(ans, cur)
        cur = max(0, cur)
    return ans

def max_submatrix(matrix):
    ROW = len(matrix)
    COL = len(matrix[0])
    ans = -999999
    for row in range(ROW):
        temp = matrix[row]
        ans = max(maxSubArray(temp), ans)
        for subrow in range(row + 1, ROW):
            temp = [sum(x) for x in zip(temp, matrix[subrow])]
            ans = max(maxSubArray(temp), ans)
    return ans

m = [[-90, 48, 78],[64, -40, 64],[-81, -7, 66]]
print(max_submatrix(m))

m = [[-1, -1, -1],[-1, 2, 2],[-1, -1, -1]]
print(max_submatrix(m))
