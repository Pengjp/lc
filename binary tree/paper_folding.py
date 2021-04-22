def printProcess(i,N,down):
    if i > N:
        return
    printProcess(i+1, N, True)
    print('down') if down else print('up')
    printProcess(i+1, N, False)

def printall(N):
    printProcess(1, N, True)

printall(3)
