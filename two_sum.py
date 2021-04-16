def twoSum(numbers , target ):
    ha = {val:index for index,val in enumerate(numbers)}
    for index,num in enumerate(numbers):
        diff = target-num
        if diff in ha and ha[diff]!=index:
            index1 = min(index,ha[diff])
            index2 = max(index,ha[diff])
            return (index1+1,index2+1)

print(twoSum([2,1,9,4,4,56,90,3],8))
