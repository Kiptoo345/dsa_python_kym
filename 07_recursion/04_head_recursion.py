def tail_recursion(n):
    if n < 1:
        return n

    tail_recursion(n - 1)
    print(n)


tail_recursion(5)
