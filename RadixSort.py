Here is a detailed implementation of **Radix Sort** in Python using **Counting Sort** as the subroutine to sort numbers based on individual digits:

```python
# Function to perform Counting Sort on the array based on a specific digit
def counting_sort(arr, exp):
    n = len(arr)
    
    # Output array to store sorted numbers
    output = [0] * n
    
    # Count array to store the count of occurrences of digits (0-9)
    count = [0] * 10
    
    # Store the count of occurrences of each digit in the given place (exp)
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # Modify the count array to get the actual positions of the digits
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array using the count array (sorting based on the current digit)
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    # Copy the sorted output array to the original array
    for i in range(n):
        arr[i] = output[i]

# Function to perform Radix Sort
def radix_sort(arr):
    # Find the maximum number in the array to determine the number of digits
    max_num = max(arr)
    
    # Perform Counting Sort for each digit, starting from the least significant digit
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Example usage
if __name__ == "__main__":
    # Input array
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original array:", arr)
    
    # Perform Radix Sort
    radix_sort(arr)
    
    # Output the sorted array
    print("Sorted array:", arr)
```

### Explanation of the Code:
1. **counting_sort(arr, exp)**: This function sorts the array based on the digit at the position specified by `exp` (1 for units place, 10 for tens place, etc.).
   - **count array** stores the frequency of each digit (0 to 9).
   - The **output array** is built based on the counts, ensuring a stable sort for the current digit.

2. **radix_sort(arr)**: This function manages the whole sorting process.
   - It finds the maximum number in the array to determine how many digits it has.
   - It then calls **counting_sort** repeatedly for each digit, starting from the least significant digit.

### Output Example:
```bash
Original array: [170, 45, 75, 90, 802, 24, 2, 66]
Sorted array: [2, 24, 45, 66, 75, 90, 170, 802]
```

This code efficiently sorts the array using Radix Sort.
