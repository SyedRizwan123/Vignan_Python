#Find the second largest element in a list
# List of numbers
"""numbers = [12, 45, 67, 89, 34]
# Sort the list in ascending order (smallest → largest)
numbers.sort()  # After sorting: [12, 34, 45, 67, 89]
print(numbers[-2])"""

"""numbers = [12, 45, 67, 89, 34]

largest = numbers[0]   #12
second = numbers[0]    #12

for i in numbers:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second largest:", second)"""

#Check if a list is a palindrome
"""list1 = [1, 2, 3,2,1]

if list1 == list1[::-1]:   #[1,2,3,2,1] ==[1,2,3,2,1]
    print("The given list is Palindrome")
else:
    print("The given list is not palindrome")"""
    
#Find the common elements between two lists
"""list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = []   #4,5
for x in list1: #x=1, x=2, x=3, x=4, x=5           # check each element in list1
    if x in list2:
        common.append(x)
print(common)"""

#Find all even numbers from a list
"""numbers = [10, 15, 20, 25, 30]
even=[]
for i in numbers:
    if i%2==0:
        even.append(i)
print(even)"""

#print vowels from a list of characters
"""cities = ["hyderabad", "mumbai", "Banglore", "Kolkata", "chennai"]
vowels = "aeiouAEIOU"   # include uppercase vowels also
for city in cities:   #city="hyderabad"            # loop through each city
    print("City:", city)
    for ch in city:   #city="hyderabad" ch='h', ch='y', ch='d',ch='e'
        if ch in vowels:          # if character is a vowel
            print(ch, end=" ")    # print vowel
    print()"""

#Two sum problem"
"""You are given an array of integers nums and an integer target.
Write a Python program to find two numbers in the array 
such that they add up to the given target."""
# Example Input
"""nums = [2, 7, 11, 15]          # A list (array) of integers.
target = 17                   # The sum we want two numbers from nums to add up to.

# Solution using loops
for i in range(len(nums)):     # Outer loop: i will take every index from 0 to len(nums)-1.
                                # Here: i goes 0, 1, 2, 3.
    for j in range(i + 1, len(nums)):   # Inner loop: j starts from the next index after i (i+1)
                                            # to avoid using the same element twice and to avoid duplicate pairs.
                                            # For i=0 → j: 1,2,3 ; for i=1 → j: 2,3 ; etc.
        # Check if the numbers at positions i and j add up to the target.
        if nums[i] + nums[j] == target: # Compare the sum of the two chosen elements with target.
            print([i, j])"""            # If equal, print the pair of indices as the answer.
                                                # (Problem expects indices, not the values.)
        
#Built-in Python Sorting
#sort()
#sorts the original list (modifies it).
#does not return any value (returns none)
#used only with lists
#syntax: list.sort()
"""nums=[5,2,8,1]
#nums.sort()
nums.sort(reverse=True)
print(nums)"""

#sorted
#Returns a new sorted list
#does not modify the orginal list
#can be used with any iterable(list,tuple,string, etc..)
#syntx:sorted(iterable)
"""nums=[5,2,8,1]
new_num=sorted(nums)
print("newlist",new_num)
print(nums)"""

nums=[5,2,8,1]
new_num=sorted(nums, reverse=True)
print("newlist",new_num)
print(nums)