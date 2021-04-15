def partition(arr,l,r):
    if l>=r:
        return
    k = arr[r]
    less_qual_bond = l-1
    for i in range(l,r):
        if arr[i] <= k:
            less_qual_bond += 1
            arr[less_qual_bond], arr[i] = arr[i], arr[less_qual_bond]
    less_qual_bond += 1
    arr[less_qual_bond], arr[r] = arr[r], arr[less_qual_bond]
    partition(arr, l, less_qual_bond-1)
    partition(arr,less_qual_bond+1, r)

arr = [5,4,3,2,1,0]
partition(arr,0,len(arr)-1)
print(arr==[0,1,2,3,4,5])

arr = [4,3,7,2,9,1,8]
partition(arr,0,len(arr)-1)
print(arr==[1,2,3,4,7,8,9])

arr = [1,2,3,4,7,8,9]
partition(arr,0,len(arr)-1)
print(arr==[1,2,3,4,7,8,9])
