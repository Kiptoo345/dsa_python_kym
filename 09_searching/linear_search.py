import random

def linear_search(values, target):
    for index in range(len(values)):
        print(f"Comparing {target} vs {values[index]}")
        if target == values[index]:
            return index
        
    return -1

values = random.sample(range(-10, 1),9) # generate random values
print(f"The list is {values}")
target = int(input("Enter value to search : "))
result = linear_search(values, target)
if result != -1:
    print(f"Item {values[result]} found at index {result}")
else:
    print("Not found")
