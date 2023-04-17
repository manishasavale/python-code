def factorial(n):
    n = n if n > 1 else 1
    j = 1
    for i in range(1, n + 1):
        j = j * i
    return j


# Testing ...
for i in range(1, 10):
    print( i, '->', factorial(i))
