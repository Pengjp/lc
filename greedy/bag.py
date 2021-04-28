def process(w,v,index,already,bag):
    if already > bag:
        return -1
    if index == len(w):
        return 0
    p1 = process(w,v,index+1,already,bag)
    p2next = process(w,v,index+1,already+w[index],bag)
    p2 = -1
    if p2next != -1:
        p2 = v[index] + p2next
    return max(p1,p2)

w = [1,3,5]
v = [1,3,5]

print(process(w,v,0,0,10))


def solve1(index,leftWeight):
    res=0
    if index >= len(w):
        return 0       #物品已用完,剩下的重量装不了物品，返回价值0
    if w[index]>leftWeight:       #当前位置的物品重量大于剩余重量，则不选择该物品，从它下一个物品进行背包问题
        res=solve1(index+1,leftWeight)
    else:
        #还剩物品，并且当前位置的物品重量小于剩余重量，则就取该物品和不取该物品两种情况进行递归
        res=max(solve1(index+1,leftWeight),\
                solve1(index+1,leftWeight-w[index]) + v[index])
    return res

print(solve1(0,10))

def solve2(w,v,index,rest):
    if rest <= 0:
        return 0
    if index == len(w):
        return 0
    p1 = solve2(w,v,index+1, rest)
    p2 = -1
    if rest >= w[index]:
        p2 = solve2(w,v,index+1, rest-w[index]) + v[index]
    return max(p1,p2)

print(solve2(w,v,0,10))
