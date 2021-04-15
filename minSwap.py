# Minimum swaps required to bring all elements less than or equal to k together
# quick sort 的基础
def minswap(arr,k):
    less_qual_bond = -1
    n = 0
    for i in range(len(arr)):
        if arr[i] <= k:
            less_qual_bond += 1
            arr[less_qual_bond], arr[i] = arr[i], arr[less_qual_bond]
            n += 1
    return arr,n

arr = [2,7,9,5,8,7,4]
arr = [5,4,3,2,1,0]
print(minswap(arr,arr[-1]))
