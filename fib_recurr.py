def fib(n):
    """ Fibonacci:
    fib(n) = fib(n - 1) + fib(n - 2) where n > 1
    fib(n) = 1 where n <= 1
    """
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1


# Show Fibonacci from 1 to 5
for i in [1, 2, 3, 4, 5]:
    print(i, '=>', fib(i))
