def allSub(str, i, res):
    if i == len(str):
        ans.append(res)
        return
    else:
        allSub(str, i+1, res)  # 不要下标为i+1的字符
        allSub(str, i+1, res+str[i]) # 要第i+1个字符
ans = []
str = 'abc'
allSub(str, 0, '')
print(ans)
