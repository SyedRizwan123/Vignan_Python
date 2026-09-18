#List: List are mutable sequance, typically used to store collections of homogenious items
# Lists are represented by comma-separated items within square brackets []

listpeople = ["tom","harry","jane","liz"]   #tom-->0, harry-->1, jane-->2, liz-->3
"""print(type(listpeople))
print(listpeople)"""

listflowers = ["rose","lily","tulip","jasmine"]
listpets = ["cat","turtle","goat","dog"]
listnumfriends = [21,33,10,51]

#List of heterogenious items are not incorrect, just atypical
"""listAtypical = [1,'cat',0x43,567.55]       #0x45 UTF-8 ENCODING FOR 69
print(listAtypical)"""

#concatenate lists
"""listCon= listpeople + listflowers
print(listCon)"""

#Length of lists
#print("length position->",len(listpeople))

"""print(listpeople[0])  #tom
print(listpeople[2])
print(listpeople[-2])"""

#slice list with [startindex:endindex]
#print("listpeople[2:]->", listpeople[1:3])   #-->1,2

#unlike strings, Lists are mutable
#assign to an index, we can update a value
"""print("Original",listpets)   #["cat","turtle","goat","dog"] -->cat-->0, turtle-->1,goat-->2,dog-->3
listpets[0]='t-rex'
print("After Update", listpets)"""

#Assign to a slice
"""listpets[0:2] =['python','elephant']
print(listpets)"""

#delete a slice
"""listpets[2:4]=[]
print(listpets)"""

#append new items to list
"""listpets.append('fox')    #["cat","turtle","goat","dog"]
print(listpets)"""

#clear a list by assignment to an empty list
"""listpets[:]=[]
print(listpets)"""

#nested list
"""nestedlist=[listpeople,listflowers]
print(nestedlist)
print("nestedlist[0]:",nestedlist[0])
print("nestedlist[1]:",nestedlist[1])
print("nestedlist[1][2]:",nestedlist[1][2])"""

#lists with integers
list1=[100,200,300]
list2=[5,15,25]
list3=[10,50,50,20,0,10,50]

list1.append(-400)   #Add an item to the end of the list. equalent to list
print("list1 Append:",list1)

list2.extend(list1)  #Extend the list2 by appending all the time in list1.
print("list2extend:", list2)

list2.remove(-400)  #Remove the first item from list2 whose value is -400.
print("list2 Remove Element:",list2)

del list2[2]       #Remove the item at index[2]
print("delete list2[6]:", list2)

list2.pop()       #Remove and returns the last item in the list
print("list2 pop():", list2)

print("Index of an element:", list3.index(10)) #[10,50,50,20,0,10,50] Returns the index in list3 of element position

print(list3.count(50))   # the number of times 50 appears in list

list3.reverse()    #Reverse the items of list3 in place
print("list3 Reverse:", list3)


list3.sort()      #Sort the items of list3 in place
print("list3 sorted:",list3)

list3.clear()      #Remove all items from the list
print("list3 clear:",list3)

"""del list3        #Delete the list
print("delete list3:")
print(list3)"""

txt = "Syed" [::-1]
print(txt)