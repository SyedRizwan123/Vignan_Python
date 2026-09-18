"""What is the Problem?
we need to calculate an employee’s Gross Salary (GS) based on:Basic Salary (BS)

# Allowances:
HRA (House Rent Allowance) = 80% of BS
TA (Travel Allowance) = 40% of BS
DA (Dearness Allowance) = 30% of BS

# Mathematical Concept
HRA = 0.8 × Basic Salary  13000
TA = 0.4 × Basic Salary
DA = 0.3 × Basic Salary
Gross Salary = BS + HRA + TA + DA

# Simple Understanding
Basic salary is the main salary
Additional benefits (HRA, TA, DA) are calculated as percentages
Add all → get Gross Salary"""

# Program to calculate Gross Salary
# Take basic salary input from user
"""basic_salary = int(input("Enter basic salary: "))  #60000
# Calculate allowances based on percentage
hra = basic_salary * 0.8   # 80% of basic salary  48000
ta = basic_salary * 0.4    # 40% of basic salary  24000
da = basic_salary * 0.3    # 30% of basic salary  18000

# Calculate gross salary
gross_salary = basic_salary + hra + ta + da  #60000+48000+24000+18000=150000
# Display results
print("\nHRA (80%) =", hra)
print("TA (40%) =", ta)
print("DA (30%) =", da)
print("\nGross Salary =", gross_salary)"""

"""Problem Explanation: Simple Interest
What is the Problem?

You need to calculate Simple Interest (SI) based on:
Principal Amount (P)
Time (T) in years
Rate of Interest (R) in percentage
# Mathematical Concept
SI= P×T×R / 100
	
P → Principal (amount)
T → Time (years)
R → Rate (%)

# Simple Understanding
You invest some money (principal)
Bank gives interest based on:
time
rate
Formula calculates how much extra money you earn

# Steps to Solve
Take amount, time, rate as input
Apply formula → (P × T × R) / 100
Display the result"""
# Program to calculate Simple Interest

# Take input from user
# Convert values into integers
"""amount = int(input("Enter principal amount: "))    #100000
time = int(input("Enter time (in years): "))       #1
rate = int(input("Enter rate of interest (%): "))   #24

# Calculate simple interest using formula
simple_interest = (amount * time * rate) / 100

# Display result
print("\nRate of Interest =", rate, "%")
print("Simple Interest =", simple_interest)"""

# Program to swap two numbers using a third variable
# Take input from user
"""a = int(input("Enter value of a: "))  #10
b = int(input("Enter value of b: "))  #20

# Display values before swapping
print("\nBefore swapping a =", a, "b =", b)
# Swapping logic using third variable
temp = a   # store value of a in temp #temp=10
a = b      # assign value of b to a #a=20
b = temp   # assign value of temp (old a) to b
# Display values after swapping
print("After swapping a =", a, "b =", b)"""

# Program to swap two numbers without using a third variable
# Take input from user
"""a = int(input("Enter value of a: "))   #10
b = int(input("Enter value of b: "))    #20
a=a+b  # Step 1: a now holds the sum of a and b   10+20=30, a=30
b=a-b  # Step 2: b now holds the original value of a  30-20=10, b=10
a=a-b  # Step 3: a now holds the original value of b  30-10=20, a=20

a, b = b, a  # Swapping using tuple unpacking
print(a)
print(b)"""

# Program to calculate sum of N natural numbers   #5-->1+2+3+4+5=15
"""Problem Explanation: Sum of N Natural Numbers
What is the Problem?
we need to calculate the sum of first N natural numbers.

Natural numbers → 1, 2, 3, 4, ... , N
Example: If N = 5 → Sum = 1 + 2 + 3 + 4 + 5 = 15

#Mathematical Concept
S=n(n+1)/2  --5(5+1)/2-->  6/2=3*5=15
S → Sum of numbers
n → Number of terms

#Simple Understanding
--> Instead of adding numbers one by one
--> We use a direct formula to save time

#Steps to Solve
--> Take n value from user
--> Apply formula → n × (n + 1) / 2
--> Display the result"""

# Take input from user
"""n = int(input("Enter n value: "))   #5
# Calculate sum using formula
sum_n = (n * (n + 1)) // 2   # // for integer result
#n=5 then sum_n = (5 * (5 + 1)) // 2 = (5 * 6) // 2 = 30 // 2 = 15

# Display result
print("Sum of", n, "natural numbers is =", sum_n)"""


# Program to calculate sum of squares of N natural numbers
""" Problem Explanation: Sum of Squares of N Natural Numbers
# What is the Problem?
we need to calculate the sum of squares of first N natural numbers.

Example:
If N = 3
Sum = 1² + 2² + 3² = 1 + 4 + 9 = 14

Mathematical Concept

S=n(n+1)(2n+1)/6

--> S → Sum of squares
--> n → Number of terms

# Simple Understanding
--> Instead of calculating:1² + 2² + 3² + ... + n²
--> We use a direct formula to save time

#Steps to Solve
--> Take n value from user
--> Apply formula → n(n+1)(2n+1)/6
--> Display the result """

# Take input from user
"""n = int(input("Enter n value: "))   #3

# Calculate result using formula
result = (n * (n + 1) * (2 * n + 1)) // 6   # // gives integer result
# If n=3 then result = (3 * (3 + 1) * (2 * 3 + 1)) // 6
# = (3 * 4 * 7) // 6
# Display result
print("Sum of squares of", n, "is =", result)"""

# Program to calculate Volume of a Cylinder
""" Problem Explanation: Volume of a Cylinder
# What is the Problem?
we need to calculate the volume of a cylinder using:

--> Radius (r)
--> Height (h)

Mathematical Concept
Volume (V) of cylinder = πr²h 

V → Volume
r → Radius
h → Height
π (pi) → 3.1415

# Simple Understanding
--> A cylinder is like a pipe or water tank
--> Volume means how much space it can hold
--> Formula → π × r² × h 

# Steps to Solve
--> Take radius and height as input
--> Apply formula → π × r × r × height
--> Display the result """

# Program to calculate Volume of a Cylinder

# Define constant PI
PI = 3.1415

# Take input from user
radius = float(input("Enter radius: "))     # 3.0
height = float(input("Enter height: "))     # 5.0

# Calculate volume using formula: PI * r * r * h
volume = PI * radius **2 * height   # volume = 3.1415 * 3.0 * 3.0 * 5.0 = 141.3675
# Display the result
print("Volume of Cylinder:", volume)










