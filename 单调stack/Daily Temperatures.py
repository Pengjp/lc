''' 739. Daily Temperatures '''
def rightMostCloseMin(arr):
    ''' find the right cloest value that is smaller that each element '''
    # a stack to to record the position, stricly increasing order from small to large
    stack = []
    ans = [0] * len(arr)
    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            pop_index = stack.pop()
            ans[pop_index] = i - pop_index
        stack.append(i)
    return ans

print(rightMostCloseMin([73, 74, 75, 71, 69, 72, 76, 73]))
