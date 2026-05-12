#direct and tail recursion

def direct_recursion(n):
    if n<1:
        return n #this is a base case.It helps the code exit the loop
    
    print(n)
    return direct_recursion(n-1)

#direct_recursion(5)

#indirect recursion - a function calling another function

#def a(n):
    if n>0:
        print(n)
        return b(n-1)

#def b(n):
    if n<1:
        return n
    else:
        print(n)
        return a(n-1)
    
#a(7)

#in head recursion the print stattement is after the function calling
#e.g  return direct_recursion(n-1)
#     print(n)

# When defining a fucntion we pass three figures: parameters, return adress and local variables

def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
    c()
    print(4)
def c():
    print(5)
    return 0 #clearing the stack

a()