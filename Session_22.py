"""text="banana"      #[('a',3), ('b',1),('n',2)]
count={}
for ch in text:       # ch='b', ch='a', ch='n', ch='a', ch='n', ch='a'
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1
items=sorted(count.items())
print(items)"""

#find longest word
"""text='python programming is easy'
longest=''   #longest='python', longest='programming'
for word in text.split():    #['python', 'programming','is','easy']
    if len(word) > len(longest):   #11>6, 2>11, 4>11
        longest=word

print(longest)"""

#Find the largest and smallest element in a list
"""numbers = [12, 45, 67, 2, 89, 34]
print("Largest:", max(numbers))
print("Smallest:", min(numbers))"""

#Find the largest and smallest element in a list without using built-in functions
"""numbers = [12, 45, 67, 2, 89, 34]
largest = numbers[0]   #89
smallest = numbers[0]  #2
for num in numbers:                #num=12,num=45,num=67,num=2,num=89,num=34
    if num > largest:  #45>12, 67>45, 2>67, 89>67, 34>89
        largest = num
    elif num < smallest:   #2<12, 34<2
        smallest = num
print("Largest:", largest)
print("Smallest:", smallest)"""

#Reverse a list without using built-in reverse()
"""numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]
print("Reversed:", reversed_list)"""

#Find the sum and average of list elements
"""Marks = [78, 90, 67, 80, 87, 95]
total_marks = sum(Marks)  #78+90+67+80+87+95=
avg_marks= total_marks / len(Marks)     # 497/6
print(total_marks)
print(avg_marks)"""

#Remove duplicates from a list
"""numbers = [1, 2, 2, 3, 4, 4, 5]
unique = []   #[1,2]
for num in numbers:    #num=1, num=2, num=2, num=3, num=4, num=4, num=5
    if num not in unique:   # check if element already exists
        unique.append(num)
print(unique)"""

#Find the second largest element in a list
numbers = [12, 45, 67, 89, 34]