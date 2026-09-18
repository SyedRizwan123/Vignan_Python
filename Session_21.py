#Count vowels and consonants
# Program to count vowels and consonants in a string
"""input_string = "Hello, World!"
vowels = "aeiouAEIOU"
vowel_count = 0   #1
consonant_count = 0  #2
for char in input_string: #H,e,l,l,o,,, ,W,o,r,l,d,!
    if char.isalpha():    #Check if the character is an alphabet letter
        if char in vowels: #Check if the character is a vowel 
            #H in vowels? False, e in vowels? True
            vowel_count += 1   #Increment the vowel count
        else:
            #If the character is not a vowel, it must be a consonant H in vowels? False
            consonant_count += 1   #Increment the consonant count
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)"""


#Program to check if two strings are anagrams
"""An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once. 
For example, listen" and "silent" are anagrams because both use the same letters in a different order."""
"""str1 = "listen"
str2 = "silent"
# Sort both strings and compare
print(sorted(str1))  #['e', 'i', 'l', 'n', 's', 't']
print(sorted(str2))  #['e', 'i', 'l', 'n', 's', 't']
if sorted(str1) == sorted(str2):
    print("Anagrams")
else:
    print("Not anagrams")"""

# Program to remove all duplicate characters from a string
# Input string with duplicate characters
"""input_string = "programming"

# Initialize an empty string to store the result without duplicates
# This will be used to build the final string
result_string = ""
# Loop through each character of the input string
# For each character, we check if it's already in our result string
for char in input_string:
    # Check if the current character 'char' is NOT in 'result_string'
    # The 'in' operator efficiently checks for membership in a string.
    # It returns True if the character is found, and False otherwise.
    # We use 'not in' to only proceed if the character is new.
    if char not in result_string:
        # If the character is not a duplicate, add it to our result string
        # We are building a new string here, as strings are immutable.
        result_string += char   #result_string = result_string + char, 
        #result_string = "" + 'p' = "p", result_string = "p" + 'r' = "pr", result_string = "pr" + 'o' = "pro", result_string = "pro" + 'g' = "prog", result_string = "prog" + 'r' = "prog" (r is duplicate), result_string = "prog" + 'a' = "proga", result_string = "proga" + 'm' = "progam", result_string = "progam" + 'm' = "progam" (m is duplicate), result_string = "progam" + 'i' = "progami", result_string = "progami" + 'n' = "progamin", result_string = "progamin" + 'g' = "progamin" (g is duplicate)
# Print the final string with all duplicates removed
print("Original string:", input_string)  #programming
print("String after removing duplicates:", result_string)"""   #progamin     

#Program to print decending order
"""text="python"
# Assuming 'chars' is a list of characters, for example: chars = ['p', 'y', 't', 'h', 'o', 'n']
chars=list(text)
# Get the total number of elements in the list and store it in the variable 'n'.
n = len(chars) #6
# This is the outer loop. It controls the number of passes through the list.
# After each pass, one more element will be in its correct sorted position.
# It runs 'n' times to ensure every element is checked.
for i in range(n):
    # This is the inner loop. It performs the actual comparisons and swaps.
    # It iterates from the first element up to the last unsorted element.
    # The 'n-i-1' is an optimization: after 'i' passes, the last 'i' elements are already sorted,
    # so we don't need to compare them again.
    for j in range(0, n-i-1):   #6-0-1=5
        # Compare the current element with the next one.
        # For descending order, we check if the current element is LESS THAN the next one.
        # If it is, they are in the wrong order and need to be swapped.
        if chars[j] < chars[j+1]:
            # This is the swap. It swaps the positions of the two elements
            # using a concise Python feature called tuple unpacking.
            # The larger element "bubbles up" towards the beginning of the list.
            chars[j], chars[j+1] = chars[j+1], chars[j]
        

# After the loops are finished, the list 'chars' is sorted in descending order.
# The "".join(chars) method concatenates all characters in the list into a single string.
# Finally, print() displays the sorted string to the console.
# For example, if chars was ['p', 'y', 't', 'h', 'o', 'n'], it will print "ytponh".
print("".join(chars))"""

