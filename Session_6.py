"""print(" 'Hello Vignan' ")    #'Hello Vignan'

print(" \"Hello Vignan\" ")# "Hello Vignan" """

#print("i'm Learning Python. \
#And we are starting with the print statement.")

#here i given multiple print statements then i want to print in signle line we have to use "end='..'"
"""print("we'll first learn how to print.",end='')
print("Then we'll learn how to comment code.")"""

#string formating:In Python, string formatting is the process of creating a formatted string by embedding variables or values within a text string. This allows you to create dynamic strings that incorporate variable values, making your code more readable and flexible.
"""name="Ram"
age=25
print("my name is ",name, "i am ",age,"years old")"""

#using '%' operator: This  % operator used to insert values into a string.
"""name = "Syed"
age = 25
formatted_string ="my name is %s and I am %d years old" %(name, age)
print(formatted_string)"""

#Using '.format(): This .format() method to format strings. It allows for more flexibility in terms of the order of variables and additional formatting options.
"""name = "Raju"
age = 25
formatted_string = "my name is {} and i am {} years old".format(name,age)
print(formatted_string)"""

#Using f-strings (Formatted String Literals):  f-strings are a concise and readable way to format strings. They allow you to embed expressions directly within string literals by using curly braces {}
"""name = "Zareena"
age = 22
formatted_string = f"my name is {name} and i am {age} years old"
print(formatted_string)"""

#String Operations: 
#string can be concatenated using + 
"""fname="Syed"
lname="Rizwan"
number =10
print(fname)  #Syed
print(lname)  #Rizwan
print(fname+lname)"""
#print(fname+number)   #String+interger

# string can be counted from the left using +ve indices, starting with 0
"""word = "python"
print(word[2])

#string can be counted fromm the right using -ve indices,starting with -1
print(word[-2])"""

#slicing
# - string can be sliced with [startIndex:endIndex]
# - startIndex is included and endIndex is excluded
# - startIndex must be < endIndex, else empty string is returned
# - if a slice index is out of range, python will go as far as it can

word="python"  #p-->0, y-->1, t-->2, h-->3, o-->4, n-->5
print(word[0:3])  #pyt
print(word[0:10])
print(word[-3:-1])
name = "python"
print(name[-1:-3:-1])   # prints "no"
print(word[-3:-6])
print(word[:2])
print(word[4:])


