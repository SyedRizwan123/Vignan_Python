#loops
"""for number in range(0,11):    #0 t0 10    number=0, number=1, number=2, number=4..... number=10, number=11    11-1=10
    print(number)"""    #0, 1, 2
    
"""for number in range(0,10,3):    #number=0, number =3, number=6, number=9
    print(number)"""
    
"""for number in range(5,-1,-1):  #number=5-1, number=4-1, number=3-1, number=2-1, number=1-1, number=0
    print(number)"""    #5,4,3,2,1,0
    
#looping list
"""my_list=[1,2,3,4, "python","is","neat"] #7, item=1, item=2, item=3, item=4
                        #item='python', item='is', item='neat'
for item in my_list:
    print(item)"""

#Break statement
"""my_list=[1,2,3,4, "python","is","neat"] #7, item=1, item=2, item=3, item=4
                        #item='python', item='is', item='neat'
for item in my_list:
    if item=="python":  #1=="python", 2=="python", "python"=="python"
        break
    print(item)"""   #1,2,3,4
    
"""my_list=[1,2,3,4, "python","is","neat"]
for item in my_list:
    if item=="python":
        continue
    print(item)"""
    
"""number = 1  #2,3, 4
while number <= 3:   #1<=3 , 2<=3, 3<=3, 4<=3
    print(number)    #1, 2, 3
    number = number + 1"""
    

"""x=10  #9,8
while x>=0:
   print(x)   #10,9,8
   x-=1 """      #x=x-1, x=9, x=9-1=8, x=8-1=7 




#nested loop
for i in range(1, 4):   #i=1, i=2, i=3
    for j in range(1, 4):  #j=1, j=2,j=3
        print(i * j, end="  ")    #1*1=1, 1*2=2, 1*3=3, 2*1=2, 2*2=4, 2*3=6
                                  #3*1=3, 3*2=6, 3*3=9
    print()  # new line after inner loop"""