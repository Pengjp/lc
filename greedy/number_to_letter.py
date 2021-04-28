def process(str, i, path):
    if i == len(str):
        ans.append(path)
        return  # 证明决策结束，所有之前的决策加起来，是一种情况
    cur = str[i]
    if cur == '0':
        return
    if cur == '1':
        process(str, i+1, path+'a')
        if i+1 < len(str):
            num = int(str[i:i+2])
            process(str, i+2, path+chr(ord('`')+num))
    if cur == '2':
        process(str, i+1, path+'b')
        if i+1 < len(str):
            num = int(str[i:i+2])
            if num <= 26:
                process(str, i+2, path+chr(ord('`')+num))
    process(str, i+1, path+chr(ord('`')+int(cur)))
ans = []
process('11111',0,'')
print(set(ans))

def process(str, i):
    if i == len(str):
        return 1
    if str[i] == '0':
        return 0
    if str[i] == '1':
        res = process(str, i+1)
        if i+1 < len(str):
            res += process(str, i+2)
        return res
    if str[i] == '2':
        res = process(str, i+1)
        if i+1 < len(str):
            num = int(str[i:i+2])
            if num <= 26:
                res += process(str, i+2)
        return res
    return process(str, i+1)

print(process('123',0))
