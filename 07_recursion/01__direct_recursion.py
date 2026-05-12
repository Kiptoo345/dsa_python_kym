
def direct_recurion(n):
    if n < 1:
        return n

    print(n)
    return direct_recurion(n - 1)

direct_recurion(5)
