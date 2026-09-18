#Remove an element
"""We can remove an element from a set by using the remove function.
A remove operation modifies the original set""" 
"""set1={1,2,3}
set1.remove(2)
print(set1)"""

"""We cannot attempt to remove an nonexistent element from the set. The operation will
return in 'keyerror' if the specified element to be removed is not found within the set"""
"""set1 = {1,2,3}
set1.remove(4)
print(set1)"""


"""To prevent an accidental 'KeyError', we can always check to see if the element is present within the 
set or not before attempting a delete operation"""
#if condition
"""set1={1,2,3}
if 4 in set1:
    set1.remove(4)
print(set1)"""

#pop element
"""We can pop out a randomm element from the set. This is usually done when to iterate over
the set to fully consume it. What we mean by consume is, we don't want the value we popped to be present within the set;
and we will continue to do so unit the set is empty"""
"""my_set = {5,2,1,4,3}
popped_element = my_set.pop()
print(popped_element)
print(my_set)"""

# A pop operation will result in a 'KeyError' if invoked on an empty set
"""set1 = {1}
print(set1.pop())
set1.pop()"""

#union
#We can create a union of 2 sets, which creates a new set containing unique elements found across both the sets
"""set1={1,2,3}
set2={2,3,4}
set3=set1.union(set2)
print("union:", set3)"""

#A union can also be performed using pipe operator
"""set1 = {1,2,3}
set2 = {2,3,4}
set3=set1 | set2
print(set3)"""

#intersection
"""One can performm an intersection operation on sets. This results in a set that contains elements
which are present in both sets. Let us take the same example as before, but this time we will do an intersection operation"""
"""set1={1,2,3}
set2={2,3,4}
set3= set1.intersection(set2)
print(set3)"""

#intersection can also be performed by using '&' operator
"""set1 = {1,2,3}
set2 = {2,3,4}
set3=set1 & set2
print(set3)"""
#Both set1.intersection(set2) and set1 & set2 do exactly the same thing 


#list[]--> Homogenious and heterogenious -->[1,2,3], ["syed","ravi"]
#tuple()-->(1,2,3), 
#set={1,2,3,4}

#Dictionories: Collection of key-value pairs     --> name:"Ravi" -->item
"""my_empty_dict={} #we have to define dictionory with {}   #alternative: my_empty_dict=dict()
print(f"dict:{my_empty_dict},type:{type(my_empty_dict)}")"""

#initilization: How we Define
dict1={"value1":1.6, "value2":10, "name":"Syed"}
dict2= dict(value1=1.6, value2=11, name="Syed")
dict3={"value1":1.6, "value2":10, "name":"Syed", "1":"Vnurture"}  # we should not use predifine command like 'list'

"""print(dict1)
print(dict2)
print(dict3)

print(f"equals: {dict1==dict2}")
print(f"lenght: {len(dict1)}")"""

#dict.keys(), dict.values(), dict.items()
"""print(f"keys: {dict1.keys()}")
print(f"values:{dict1.values()}")
print(f"items:{dict1.items()}")"""

#Accessing and setting values
#Setting the values
my_dict={}   #create a new dictionory
my_dict["key1"] = 10
my_dict["key2"] = 20
my_dict["key3"] = 30
my_dict["key1"] = 40     # #overriding existing value


print(my_dict)

#Accessing values:
"""print(f"value of key1: {my_dict['key1']}")
print(f"value of key3:{my_dict['key3']}")"""

#Accessing a noneexistent key will raise "KeyError" ):
#print(my_dict['key4'])

#Deleting a key-value pair: del dict[key]
"""my_dictn={"key1":"value1","key2":99, "keyx":"valuex"}
del my_dictn["keyx"]
print(my_dictn)"""

