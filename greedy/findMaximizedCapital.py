import heapq
'''
因为我们要在可做的项目里选收益最高的做，则用两个heap
一个是maxheap,存放可做项目的收益，从大到小
一个是minheap，存放不可做的项目，用cost排序，从小到大
如果max不空，且还能做任务，则先看我们还能否加新的任务
加完任务后从max里面做一个并且弹出。
'''
def demo1(W, K, costs, profits):
    minheap, maxheap = list(), list()
    for i in range(len(costs)):
        if costs[i]<=W:
            maxheap.append(-profits[i])
        else:
            minheap.append((costs[i], profits[i]))
    heapq.heapify(minheap)
    heapq.heapify(maxheap)
    res = W
    while K > 0 and maxheap:
        while minheap and minheap[0][0]<=res:
            heapq.heappush(maxheap, -minheap[0][1])
            heapq.heappop(minheap)
        K-=1
        res -= heapq.heappop(maxheap) # maxheap存放的是负数

    return res

k, m, costs, profits = 175,285,[339,229,271,206,375,432],[206,436,444,265,253,55]
assert (demo1(m,k , costs , profits ) == 1944)
m,k = 3,2
costs = [5,4,1,2]
pro = [3,5,3,2]
print(demo1(m,k,costs,pro) == 11)
