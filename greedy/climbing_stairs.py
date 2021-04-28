def solve(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return solve(n-1) + solve(n-2)

def solve1(n):
    if n == 1:
        return 1
    ans = [0 for i in range(n)]
    ans[0], ans[1] = 1,2
    for i in range(2,n):
        ans[i] = ans[i-1] + ans[i-2]
    return ans[n-1]

dic = {1:1, 2:2}
def solve2(n):
    if n not in dic:
        dic[n] = solve2(n-1) + solve2(n-2)
    return dic[n]

print(solve2(5))
