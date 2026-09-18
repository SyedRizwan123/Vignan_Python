#print("Hello World")

"""statement =True
if statement:
    print("Hello Python")"""
    
"""x=10
y=20
if x<=y:    #10<=20
    print("True")"""
    
"""x=10
y=20
if x>=y:    #10>=20
    print("True")
else:
    print("false")"""

#elif
"""val = 88
if val >= 100:   #88>=100
    print("value is equal or greater than 100")
elif val > 10:    #88>10
    print("value is greater than 10 but less than 100")
elif val < 0:
    print("value is less than 0")
else:
    print("value is equal or less than 10")"""


#nested if
"""num = 15
if num >= 0:   #15>=0
    if num == 0:   #15==0
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")"""
    
#write a python program to find given year is leap year or not
year = int(input("Enter a year"))
if (year%4==0 and year%100!=0) or year%400==0:    #F  or  T
    print("The given year is leap year")
else:
    print("The given year is not a leap year")