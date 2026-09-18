"""word="pyhton"
word[0] = 'P'
print(word)""" 

"""word="pyhton"
newword= 'J' + word[0:]
print(newword)"""

"""word = "python"
new_word=word[0] + word[5]   #p+n=pn
print(new_word)"""

#print(len('python'))
#print('python'.find('t')) #find index of substring in string
#print('python'.startswith('p'))  # check string starts with substring
#print('python'.endswith('o'))    # check string ends with substring
#print('PYTHON'.lower())
#print('python'.upper())
#print('a'.isalpha())  #True
#print('abc123'.isalnum())  #True
#print('2'.isdigit())  #True #check if all characters in the string are digits
#print('syed'.capitalize())  #Syed
#print('  python  '.strip())  #python
#print("syed rizwan".title())   #Syed Rizwan If you want each word’s first letter capitalized, use .title():
#print("Syed".count('S'))
#print(' \"p y t h o n\" ' .strip())  #The strip() method in Python is used to remove leading and trailing whitespace (or specific characters) from a string.
#print('python is very easy'.split())  #the split() method in Python is used to split a string into a list of substrings based on a specified delimiter. By default, it splits the string at whitespace characters (spaces, tabs, newlines). In this case, the string 'python is very easy' is split into a list of words: ['python', 'is', 'very', 'easy'].

#.join() method in Python is used to concatenate a list or iterable of strings into a single string, with a specified separator between each element.
words = ["Python", "is", "fun"]  #3
print(words)
sentence = "@".join(words)   # join with a @ symbol
print(sentence)