# 1. Count Letters
# Write a function called unique_english_letters that takes the string word as a parameter. The function should return the total number of unique letters in the string. Uppercase and lowercase letters should be counted as different letters.
# We’ve given you a list of every uppercase and lower case letter in the English alphabet. It will be helpful to include that list in your function.
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def unique_english_letters(word):
    unique_letters = ""
    count = 0
    for letter in letters:
        if letter in word and letter not in unique_letters:
            unique_letters += letter
    # return len(unique_letters)
    for item in unique_letters:
        count += 1
    return count

print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4


# 2. Count X
# Write a function named count_char_x that takes a string named word and a single character named x as parameters. The function should return the number of times x appears in word.
def count_char_x(word, x):
    return word.count(x)

print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1


# 3. Count Multi X
# Write a function named count_multi_char_x that takes a string named word and a string named x. This function should do the same thing as the count_char_x function you just wrote - it should return the number of times x appears in word. However, this time, make sure your function works when x is multiple characters long.
# For example, count_multi_char_x("Mississippi", "iss") should return 2
# count() function is handy, but using split() function is another approach
def count_multi_char_x(word, x):
    return len(word.split(x)) - 1

print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1


# 4.Substring Between
# Write a function named substring_between_letters that takes a string named word, a single character named start, and another character named end. This function should return the substring between the first occurrence of start and end in word. If start or end are not in word, the function should return word.
# For example, substring_between_letters("apple", "p", "e") should return "pl".
def substring_between_letters(word, start, end):
    if start not in word or end not in word:
        return word
    return word[word.find(start)+1 : word.find(end)]

print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"



# 5. X Length
# Create a function called x_length_words that takes a string named sentence and an integer named x as parameters. This function should return True if every word in sentence has a length greater than or equal to x.
def x_length_words(sentence, x):
    for word in sentence.split():
        return len(word) >= x

print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True


# 6. Check Name
# Write a function called check_for_name that takes two strings as parameters named sentence and name. The function should return True if name appears in sentence in all lowercase letters, all uppercase letters, or with any mix of uppercase and lowercase letters. The function should return False otherwise.
# For example, the following three calls should all return True:
# check_for_name("My name is Jamie", "Jamie")
# check_for_name("My name is jamie", "Jamie")
# check_for_name("My name is JAMIE", "Jamie")
def check_for_name(sentence, name):
    return name.lower() in sentence.lower()

print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False


# 7. Every Other Letter
# Create a function named every_other_letter that takes a string named word as a parameter. The function should return a string containing every other letter in word.
def every_other_letter(word):
    #return word[::2]
    new_word = ''
    for index in range(len(word)):
        if index % 2 == 0:  # index starts from 0, 0 is the first character, we need it
            new_word += word[index]
    return new_word

print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 


# 8. Reverse
# Write a function named reverse_string that has a string named word as a parameter. The function should return word in reverse.
def reverse_string(word):
    # return word[::-1]  # >>> shorted solution
    # first split the string:
    str_split = []
    temp_str = ''
    for char in word:
        if char == " ": # check if char is a space
            str_split.append(temp_str) # append an empty string in str_split
            temp_str = '' # and make sure the temp_str is empty
        else:
            temp_str += char # add every char into the empty string
    if temp_str:  # if the temp_str is not empty
        str_split.append(temp_str)
    
    # second, reversed str_split
    reversed_list = []
    for index in range(len(str_split) - 1, -1, -1):
        reversed_list.append(str_split[index])
       
    # reverse each item in reversed_list
    new_list = []
    for word in reversed_list:
        word_list = []
        for i in range(len(word) - 1, -1, -1):
            word_list.append(word[i])
        new_list.append(word_list)
    
    # join the characters 
    reversed_string = ""
    for item in new_list:
        space_str = " "
        single_word = ''
        for char in item:
            single_word += char
        reversed_string += single_word + space_str
    return reversed_string[:len(reversed_string)-1]
    # @@@ To Do
    # there will be a space at the end of the reversed_string, strip it off
    # str_len = len(reversed_string)
    # final_string = ""
    # index = 0
    # if str_len == 0:
    #     return final_string
    # else:
    #     while str_len >= len(final_string) and reversed_string[str_len-1] == " ":
    #         final_string += reversed_string[index]
    #         index += 1
    #         str_len -= 1
    # return final_string

print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print


# 9. Make Spoonerism
# A Spoonerism is an error in speech when the first syllables of two words are switched. For example, a Spoonerism is made when someone says “Belly Jeans” instead of “Jelly Beans”.
# Write a function called make_spoonerism that takes two strings as parameters named word1 and word2. Finding the first syllable of a word is a difficult task, so for our function, we’re going to switch the first letters of each word. Return the two new words as a single string separated by a space.
def make_spoonerism(word1, word2):
    return word2[0] + word1[1:] + " " + word1[0] + word2[1:]

print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a


# 10. Add Exclamation
# Create a function named add_exclamation that has one parameter named word. This function should add exclamation points to the end of word until word is 20 characters long. If word is already at least 20 characters long, just return word.
def add_exclamation(word):
    if len(word) >= 20:
        return word
    else:
        while len(word) < 20:
            word = word + "!"
    return word

print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
