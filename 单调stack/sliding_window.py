''' 求滑动窗口最大值 '''
from collections import deque
def sliding(arr, size):
    dq = deque()
    ans = []
    for i in range(len(arr)):
        # if new element is larger than right most ele, pop it
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        # maintain a stricly decreasing deque from left to right
        dq.append(i)
        # pop old ele to maintain proper size
        if i - size >= dq[0]:
            dq.popleft()
        if i + 1 - size >= 0:
            ans.append(arr[dq[0]])
    return ans

arr = [4,3,5,4,3,3,6,7]
size = 3
print(sliding(arr,size))
