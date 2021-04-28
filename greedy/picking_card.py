# 先手函数
def f(arr,i,j):
    if i == j: # 如果只剩下一张牌，直接拿走
        return arr[i]
    return max(arr[i] + s(arr,i+1,j), arr[j]+s(arr,i,j-1))
def s(arr,i,j):
    if i == j:
        return 0
    return min(f(arr,i+1,j), f(arr,i,j-1))

arr = [1,2,100,4]
print(f(arr,0,3))
print(s(arr,0,3))
print(max(f(arr,0,3),s(arr,0,3)))
