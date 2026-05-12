import random

# 2.)Binary Search - starts in the middle

def binary_reccursive(values, target, low, high):
    if low > high:
        return -1
    mid = (low + high)// 2
    if target == values[mid]:
        return mid
    elif target > values[mid]:
        return binary_reccursive(values, target, mid + 1, high)
    else:
        return binary_reccursive(values, target, low, mid - 1)
        
    
values = random.sample(range(10,20),5)
values = sorted(values)

print(f"The list of values are {values}")

target = int(input("Enter a number to search: "))

result = binary_reccursive(values,target,low , high)
if result != -1:
    print(f"item {values[result]} found at index {result}")
else:
    print("Not found")

