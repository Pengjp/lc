'''
数轴上有N个点，求一条长度为K的线段最多覆盖多少个点？
'''
n, k = 5, 3
arr = [1,2,3,4,5]
l, r = 0, 0
ans = 0
while l < n:
    while r < n and arr[r] - arr[l] < k:
            r += 1
    ans = max(ans, r-l)
    l += 1
print(ans)
