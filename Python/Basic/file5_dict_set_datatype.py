'''
#######  dictonary

dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

print(dict['key2']) # if you append value in key which already has its value then it will replace that value

for x in dict: # to print keys using for loops or key only
print(x)

for x in dict.values():  # to print values only
print(x)

for x in dict.items():  # to print values and key both
print(x)

dict['key2'] = 10  # key must be unique
print(dict['key2'])

print(dict.items())  # to print whole dictionary

############   set
# we can store only unique value we cannot use same duplicate value


set = set()

set.add(1) # to add element in set
set.add(2)
set.add(2)  # same value cannot be added
print("set list",set)

#print(set[0]) it is not possible as it does not support indexing

set.pop()  # to delete the set element
print(set)

######  data type
### boolean value

a = 1 > 2
print(a)

b = 1 < 2
print(b)

a = 4
b = True
print(a == b)

c = None
print(c)


'''
