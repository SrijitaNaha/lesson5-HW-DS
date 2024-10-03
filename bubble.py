def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage:
arr = [5, 2, 8, 3, 1, 6, 4]
arr = bubble_sort_descending(arr)
print(arr)  