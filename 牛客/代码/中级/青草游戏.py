def winner(n):
    if n < 5:
        return "后手" if n == 0 or n == 2 else "先手"
    base = 1
    while base <= n:
        if winner(n - base) == "后手":
            return "先手"
        if base > n / 4:
            break
        base *= 4
    return "后手"

def winner2(n):
    if n % 5 == 0 or n % 5 == 2:
        return '后手'
    else:
        return '先手'

for i in range(20):
    print(i,winner(i), winner2(i))
