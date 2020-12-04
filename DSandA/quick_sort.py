 
def quick_sort(arr):
    
    arr_len = len(arr)

    if arr_len <= 1:
        return arr

    pivot = 0

    for i in range(1, arr_len):
        if arr[i] <= arr[0]:
            pivot += 1
            arr[i], arr[pivot] = arr[pivot], arr[i]

    arr[0], arr[pivot] = arr[pivot], arr[0]

    smaller = quick_sort(arr[0:pivot])
    larger = quick_sort(arr[pivot + 1:arr_len])

    arr = smaller + [arr[pivot]] + larger

    return arr

array = [8, 3, 1, 7, 0, 10, 2]

print("Original Array: ",array)
print("Sorted Array: ",quick_sort(array))



