def iterative_binary_search_v2(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Calculate mid

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Move left pointer
        else:
            right = mid - 1  # Move right pointer

    return -1  # Target not found


# Example usage
if __name__ == "__main__":
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target_value = 7
    result = iterative_binary_search_v2(sorted_array, target_value)

    if result != -1:
        print(f"Element found at index: {result+1}")
    else:
        print("Element not found in the array.")
