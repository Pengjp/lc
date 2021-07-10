'''
给定一个路径数组paths，表示一张图。
paths[i]==j代表城市i连向城市j，如果paths[i]==i表示i城市是首都，一张图里只会有一个首都，不会有分图且图中除了首都指向自己之外不会有环；
例如：paths={9,1,4,9,0,4,8,9,0,1} 由这个数组表示的图如下图所示。
城市1是首都所以距离为0；离首都距离为1的城市只有城市9；离首都距离为2的城市有城市0，3，7；离首都距离为3的城市有城市4，8；离首都距离为4的城市有城市2，5，6； 所以，距离为0的城市有1座；距离为1的城市有1座；距离为2的城市有3座；距离为3的城市有2座；距离为4的城市有3座；那么统计数组为numArr={1,1,3,2,3,0,0,0,0,0}，numArr[i]==j代表距离为i的城市有j座； 要求实现一个void类型的函数，输入一个路径数组paths，直接在原数组上调整，使之变为numArr数组。 paths={9,1,4,9,0,4,8,9,0,1}，函数处理后，paths={1,1,3,2,3,0,0,0,0,0}。 要求：如果paths长度为N，时间复杂度为O(N)，额外空间复杂度为O(1)；'''
def calculate_distance(arr, index):
    origin = index
    last = index
    cur = arr[index]
    while arr[cur] > -1 and arr[cur] != cur:
        # print('last',last)
        # print('cur',cur,'arr[cur]',arr[cur])
        next = arr[cur]
        # print('next',next)
        arr[cur] = last
        # print('arr[cur]',arr[cur])
        last = cur
        # print('last',last)
        cur = next
        # print('cur',cur)
        # print([arr[0],arr[2],arr[3],arr[5],arr[7]])
        # print()
    # now cur stands at either the capital or somewhere which negative value
    # which means we have visited that position before
    if arr[cur] == cur:
        distance = 0
    else:
        distance = arr[cur]

    while cur != origin:
        distance -= 1
        cur = last
        last = arr[cur]
        arr[cur] = distance

    # print([arr[0],arr[2],arr[3],arr[5],arr[7]])

def distansToNums(arr):
    for i in range(len(arr)):
        index = arr[i] # distance to capital for current city
        if index < 0: # it means we have not converted
            arr[i] = 0
            while True:
                index = -index
                if arr[index] > -1:
                    arr[index] += 1
                    break
                else:
                    nextIndex = arr[index]
                    arr[index] = 1
                    index = nextIndex
    arr[0] = 1

arr = [7,5,2,2,0,3,7,5]
arr = [9,1,4,9,0,4,8,9,0,1]
arr = [-2,1,-1,-2,-1,-3]

def process(arr):
    for index, value in enumerate(arr):
        if index == value or value < 0:
            continue
        calculate_distance(arr,index)

    distansToNums(arr)
    print(arr)

process(arr)
