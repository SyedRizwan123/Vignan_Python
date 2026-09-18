#count of number digits
"""num = int(input("Enter a number: "))  #1234,  123, 12, 1, 0
count = 0  #4
while num != 0:       #1234 !=0, 123!=0  12!=0, 1!=0, 0!=0
    num = num // 10     #1234//10=123, 123//10=12, 12//10=1, num=0
    count += 1          #count=count+1, 0+1=1, 1+1=2 , 2+1=3, 3+1=4

print(count)"""

#Find the ASCII value of a given character
"""ch = input("Enter a character: ")   #a-97 to z-122,  A-65 to Z-90
ascii_value = ord(ch) #97   #ord() function is used to find the ASCII value of the character.
print(ascii_value)"""

#Find the given charecter is Alphabet or not     #a to z A to Z
"""ch = input("Enter a character: ")   #b

if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
    print(f"{ch} is an alphabet")
else:
    print(f"{ch} is not an alphabet")"""
    
"""ch = input("Enter a character: ")   #@
if ch.isdigit():  # Check if the input consists of digits only
    print(f"{ch} is a number")
elif len(ch) == 1:  # Check if the input is a single character
    if ch == '@':      #if @==#@$%&
        print(f"{ch} is the '@' symbol")
    elif 'a' <= ch <= 'z':
            print(f"{ch} is a small letter")
    elif 'A' <= ch <= 'Z':
            print(f"{ch} is a capital letter")
    else:
        print(f"{ch} is a special character")
else:
    print(f"{ch} invalid")"""
    
#Write a Python program elegible for vote or not
"""age = int(input("Enter age: "))   #18, 17
gend = input("Enter gender (M/F): ").upper()  #F  # Convert to uppercase for case-insensitive comparison

if gend == 'F':                 #F==F
    if age >= 18:             #19>=18
        print("Female and eligible to vote")
    else:
        print("Female and not eligible to vote")
elif gend == 'M':
    if age >= 18:
        print("Male and eligible to vote")
    else:
        print("Male and not eligible to vote")
else:
    if age >= 18:
        print("None and eligible to vote")
    else:
        print("None and not eligible to vote")"""

#write a python program the given number is palindrome or not      
#Palidrome : A palindrome is a word, number, or sequence of characters that reads the same forward and backward ex:121
num = int(input("Enter a number")) #121        #num=12       #num=1, num=0
temp=num   #121
rev=0   #1, 12, 121
while num != 0:     #121 !=0, 12!=0, 1!=0, 0!=0
    rem = num % 10         #rem=121%10=1 rem=1, 12%10=2, rem=1
    rev = rev * 10 + rem   #rev=0*10+1=1, 1*10+2=12, 12*10+1= 121
    num=num//10     #12, 1, 0

print("reverse value is", rev)
if temp==rev:     #121 == 121
    print("The given number is Palindrome" )
else:
    print("The Given number is not a palindrome")












