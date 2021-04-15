import time
N = 100
# def fib(n):
#     if n<=0: return 0
#     elif n == 1: return 1
#     return fib(n-1) + fib(n-2)
# t = time.time()
# for i in range(N):
#     fib(i)
# print(time.time()-t)

def fib2(n,memo):
    if n <= 0: return 0
    elif n == 1: return 1
    elif memo[n] > 0: return memo[n]

    memo[n] = fib2(n-1,memo) + fib2(n-2,memo)
    return memo[n]

t = time.time()
memo = [0 for _ in range(N+1)]
for i in range(N):
    print(fib2(i,memo))
print(time.time()-t)
