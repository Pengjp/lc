import heapq

def running_median(arr):
    maxpq = []
    minpq = []

    for i in arr:
        print('adding',i)
        # max为空 或者加入数值小于等于max顶部，放到max
        if len(maxpq) == 0 or i <= -maxpq[0]:
            heapq.heappush(maxpq, -i)
        else:
            heapq.heappush(minpq, i)
        # max和min的长度差距为2时候，长的转移到短的
        if abs(len(maxpq) - len(minpq)) > 1:
            if len(maxpq) > len(minpq):
                heapq.heappush(minpq, -heapq.heappop(maxpq))
            else:
                heapq.heappush(maxpq, -heapq.heappop(minpq))
        print('max',maxpq,'min',minpq)
        if len(maxpq) == len(minpq):
            print('median is',(-maxpq[0] + minpq[0]) / 2)
        else:
            if len(maxpq) > len(minpq):
                print('median is', -maxpq[0])
            else:
                print('median is', minpq[0])
        print()

arr = [5,2,3,4,1,6,7,0,8]
running_median(arr)
