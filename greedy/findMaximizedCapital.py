import heapq
def findMaximizedCapital(k , m , costs , profits ):
    tasks = []
    for i in range(len(costs)):
        tasks.append([costs[i],profits[i]])
    # sort all tasks by cost, from large to small
    tasks.sort(key=lambda x: x[0], reverse=True)
    maxpq = []
    for i in range(k):
        while len(tasks) > 0 and tasks[-1][0] <= m:
                maxpq.append(tasks.pop())
        if len(maxpq) == 0:
            return m
        cur_task = max(maxpq, key = lambda x: x[1])
        maxpq.remove(cur_task)
        m += cur_task[1]
    return m


k, m, costs, profits = 175,285,[339,229,271,206,375,432],[206,436,444,265,253,55]
assert (findMaximizedCapital(k , m , costs , profits ) == 1944)
