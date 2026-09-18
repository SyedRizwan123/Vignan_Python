#Dictonary mutable
"""my_dict={"ham":"good", "carrot":"Semi good"}
my_other_dict = my_dict
#print(my_other_dict)

my_other_dict["carrot"] = "Super tasty"   #replace in semi good
#print(my_other_dict)

my_other_dict["sausage"]="best ever"     #cretaing a new key-value (item)
#print(my_other_dict)

print(f"{my_dict=}\n other:{my_other_dict}")
print(f"equals: {my_dict==my_other_dict}")"""

#dict.get: Returns none if key is not in dict. However, you can also specify default return value which will be returned if key is not present in the dict.
"""my_dict={"a":1, "b":2, "c":3}
#value_of_d= my_dict.get('d')
value_of_d = my_dict.get("d", "My name is Syed")
print(value_of_d)"""

# Create a dictionary using dict() constructor
# Keys = "food", "drink", "sport"
# Values = "ham", "beer", "football"
"""my_dict = dict(food="ham", drink="beer", sport="football")
# Print the dictionary before removing anything
print(f" {my_dict}")  
# Output: dict before pops: {'food': 'ham', 'drink': 'beer', 'sport': 'football'}

# pop("drink") removes the key "drink" from the dictionary
# It also returns the value associated with "drink" → "beer"
food = my_dict.pop("drink")
print(food)

print(my_dict)

# pop("food", "default value for food")
# → removes "food" key and returns its value ("ham")
# If "food" was NOT in the dictionary, it would return the default value instead
food_again = my_dict.pop("food", "default value for food")

print(f"food again: {food_again}") """ 
# Output: food again: ham

#dict.setdefault: its a one of the command
#Return the value of key defined as first parameter. if the key is not present in the dict, adds key with default value (second parameter)
"""my_dict={"a":1,"b":2,"c":3}
print(my_dict)
a=my_dict.setdefault("a","my default value")
d=my_dict.setdefault("d","my default value")
print(a)
print(d)"""

#dict.update: Merge two dicts  (its like append))
"""dict1={"a":1, "b":2,}
print("Before update",dict1)   #2
dict2={"c":3}
dict1.update(dict2)
print("After update",dict1) """   #3

#we can also give list values to key
good_dict={"mykey": ["python", "is","still", "cool"]}
print(good_dict)
