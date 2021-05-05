def getNearLess(arr):
    res = [[-1,-1] for _ in range(len(arr))]
    # 生成一个单调栈，严格的单调递增，里面储存的是List of index ，同样值的放在list里面
    stack = []
    for i in range(len(arr)):
        while stack and arr[stack[-1][0]] > arr[i]: # 如果stack顶部的值大于当前数值，需要弹出并且生成答案
            pop_index = stack.pop()
            # 左边里当前位置最小的是当前stack的顶部的list中最后一个，如果stack是空，则为-1
            if stack:
                leftLessIndex = stack[-1][-1]
            else:
                leftLessIndex = -1
            for index in pop_index:
                res[index][0] = leftLessIndex
                res[index][1] = i
        # while loop 结束后，比arr[i] 的都已经弹出了，剩下两种情况，相等和比它小的
        if stack and arr[stack[-1][0]] == arr[i]: # 相等情况
            stack[-1].append(i)
        else:
            stack.append([i])
    # 清算剩余的元素
    while stack:
        pop_index = stack.pop()
        if stack:
            leftLessIndex = stack[-1][-1]
        else:
            leftLessIndex = -1
        for index in pop_index:
            res[index][0] = leftLessIndex
            res[index][1] = -1
    return res

print(getNearLess([3,4,1,5,6,2,7]))
