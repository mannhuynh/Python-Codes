# 1. Sum Values
# Write a function named sum_values that takes a dictionary named my_dictionary as a parameter. The function should return the sum of the values of the dictionary
def sum_values(my_dictionary):
    total = 0
    for value in my_dictionary.values():
        total += value
    return total

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6


# 2. Even Keys
# Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, as a parameter. This function should return the sum of the values of all even keys.
def sum_even_keys(my_dictionary):
    total = 0
    for key, value in my_dictionary.items():
        if key % 2 == 0:
            total += value
    return total

print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6


# 3. Add Ten
# Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. The function should add 10 to every value in my_dictionary and return my_dictionary
def add_ten(my_dictionary):
    for key, value in my_dictionary.items():
        my_dictionary[key] = value + 10
    return my_dictionary

print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}


# 4. Values That Are Keys
# Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. This function should return a list of all values in the dictionary that are also keys.
def values_that_are_keys(my_dictionary):
    lst = []
    for value in my_dictionary.values():
        if value in my_dictionary.keys():
            lst.append(value)
    return lst

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]


# 5. Largest Value
# Write a function named max_key that takes a dictionary named my_dictionary as a parameter. The function should return the key associated with the largest value in the dictionary.
def  max_key(my_dictionary):
    current_key = ""
    current_value = 0
    for key, value in my_dictionary.items():
        if current_value <= value:
            current_value = value
            current_key = key
    return current_key

print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"


# 6. Word Length Dict
# Write a function named word_length_dictionary that takes a list of strings named words as a parameter. The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.
def word_length_dictionary(words):
    new_dict = {}
    for word in words:
        new_dict.update({word: len(word)})
    return new_dict

print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}


# 7. Frequency Count
# Write a function named frequency_dictionary that takes a list of elements named words as a parameter. The function should return a dictionary containing the frequency of each element in words.
def frequency_dictionary(words):
    new_dict = {}
    for word in words:
        new_dict[word] = words.count(word)
    return new_dict

print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}


# 8. Unique Values
# Create a function named unique_values that takes a dictionary named my_dictionary as a parameter. The function should return the number of unique values in the dictionary.
def unique_values(my_dictionary):
    value_lst = []
    count = 0 
    for item in list(my_dictionary.values()):
        if item not in value_lst:
            value_lst.append(item)
    print(value_lst)
    return len(value_lst)

print(unique_values({0:2, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1


# 9. Count First Letter
# Create a function named count_first_letter that takes a dictionary named names as a parameter. names should be a dictionary where the key is a last name and the value is a list of first names. For example, the dictionary might look like this:
# names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
# The function should return a new dictionary where each key is the first letter of a last name, and the value is the number of people whose last name begins with that letter.
# So in example above, the function would return:
# {"S" : 4, "L": 3}
def count_first_letter(names):
    new_dict = {}
    for key, value in names.items():
        first_letter = key[0]
        if first_letter not in new_dict:
            new_dict[first_letter] = len(value)
        else:
            new_dict[first_letter] += len(value)        
    return new_dict

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
