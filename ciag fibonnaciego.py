def fib(N, l1, l2):
    if N > 0:
        print(l1 + l2)
        fib(N - 1, l2, l1 + l2)

fib(10,0,1)