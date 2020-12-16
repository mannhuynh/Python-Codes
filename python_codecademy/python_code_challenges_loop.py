

# 1. Divisible by Ten
# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.
# Return the count of how many numbers in the list are divisible by 10.
def divisible_by_ten(nums):
    count = 0
    for num in nums:
        if num % 10 == 0:
            count += 1
    return count

print(divisible_by_ten([20, 25, 30, 35, 40]))


# 2. Greetings
# Create a function named add_greetings() which takes a list of strings named names as a parameter.
# In the function, create an empty list that will contain each greeting. Add the string "Hello, " in front of each name in names and append the greeting to the list.
# Return the new list containing the greetings.
def add_greetings(names):
    # greeting = ["Hello, " + name for name in names]
    return ["Hello, " + name for name in names]

print(add_greetings(["Owen", "Max", "Sophie"]))


# 3. Delete Starting Even Numbers
# Write a function called delete_starting_evens() that has a parameter named lst.
# The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.
# For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].
# Make sure your function works even if every element in the list is even!
# HINTS: Use a while loop to check two things. First, check if the list has at least one element, using len(lst). Second, check to see if the first element is even using mod (%). If both of those are True, slice off the first element of the list using lst = lst[1:].
def delete_starting_evens(lst):
    while len(lst) >= 1 and lst[0] % 2 == 0:
        lst = lst[1:]
    return lst


### Below solution is not correct as it will remove all even numbers ###
# def delete_starting_evens(lst):
#     new_lst = []
#     for number in lst:
#         if number % 2 != 0 and len(lst) >= 1:
#             new_lst.append(number)
#         else:
#             continue
#     return new_lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


# 4. Odd Indices
# Create a function named odd_indices() that has one parameter named lst.
# The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.
# For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].
def odd_indices(lst):
    return [lst[i] for i in range(len(lst)) if i % 2 != 0]

print(odd_indices([4, 3, 7, 10, 11, -2]))


# 5. Exponents
# Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to every number in powers.
# For example, consider the following code.
# exponents([2, 3, 4], [1, 2, 3])
# the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. It would first add two to the first. Then two to the second. Then two to the third, and so on.
def exponents(bases, powers):
    # return [bases[i]**powers[i] for i in range(len(bases))]
    exponents = []
    for i in bases:
        for j in powers:
            exponents.append(i**j)
    return exponents

print(exponents([2, 3, 4], [1, 2, 3]))

# 6. Larger Sum
# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.
# The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.
#sum() function is a good replacement for the loop
def larger_sum(lst1, lst2):
    sum1, sum2 = 0, 0
    for i in lst1:
        sum1 +=  i
    for j in lst2:
        sum2 += j
    if sum1 < sum2:
        return lst2
    return lst1
print(larger_sum([1, 9, 5], [2, 3, 7]))


# 7. Over 9000
# Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.
# The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.
# For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.
def over_nine_thousand(lst):
    sum_9000 = 0
    counter = 0
    while sum_9000 <= 9000 and counter < len(lst):
        if len(lst) == 0:
            return 0
        sum_9000 += lst[counter]
        counter += 1
    return sum_9000

### FOR LOOP ###
# def over_nine_thousand(lst):
#   sum9000 = 0
#   for i in range(len(lst)):
#     if len(lst) < 1:
#       return 0
#     elif sum9000 <= 9000:
#       sum9000 += lst[i]
#   return sum9000

print(over_nine_thousand([8000, 900, 120, 5000]))
print(over_nine_thousand([]))
print(over_nine_thousand([800, 90, 12, 500]))


# 8. Max Num
# Create a function named max_num() that takes a list of numbers named nums as a parameter.
# The function should return the largest number in nums
# return max(nums) is a good choise
def max_num(nums):
    max_number = nums[0] # create a variable that hold the first element in the list as a current number
    for i in range(len(nums)):
        if nums[i] >= max_number:
            max_number = nums[i]  # if there is a number bigger than current number, assign that number into current number
    return max_number

print(max_num([50, -10, 0, 75, 20]))


# 9. Same Values
# Write a function named same_values() that takes two lists of numbers of equal size as parameters.
# The function should return a list of the indices where the values were equal in lst1 and lst2.
# For example, the following code should return [0, 2, 3]
# same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])
def same_values(lst1, lst2):
    index_lst = []
    for index in range(len(lst1)):
        if lst1[index] == lst2[index]:
            index_lst.append(index)
    return index_lst

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


# 10. Reversed List
# Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.
# The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.
# For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.
# reversed() function is the best choice
def reversed_list(lst1, lst2):
    # return list(reversed(lst1)) == lst2
    temp_lst = []
    for i in lst1[::-1]:
        temp_lst.append(i)
    return temp_lst == lst2

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
