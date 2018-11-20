def fib(n):
    if n <= 1:
        return [1]
    if n == 2:
        return [1,1]

    f = fib(n - 1)
    f.append(f[-1] + f[-2])
    return f

print(fib(15))
