import random

def binary_recursive(values, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    print(f"Low {low}")
    print(f"Mid {mid}")
    print(f"High {high}")
    if target == values[mid]:
        return mid
    elif target > values[mid]:
        return binary_recursive(values, target, mid + 1, high)
    else:
        return binary_recursive(values, target, low, mid - 1)


values = random.sample(range(1, 10),7) # generate random values
values = sorted(values) # sort the values
print(f"The list is {values}")
target = int(input("Enter value to search : "))
result = binary_recursive(values, target, 0, len(values))
if result != -1:
    print(f"Item {values[result]} found at index {result}")
else:
    print("Not found")