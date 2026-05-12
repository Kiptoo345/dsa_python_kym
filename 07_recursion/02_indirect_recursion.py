def a(n):
    if n > 0:
        print(f"n inside a {n}")
        return b(n -1)

def b(n):
    if n < 1:
        return n
    else:
        print(f"n inside b {n}")
        return a(n - 1)
    
a(10)