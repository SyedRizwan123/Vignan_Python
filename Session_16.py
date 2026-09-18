#To find given number is Strong number or not
#Strong number:A Strong number is a number where the sum of the factorials of its digits equals the number itself.
# //ex:145: find factorial with each digit 1!+4!+5!=145 we have to get same digit
"""num = int(input("Enter a number: "))   #145, 14
sum = 0    # sum is used to store the sum of the factorials of the digits.
temp = num #temp stores the original number for comparison later.  145

while num:          #145
    i = 1
    fact = 1 #1,2,6, 24, 120
    r = num % 10 # Extract the last digit  r=145%10=5
    while i <= r:    # Calculate factorial of the digit  #1<=5, 2<=5, 3<=5, 4<=5, 5<=5, 6<=5
            fact = fact * i        #fact=1*1=1 fact=1*2=2, fact=2*3=6 fact=6*4=24, fact=24*5=120
            i += 1      #i=1+1=2, 2+1=3, 3+1=4, 4+1=5, 5+1=6
    sum = sum + fact  # Add factorial to sum     #sum=0+120=120
    num = num // 10   # Remove the last digit    #num=145/10=14

if sum == temp:
    print(sum,"is a strong number")
else:
    print(sum,"is not a strong number")"""
    
# perfect number: A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).
# 6=1+2+3 =6 6 devisors is 1+2+3=6
"""num = int(input("Enter a number: "))   #6
sum = 0  #6
for i in range(1, num):  # num=5,  i=1, i=2, i=3, i=4, i=5
    if num % i == 0:      #6%1==0, 6%2==0, 6%3==0, 6%4==0, 6%5==0
        sum += i     #sum=0+1=1, sum=1+2=3, sum=3+3=6
if sum == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")"""


#print even nubers and odd numbers
"""n=4
if n%2==0:
    print("Even number")
    
for i in range(1, 11):  #1,2,3,4,5,6,,7,8,9,10
    if i % 2 == 0:     #1%2==1,  2%2==0, 3%2==0, 4%2==0
        print(i, "= even")    #2 =even, 4 =even 
    else:
        print(i, "= odd")"""   #1 =odd, 3=odd

"""for i in range(0, 11, 2):
    if i % 2 == 0:
        print(i, "= even")
    else:
        print(i, "= odd")"""


#print 2nd table
n = int(input("Enter a number: "))     #2 * 1= 2*1=2,  2*2=4 2*3=6 2*4=8
for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")
