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
