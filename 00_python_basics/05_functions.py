import random 
#a function that filters through a given set of numbers and retruns the laregst or smallest 
# ALWAYS exit aa program after the loop.


def max_min(mlist):
    minimum = mlist[0]
    for num in mlist:
        if num < minimum:
            minimum = num 
    return minimum
    #print(f"Value is {minimum}")#return exits a program from where it is, and should be after the for loop otherwise the the loop won't run fully
    
def getValues():
    mlist = random.sample(range(1,30),k=7)#
    print(mlist)
    results = max_min(mlist)
    print(f"The smallest value is {results}")
    
getValues()