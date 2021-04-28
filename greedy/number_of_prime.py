'''
已知 n 个整数 x1,x2,…,xn，以及一个整数 k（k＜n）。从 n 个整数中任选 k 个整数相加，
可分别得到一系列的和。例如当 n=4，k＝3，4 个整数分别为 3，7，12，19 时，可得全部的组合与它们的和为：
3＋7＋12=22　　3＋7＋19＝29　　7＋12＋19＝38　　3＋12＋19＝34。
现在，要求你计算出和为素数共有多少种。
例如上例，只有一种的和为素数：3＋7＋19＝29）。
'''

def is_prime(num: int):
    i = 2
    while i <= num ** 0.5:
        if num % i == 0:
            return 0
        i += 1
    return 1

def process(numbers, K, idx, count):
    if K == 0:
        return is_prime(count)
    sum_number = 0
    for i in range(idx, len(numbers)):
        sum_number += process(numbers, K - 1, i + 1, count + numbers[i])
    return sum_number

k = 3
arr = [3,7,12,19]
print(process(arr,k,0,0))
