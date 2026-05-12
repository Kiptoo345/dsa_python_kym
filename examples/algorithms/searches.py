import random

# 1.)linear - starts  in the beginning.
def linear_search(values, target):
    #for item in range(len(values)):#gives on item at a time
        #if target == values[item]:
            #pass
    #return -1
    for index in range(len(values)):
        print(f"comparing {target} to {values[index]}")
        if target == values[index]:
            return index
    return -1
    

values = random.sample(range(10,20),5)
print(f"The list of values are {values}")

target = int(input("Enter a number to search: "))

result = linear_search(values,target)
if result != -1:
    print(f"item {values[result]} found at index {result}")
else:
    print("Not found")
            
            

