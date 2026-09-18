#print vowels in a given string
"""input_string = "Hello World!"      #aeiouAEIOU
vowels = "aeiouAEIOU"
vowel_count = 0
vowel_list = []   
for char in input_string:    #char='H',char='e'
    if char in vowels:          #if e in aeiouAEIOU
        vowel_list.append(char)
        vowel_count += 1
print("Vowels in the given string:", vowel_list)
print(f"Number of vowels in the given string: {vowel_count}")"""
    
# Program to reverse a string
"""input_string = "Python"
reversed_string = input_string[::-1]   # Using slicing to reverse the string
print("Reversed string:", reversed_string)"""

#loop through string ,Program to reverse a string
"""input_string = "Python"  # Input string to be reversed
reversed_string = ""   #P, yP,tyP, htyP,ohtyP, nohtyP     # Initialize an empty string to store the reversed string
# Loop through each character of the input string
# The loop iterates from the first character to the last
for char in input_string:    #char='P',char='y',char='t',char='h',char='o',char='n'
    reversed_string = char + reversed_string # # Prepend the character to the reversed string
                       #y+p=yP
                       #t+yP=tyP
                       #h+tyP=htyP
                       #o+htyP=ohtyP
                       #n+ohtyP=nohtyP
                       
    # This effectively builds the reversed string by adding each character to the front
print("Reversed string:", reversed_string)"""  # Output the reversed string

# Program to check if a string is a palindrome
"""input_string = input("Enter a string: ")  # Prompt the user to enter a string
if input_string == input_string[::-1]:    #madam==madam # Compare the string with its reverse
    print("Palindrome")
else:
    print("Not a palindrome")"""

# Program to check if a string is a palindrome through loop
"""input_string = "madam"   #0=m, 1=a,2=d,3=a,4=m
is_palindrome = True

# Initialize two pointers, one at the start and one at the end of the string
start_index = 0    #m   #1, 2
end_index = len(input_string) - 1   #5-1=4   #m,    4-1=3, 2

# Loop as long as the start pointer is less than the end pointer
while start_index < end_index: #The condition is 0 < 4, which is True. The loop starts. 
        #1<3 
        #2<2   
    # Compare the characters at the two pointers
    if input_string[start_index] != input_string[end_index]:  #This line becomes if input_string[0] != input_string[4]:. m!=m
    #The condition 'm' != 'm' is False. The code inside the if block is skipped.
    #The condition 'a'  !=  'a' is False    
    # If they don't match, it's not a palindrome
        is_palindrome = False
        break  # Exit the loop immediately
    
    # Move the pointers towards the center
    start_index += 1      #start_index becomes 0 + 1 = 1.,2
    end_index -= 1        #end_index becomes 4 - 1 = 3. 2
    #The loop condition is checked again: 1 < 3, which is True.
    #The condition is 2 < 2, which is False. The loop terminates. The code inside the while block is not executed.
# Print the result based on the final value of the flag
if is_palindrome:         #if is_palindrome: The condition is if True:, which is True.
    print("Palindrome")
else:
    print("Not a palindrome")"""

# Program to find the first non-repeating character in a string
"""input_string = "aabbcde"
for char in input_string:  #char='a',char='a', char='b', char='b',char='c',char='d', char='e',,
    if input_string.count(char) == 1:   #aabbcde.count('a')
        #The loop starts with char = 'a'. The condition input_string.count('a') == 1 is checked.
                #The count of 'a' in "aabbcde" is 2, so the condition is False. The loop continues to the next character.
                #Next, char = 'b'. The condition input_string.count('b') == 1 is checked.
                #The count of 'b' in "aabbcde" is 2, so the condition is False. The loop continues to the next character.
                #Next, char = 'c'. The condition input_string.count('c') == 1 is checked.
                #The count of 'c' in "aabbcde" is 1, so the condition is True. The code inside the if block is executed.
        print("First non-repeating character:", char)
        break"""

#How to print thr second non repeating character in a string
"""input_string = "aabbcde"
non_repeating_chars = [] #[c,d,e] # Initialize an empty list to store non-repeating characters
for char in input_string:
    if input_string.count(char) == 1:  # Check if the character appears only once in the string
        non_repeating_chars.append(char)  # Add the non-repeating character to the list
if len(non_repeating_chars) >= 2:  # Check if there are at least two non-repeating characters
    We want the second non-repeating character.
       The first non-repeating character is at index 0.
       The second non-repeating character is at index 1.
       To safely access index [1], we must have at least 2 elements in the list.
    print("Second non-repeating character:", non_repeating_chars[1])  # Print the second non-repeating character
else:
    print("There is no second non-repeating character.") 
    
# String Compression : String compression means reducing the size of a string by representing repeated characters in a shorter format.
input_string = "aaabbbcccaaa" """  #a3b3c3a3

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

