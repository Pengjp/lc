'''
一群孩子做游戏，现在请你根据游戏得分来发糖果，要求如下：
1. 每个孩子不管得分多少，起码分到一个糖果。
2. 任意两个相邻的孩子之间，得分较多的孩子必须拿多一些糖果。(若相同则无此限制)
给定一个数组arr代表得分数组，请返回最少需要多少糖果。

数组中每个位置表示该位置孩子的分数
[1,2,2]
最少糖果情况则为，1，2，1
'''

'''
基础思路:
刻画出数组的高低变化情况，利用 Left，right 两个辅助数组
代表每一个位置的左右两边的高度
对于上面的例子

    2   2
1
left = [1, 2, 1]
right = [1, 1, 1]
答案就是每个位置 Left right的max
'''

def process(arr):
    left = [1 for _ in range(len(arr))]
    right = [1 for _ in range(len(arr))]

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            left[i] = left[i-1] + 1
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > arr[i+1]:
            right[i] = right[i+1] + 1
    ans = 0
    for i in range(len(arr)):
        ans += max(left[i], right[i])
    print(ans)

arr = [1,2,2]
process(arr)
