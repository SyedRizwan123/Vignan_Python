# Define the two tuples
"""t1 = (1, 2, 3)
t2 = (4, 5, 6)
# Concatenate the two tuples using the '+' operator
concatenated_tuple = t1 + t2
# Print the original tuples and the result
print(f"Original tuple t1: {t1}")
print(f"Original tuple t2: {t2}")
print(f"The concatenated tuple is: {concatenated_tuple}")"""

#Repeating Elements: Given colors = ("red", "blue"),repeat it 3 times using *.
# Define the original tuple with colors
"""colors = ("red ", " blue")
# Repeat the tuple 3 times using the * operator.
# The result is a new tuple with the original elements repeated in sequence.
#repeated_colors = colors * 3

repeated_element = colors[0] * 3
# Print the original and the new, repeated tuple to show the result.
print(f"Original tuple: {colors}")
#print(f"Repeated tuple: {repeated_colors}")
print(f"Repeated tuple: {repeated_element}")"""

# Define the tuple of numbers
"""nums = (1, 2, 3, 2, 4, 2, 5)
# Find the index of the first occurrence of 3 using the .index() method
# This method returns the index of the first matching item.
index_of_3 = nums.index(3)

# Count how many times 2 occurs using the .count() method
# This method returns the total number of occurrences of an item in the tuple.
count_of_2 = nums.count(2)
# Print the results
print(f"The index of the first occurrence of 3rd index is: {index_of_3}")
print(f"The number of times 2 occurs is: {count_of_2}")"""


# Define the nested tuple
"""nested = (1, (2, 3), (4, (5, 6)))
print(len(nested))  # Output: 3

# Access and print the number 3
# The first index, 1, selects the inner tuple (2, 3).
# The second index, 1, selects the element 3 from that inner tuple.
print("Accessing 3:", nested[1][1])
# Access and print the number 6
# The first index, 2, selects the inner tuple (4, (5, 6)).
# The second index, 1, selects the nested tuple (5, 6).
# The third index, 1, selects the element 6 from that deepest tuple.
print("Accessing 6:", nested[2][1][1])"""

#Check Membership
"""animals = ("dog", "cat", "lion", "tiger")
# Check if "cat" exists in the tuple and store the boolean result in the variable 'is_cat_present'
is_cat_present = "cat" in animals

# Check if "elephant" exists in the tuple and store the boolean result in the variable 'is_elephant_present'
is_elephant_present = "elephant" in animals
# Print the result for "cat"
print(f"Is 'cat' present in the tuple? {is_cat_present}")
# Print the result for "cat"
print(f"Is 'elephant' present in the tuple? {is_elephant_present}")"""

#Tuple of Tuples Given students = (("Alice", 20), ("Bob", 22), ("Charlie", 19)), print all student names and ages.
#output: Alice is 20 years old, Bob is 22 years old, Charlie is 19 years old.
# Define the tuple of tuples containing student names and ages
"""students = (("Alice", 20), ("Bob", 22), ("Charlie", 19))
# Iterate through each student tuple in the students tuple
for student in students:
    # Unpack the student tuple into name and age variables
    name, age = student   # Unpacking the tuple into two variables name and age, output: Alice 20
    # Print the formatted string with the student's name and age
    print(f"{name} is {age} years old")"""
    

#Reversing a Tuple: Given nums = (10, 20, 30, 40, 50), reverse the tuple.
"""nums = (10, 20, 30, 40, 50)
# The [::-1] slicing syntax creates a reversed copy of the tuple.
reversed_nums = nums[::-1]
# Print the original and the reversed tuples to show the change.
print(f"Original tuple: {nums}")
print(f"Reversed tuple: {reversed_nums}")"""

#Count Word Occurrences in a Sentence using Dictionary"
# Define a string (sentence) in which we want to count word occurrences
"""sentence = "python is easy and python is powerful"
# Create an empty dictionary to store words as keys and their counts as values
word_count = {}   #{python:2, is:2, easy:1, and:1, powerful:1}
# Loop through each word in the sentence after splitting it by spaces
for word in sentence.split(): 
    # sentence.split() → splits the sentence into ['python', 'is', 'easy', 'and', 'python', 'is', 'powerful']
    # For each word, get its current count from the dictionary
    # If the word is not found, default value 0 is returned
    # Then we add 1 to the count
    word_count[word] = word_count.get(word, 0) + 1  # word_count.get(word, 0) fetches the current count of 'word' from 'word_count'.
    
Step 1: Understanding word_count.get(word, 0)
.get(key, default_value) is a dictionary method
It tries to get the value for the given key (word)
If the key exists, it returns its current value
If the key doesn't exist, it returns the default_value (0 in this case)

Step 2: The Complete Process
Get current count: word_count.get(word, 0)
Add 1: + 1
Store back: word_count[word] = ...
Let's Trace Through the Example
Sentence: "python is easy and python is powerful"
Words: ['python', 'is', 'easy', 'and', 'python', 'is', 'powerful']

Iteration 1: word = "python"
word_count.get("python", 0) → "python" not in dictionary → returns 0

0 + 1 → 1

word_count["python"] = 1

Dictionary becomes: {"python": 1}

Iteration 2: word = "is"
word_count.get("is", 0) → "is" not in dictionary → returns 0
0 + 1 → 1
word_count["is"] = 1
Dictionary becomes: {"python": 1, "is": 1}

Iteration 3: word = "easy"
word_count.get("easy", 0) → "easy" not in dictionary → returns 0

0 + 1 → 1
word_count["easy"] = 1
Dictionary becomes: {"python": 1, "is": 1, "easy": 1}

Iteration 4: word = "and"
word_count.get("and", 0) → "and" not in dictionary → returns 0

0 + 1 → 1
word_count["and"] = 1
Dictionary becomes: {"python": 1, "is": 1, "easy": 1, "and": 1}

Iteration 5: word = "python" (second occurrence)
word_count.get("python", 0) → "python" exists with value 1 → returns 1

1 + 1 → 2
word_count["python"] = 2
Dictionary becomes: {"python": 2, "is": 1, "easy": 1, "and": 1}

Iteration 6: word = "is" (second occurrence)
word_count.get("is", 0) → "is" exists with value 1 → returns 1

1 + 1 → 2
word_count["is"] = 2
Dictionary becomes: {"python": 2, "is": 2, "easy": 1, "and": 1}

Iteration 7: word = "powerful"
word_count.get("powerful", 0) → "powerful" not in dictionary → returns 0

0 + 1 → 1
word_count["powerful"] = 1
Final dictionary: {"python": 2, "is": 2, "easy": 1, "and": 1, "powerful": 1}

# Finally, print the dictionary containing each word and its occurrence count
print("Word Count:", word_count)"""
#Output: {'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}

# Find the Student with the Highest Marks
students = {"Ravi": 85, "Sneha": 92, "Amit": 78, "Priya": 95}






