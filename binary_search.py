import random

def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = data[mid]

        if guess == target:
            return mid, low, mid, high  # return trace info

        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1, None, None, None

# Generate sorted list of random integers.
n = 20
max_val = 500 
data = [random.randint(1, max_val) for i in range(n)] 
data.sort() 
print("Data:", data)
target = int(input("Enter target value: "))
target_pos = binary_search(data, target)
target_pos, low, mid, high = binary_search(data, target)
if target_pos == -1:
    print("Your target value is not in the list.")
else:
    print(
        f"Your target value {target} has been found at index {target_pos} "
        f"(low={low}, mid={mid}, high={high})"
    )
