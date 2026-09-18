#write a python program the given value is positive or negative
"""n=int(input("Enter a number: "))   #5, -2
if n>0:    #5>0, -2>0
    print("Positive number")
elif n<0:   #-2<0
    print("Negative number")
else:
    print("0")"""


#Sum of natural numbers
"""n = int(input("Enter a number: "))   #5
sum = 0   #1,3, 6, 10, 15
for i in range(1, n+1):    #i=1, i=2, i=3, i=4, i=5
    sum = sum+i   #sum=0+1=1, sum=1+2=3,sum=3+3=6, sum=6+4=10, sum=10+5=15
print(sum)"""

#Sum of natural numbers using while loop
"""n = int(input("Enter a number: "))   #5
sum = 0
i = 1  #2
while i <= n:   #1<=5, 2<=5, 3<=5, 4<=5, 5<=5, 6<=5
    sum =sum+i   #sum=0+1=1,
    i+=1   #i=1+1=2
print(sum)"""

#print ASCII values
"""for i in range(65, 91):
    print(f"{chr(i)}={i}")"""

"""for i in range(97, 123):
    print(f"{chr(i)}={i}")"""
    
#Find the given is prime number or not
#prime number: Prime: if its only divisible by one and then its self     1*3=3,3*1=3   1*4=4,4*1=4,2*2=4   1*6=6,2*3=6,6*1=6   1*5=5,5*1=5                                     
"""n=int (input("Enter a number: "))   #3, 4
count=0  #1, 2
for i in range(1, n + 1):    #range(1, n+1): Generates a sequence of numbers from 1 to n (inclusive)
    if n % i == 0:        #3%1==0,  3%2==0(false)  3%3==0
        count +=1    #count=0+1=1, #count=1+1=2
if count==2:
    print("The Given number is a prime number")
else:
    print("The Given number is not a prime number")"""
    
"""n=int (input("Enter a number: "))   #3, 4
count=0  #1, 2
for i in range(1, n + 1):    #range(1, n+1): Generates a sequence of numbers from 1 to n (inclusive)
    if n % i == 0:        #3%1==0,  3%2==0(false)  3%3==0
        count +=1    #count=0+1=1, #count=1+1=2
if count==2:
    print("The Given number is a prime number")
else:

    print("The Given number is not a prime number")
    new = n + 1
    while True:
        count = 0
        for i in range(1,new+1):
            if new%i==0:
                count+=1
        if count==2:
            print("the next prime num is: ",new)
            break
        new+= 1"""

#Find the given is prime number or not
#prime number: Prime: if its only divisible by one and then its self     1*3=3,3*1=3   1*4=4,4*1=4,2*2=4   1*6=6,2*3=6,6*1=6   1*5=5,5*1=5                                     

"""prime = int(input("Enter the number: "))
count = 0

# Check if the input number is prime
for i in range(1, prime + 1):
    if prime % i == 0:
        count += 1

if count == 2:
    print(prime, "is a prime number")
else:
    # If the number is not prime, find the next prime number
    prime += 1  # Start checking from the next number
    while True:
        count = 0  # Reset count for the new number
        for i in range(1, prime + 1):
            if prime % i == 0:
                count += 1
        if count == 2:  # Check if the current number is prime
            print("The next prime number is:", prime)
            break
        prime += 1  # Move to the next number"""

# Prompt the user to input the number of terms they want in the Fibonacci series
#Fibonacci series: it is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. 
# The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.
"""n = int(input("Enter the number of terms: "))  #10
# Initialize the first two numbers of the Fibonacci series
first = 0  #1, 1, 2,3,5,8,13,21
second = 1  #1, 2,3,5,8,13,21,34
# Print the first two numbers of the Fibonacci series
print("Fibonacci Series:", first, ",", second, end=", ")
# Loop to generate and print the remaining terms of the Fibonacci series
for i in range(2, n):    #10 i=2, i=3, i=4, i=5, i=6,i=7, i=8, i=9
    # Calculate the next term in the Fibonacci series
    next_term = first + second    #0+1=1, 1+1=2, 1+2=3, 2+3=5, 3+5=8, 5+8=13, 
    #8+13=21, 13+21=34
    # Print the next term of the Fibonacci series
    print(next_term, end=", ")
    # Update the values of 'first' and 'second' for the next iteration
    first = second    #1, 1,2, 3,5,8,13, 21
    second = next_term #1, 2,3,5, 8, 13,21, 34
# Print a newline character to end the output
print()"""
    
#Pattern programs
"""for r in range(4):       #rows
    for c in range (6):  #columns
        print("*", end="")
    print()"""

#Left Triangle Star Pattern
"""for i in range(1, 7):  #i=1, i=2 ,i=3
    for j in range(1, 7):
        if j <= i:  #1<=3(True), 2<=3(True), 3<=3(True), 4<=3(False)
            print("* ", end="")
        else:
            print(" ", end="")
    print()"""

"""n = 5
for i in range(1, n+1):
    print("* " * i)"""
    
#Inverted Left Triangle Pattern
n = 5   # Step 1: Assign the value 5 to variable 'n'. 
        # This means the pattern will have 5 rows.
# Step 2: Loop starts from 'n' down to 1, with step -1 (decreasing order).
for i in range(n, 0, -1):
    # Step 3: For each row, print '* ' repeated 'i' times.
    print("* " * i)   #"* "*5= * * * * *
    
