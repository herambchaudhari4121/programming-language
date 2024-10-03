Here's a simple example of a binary search algorithm in Python:

```python
# Binary Search Function
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if target is at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            low = mid + 1

        # If target is smaller, ignore the right half
        else:
            high = mid - 1

    # Target was not found in the array
    return -1

# Example usage
arr = [2, 5, 7, 11, 15, 18, 21, 25]
target = 15
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
```

### Explanation:
1. `low` and `high` represent the range of indices to search within.
2. The midpoint `mid` is calculated each time to check if it matches the `target`.
3. If the target is found, its index is returned.
4. If not, the search continues in the left or right half of the list until either the target is found or the list is exhausted.
