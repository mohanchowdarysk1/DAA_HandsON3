# Define the merge sort function
def Merge_Sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left_side = arr[:mid]
    right_side = arr[mid:]
    
    # Recursively apply merge sort to each half
    left_side = Merge_Sort(left_side)
    right_side = Merge_Sort(right_side)
    
    # Merge the sorted halves
    return Merge(left_side, right_side)

# Define the merge function
def Merge(left, right):
    Merged = []
    left_index, right_index = 0, 0
    
    # Merge the two arrays
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            Merged.append(left[left_index])
            left_index += 1
        else:
            Merged.append(right[right_index])
            right_index += 1
    
    # Append remaining elements from left or right subarray
    Merged.extend(left[left_index:])
    Merged.extend(right[right_index:])
    
    return Merged

# Test the merge sort function
if __name__ == "__main__":
    # Test array
    arr = [5, 2, 4, 7, 1, 3, 2, 6]
    
    # Perform merge sort
    sorted_arr = Merge_Sort(arr)
    
    # Print the sorted array
    print("Sorted array:", sorted_arr)
