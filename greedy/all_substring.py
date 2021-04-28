def allSub(str, i, res):
    if i == len(str):
        ans.append(res)
        return
    else:
        allSub(str, i+1, res)
        allSub(str, i+1, res+str[i])
ans = []
str = 'abc'
allSub(str, 0, '')
print(ans)
