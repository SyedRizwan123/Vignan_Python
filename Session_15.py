#Armstrong number:An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits. Specifically, 
#for a three-digit number like 153:, 1634, 92727
"""num=int(input("Enter a number"))   #153, #15, #1, #0
temp=num  #153
Arm=0  #27, 152, 153
while num!=0:  #153!=0, 15!=0, 1!=0, 0!=0(False)
    rem=num%10  #3, 5, 1
    Arm=Arm+rem*rem*rem*rem*rem   #0+3*3*3=27,   27+5*5*5=152, 152+1*1*1=153
    num=num//10  #15, 1, 0

print(Arm)
if Arm==temp:    #10==153
    print("The Given number is Armstrong")
else:
    print("The Given number is not Armstrong")"""
    
#153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, 1741725
"""num = int(input("Enter any value: "))  
temp = num
Arm = 0
count = 0  #4

# Count number of digits
n = num    #1634, 163, 16, 1, 0
while n != 0:   #1634!=0,, 163!=0, 16!=0, 1!=0, 0!=0
    count += 1  # Increment count for each digit found in the number 
    n //= 10   #163, 16, 1, 0

# Compute sum of digits raised to count (power)
n = num   # Reset n to original number
while n != 0:
    rem = n % 10
    Arm= Arm + rem ** count   # use count as exponent
    n //= 10

print(f"The sum of digits^{count} = {Arm}")

if temp == Arm:
    print("Given number is an Armstrong number")
else:
    print("Given number is not an Armstrong number")"""
    
#Find the factorial number of given value
# To find factorial value
n = int(input("Enter any value: "))  #5
fact = 1   #1, 2, 6, 24, 120
i = 1   #2, 3,4,5, 6

while i <= n:     #1<=5, 2<=5, 3<=5, 4<=5, 5<=5, 6<=5(false)
    fact = fact * i     #fact=1*1=1, fact=1*2=2, fact=2*3=6, fact=6*4=24, fact=24*5=120 
    i = i + 1    #i=1+1=2, i=2+1=3, i=3+1=4, i=4+1=5, i=5+1=6
print(fact)  

