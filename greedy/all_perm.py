def process(str, path, ans):
    print('current str',str,'current path',path)
    if not str:
        ans.add(path)
        return
    for i in range(len(str)):
        pick = path + str[i]
        next = str
        next = next[:i] + next[i + 1:]
        process(next, pick, ans)

ans = set()
process('aac','',ans)
print(ans)
