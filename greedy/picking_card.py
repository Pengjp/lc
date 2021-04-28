'''给定一个整型数组arr，代表数值不同的纸牌排成一条线，玩家A和玩家B依次拿走每张纸牌，
规定玩家A先拿，玩家B后拿，但是每个玩家每次只能拿走最左和最右的纸牌，玩家A和玩家B绝顶聪明。
请返回最后的获胜者的分数。
'''
# 先手函数
def f(arr,i,j):
    if i == j: # 如果只剩下一张牌，直接拿走
        return arr[i]
            #拿左边的
    return max(arr[i] + s(arr,i+1,j),\
     arr[j]+s(arr,i,j-1)) # 拿右边的

#后手函数
def s(arr,i,j):
    if i == j:
        return 0
    # 因为两者都会利益最大化，先手则会拿最大的，后手则需要选最小的
    return min(f(arr,i+1,j), f(arr,i,j-1))

arr = [1,2,100,4]
# 返回先拿还是后拿中最大的
print(max(f(arr,0,3),s(arr,0,3)))
