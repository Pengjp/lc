def merge(arr,l,m,r):
    help = []
    p1 =l
    p2 = m + 1
    while p1 <= m and p2 <= r:
        if arr[p1] <= arr[p2]:
            help.append(arr[p1])
            p1 += 1
        else:
            help.append(arr[p2])
            p2 += 1

    for i in range(p1,m+1):
        help.append(arr[i])
    for i in range(p2, r+1):
        help.append(arr[i])
    for i in range(len(help)):
        arr[l+i] = help[i]


def mergesort(arr,l,r):
    if l == r:
        return
    mid = (r+l)//2
    mergesort(arr,l,mid)
    mergesort(arr,mid+1,r)
    merge(arr,l,mid,r)

arr = [1,7,2,3,6,9,10,4]
mergesort(arr,0,len(arr)-1)
print(*arr)

''' 小和问题 '''
''' 如 [1,3,4,2,5] 小和为1+1+3+1+1+3+4+2=16
    利用归并排序来做
    可以看右边有多少个数比当前数大，有几个则产生几个小和
    比如 1 右边有四个比1大的数，则有4个1， 同理
    有2个3 1个4 1个2 0个5'''

def merge(arr,l,m,r):
    small_sum = 0 # 不同点
    help = []
    p1 =l
    p2 = m + 1
    while p1 <= m and p2 <= r:
        if arr[p1] < arr[p2]: # 不同点
            small_sum += arr[p1]*(r-p2+1) # 不同点
            help.append(arr[p1])
            p1 += 1
        else:
            help.append(arr[p2])
            p2 += 1

    for i in range(p1,m+1):
        help.append(arr[i])
    for i in range(p2, r+1):
        help.append(arr[i])
    for i in range(len(help)):
        arr[l+i] = help[i]
    return small_sum

def mergesort(arr,l,r):
    if l == r:
        return 0
    mid = (r+l)//2
    return mergesort(arr,l,mid) + mergesort(arr,mid+1,r) + merge(arr,l,mid,r)

arr = [1,3,4,1,5]
print(mergesort(arr,0,len(arr)-1))
print(*arr)
