def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key > arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr

# Example usage:
arr = [5, 2, 8, 3, 1, 6, 4]
arr = insertion_sort_descending(arr)
print("Sorted array in descending order:", arr)