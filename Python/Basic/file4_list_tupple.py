'''
### list
a = [1, 'anusha', 3, 4.0, 5]

print(a)  # to print the whole list

print(a[0])  # to print first element

print(a[::2])  # to print skipping 1 element

print(a[:4])  # to print up to 4th position

print("length of list: ", len(a))  # to print length of string

# to add the element
a.append('ram') # to add the element at last in the existing list
print(a)
a.insert(1, 'love') # to insert at the required position
print(a)

# to delete a element
b = a.pop()  #  to delete the last element of the list
print("removed string", b)
print("new list is", a)

c = a.pop(3)  # to removed the element of the required position
print("removed string", c)
print("new list is", a)

a.remove(4.0)  # to delete by giving element data
print(a)

del a[1:3]  # to delete  in a range from 1 to 3
print(a)


a = [1, 2, 3, 4, 5]
a.reverse()  # to reverse the list element
print("new list : ", a)

b=[1, 3, 4, 2, 5]
b.sort()  # to sort the list in ascending order
print("new list", b)

b.append(["hello", "world"]) # to add data as a  different list in that list
print(b)

b.extend(["hello", "world"])  # to add data as a  different elements in the list
print(b)

## tuples
# tuples value cannot be changed where list value can be changed

tup = (1, [7, 8, 9], 3, 4, 5)
print("list of tupple: ", tup)

print(tup.index(3))  #  to know the position of element in array

 tup [0] = 2 # this method does not work because we can not change the value of tupple

print(tup[1][1]) # to print 8 we have to follow this method [1] it means that 2nd element of tupple 
                 # [1] [1] means 2nd element ko  list ko second element

print(tup.count(4))  # to know how much time 4 is occured in  tupple


## list comprehensions : makes easy to create a list

list = [letter for letter in range(10) if letter%2==0] # to add data in list if it is odd number
print(list)



'''


