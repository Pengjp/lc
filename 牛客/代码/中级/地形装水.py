'''
有一个arr用来表示一个容器的形状，arr的每个数字表示高度，
                    [3,5,1,2,4]
               []
               []       []
            [] []       []
            [] []    [] []
            [] [] [] [] []
             0 1  2  3  4
所以最大存水量是在 2， 3列上，分别是3和2，总和是5

思路，用两个左右指针 l, r 分别从1和n-2位置向中间推进（因为0和n-1位置没法放水 i.e. 如果arr长度小于等于2直接返回0）
，两个指针来决定指向位置最大的放水量，哪边的最大值小来结算那边因为水量由最小值决定。
加入lmax小，那么用 水量就是 max(0, lmax-arr[l]), 结算完后移动l，对于r同理
'''
def compute(arr):
    if len(arr) < 3:
        return 0
    n = len(arr)
    l = 1
    r = n - 2
    lmax = arr[0]
    rmax = arr[n-1]
    ans = 0
    while l <= r:
        if lmax < rmax:
            print('left move at',l,'value is',max(0, lmax-arr[l]))
            ans += max(0, lmax-arr[l])
            lmax = max(lmax, arr[l])
            print('updated left max',lmax)
            l += 1
        else:
            print('right move at',r,'value is',max(0, rmax-arr[r]))
            ans += max(0, rmax-arr[r])
            rmax = max(rmax, arr[r])
            print('updated right max',rmax)
            r -= 1
    return ans

arr = [3, 5, 1, 2, 4]
print(compute(arr))
arr = [3, 1, 3]
print(compute(arr))
