def fib(n):
    """ Fibonacci:
    fib(n) = fib(n -1 ) + fib(n - 2) where n > 1
    fib(n) = 1 where n <= 1
    """

    # the first two values
    l = [1, 1]

    # Calculating the others
    for i in range(2, n + 1):
        l.append(l[i - 1] + l[i - 2])

    return l[n]


# Show Fibonacci from 1 to 5
for i in [1, 2, 3, 4, 5]:
    print(i, '=>', fib(i))
