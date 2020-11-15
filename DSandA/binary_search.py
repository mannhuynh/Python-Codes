"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value): 
    low = 0
    high = len(input_array) - 1
    mid = 0
  
    while low <= high: 
        mid = (high + low) // 2
         
        if input_array[mid] < value: 
            low = mid + 1
  
        elif input_array[mid] > value: 
            high = mid - 1
  
        else: 
            return mid 
  
    return -1
  
  
# Test array 
test_list = [1,3,9,11,15,19,29]
test_val1 = 25              
test_val2 = 15
print(binary_search(test_list, test_val1))  # -1 - return -1 since 25 is not in the list
print(binary_search(test_list, test_val2))  # 4 - return 4 since 15 has index of 4 in the list
