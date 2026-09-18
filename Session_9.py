#Tuples():Tuples are immutable sequance, typically used to store collections of heterogenious (mixed_list = [1, "two", 3.0, True]  # A list with elements of different data types is heterogeneous.
#data, or for cases where an immutable sequnce of homogeniuos data is needed
#declaring empty tuple
"""tuple1= ()
print(type(tuple1))
print("tuple1:", tuple1,len(tuple1))"""

#single element tuple must have a traling comma
"""tuple3=(1,)      #tuple3=(1) will throw a syntax error
print("tuple3:", tuple3, len(tuple3))"""

#tuple operations: Limited since unlike list, tuple are immutable
"""tuple4=(1,2,3)
print("tuple4:", tuple4, len(tuple4))"""

#you can index tuple just like lists
"""tuple4=(1,2,3)
print("tuple4:", tuple4[0])
print("tuple4:", tuple4[1])
print("tuple4:", tuple4[2])"""

#You can slice tuples just like lists
"""tuple4=(1,2,3)
print("tuple4:", tuple4[0:2], tuple4[0:3])"""    #1,2

#You can also nest tuples like lists
"""tuple5=(1,2,3),(4,5,6)
#tuple5=(1,2,3)+(4,5,6)
print("tuple5:", tuple5, len(tuple5))
print("tuple5[1][2]:", tuple5[1][1])"""

#converted into List
"""my_tuple=(1,2,3,4,5)
print(my_tuple)
print("Before convert", type(my_tuple))

my_list=list(my_tuple)
print(my_list)
print("after convert",type(my_list))"""

"""a,b,c = 10,20,30
print(b)"""

#tuple packing and unpacking
#tuple packing and unpacking is a way to assign multiple values to multiple variables in a single statement

#tuple packing
"""tuple7= 1,2,3   #(1,2,3)
print("tuple7:", tuple7, len(tuple7))

#tuple unpacking
x,y,z=tuple7
print("tuple unpacking:",z)"""

#set:set is a data structure a set is a collection of unique items, with the structural implementation of the set not allowing duplicate values a set is defined by curly braces{}
"""set1={1,2,3}
print(type(set1))
print(set1)"""


"""tuple=(1,1,2,3)
print(tuple)"""

#Add an element
"""we can add an element to an existing set by using the add function . The resulting set will ensure uniquness of the added value within the set. 
An add operation modifies the original set """
"""set1={1,2,3}
#set1.add(4)
set1.add(2)
print(set1)"""

#Find element:
"""We can search a set to see if a specified element is present within the set.
This can be done using the in 'keyword'""" 
"""set1={1,2,3}
contains2 = 2 in set1   #True
contains4 = 4 in set1   #False
print("contain2:", contains2)
print("contain4:", contains4)"""

