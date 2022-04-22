
'''
#  if statement

name = input("Please Enter  Your Name: ")
age = input("Please Enter Your Age " + name + "")
print(" Your name is "+ name + "and Your age is " + age)

if age >= '18':
  print(" You are able to give a vote")
else:
   print(" you are not able to give a vote")

# if and if else statement

print("Please guess a number between 1 to 10: ")
guess = int(input())

if guess < 5:
    print(" Please guess the higher number")
    guess = int(input())

    if guess == 5:
        print(" well done the number is correct ")

    else:
        print(" sorry you have not guessed the correct number ")

elif guess > 5:
    print(" please guess the lower")
    guess = int(input())

    if guess == 5:
        print(" well done the number is correct ")

    else:
        print(" sorry you have not guessed the correct number ")

else:
    print(" you got it in first time ")


name = input("Enter your Name: ")
age = int(input("Enter Your Age: "))

if age >= 18 and age <= 30:
    print(" Welcome to you in the holiday ...")
else:
    print(" Sorry you are not able to take this holiday offer ....")


##  for loop

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))
    # i**2 = i square and i ** 3 = i cube
    # %2d and %4d gives the space before the integer

for state in ["not pinin", "no more", "a stiff", "bereft of lift"]:
    print(" This parrot is  " + state)

for i in range(0, 50, 5):   # range(start, end, step)
    print(" i is {}".format(i))

# to create a table

for i in range(1, 13):
    for j in range(1, 13):
        print("{1} times {0} is {2}".format(i, j, i*j))
        
    print("===============")

######   while

i = 0
while i < 10:
    if(i == 5):
        break  #to break the condition means below it other code will not be executed
    #continue # to continue the further process
    #pass # it is used when we did not want to enter any statement
    print(i)
    i = i + 1
    
else:
    print(' loop is exited ')

### some other function and operators are:

## range

range(start, stop, step)

for i in range(0, 10):
    print(i)
print("=============")
for i in range(0, 10, 2):
    print(i)

for i in range(0, 10):
    result = list(range(0, 10))
    print(result)

string = "dipeshadhikari"
count = 0
for i, j in enumerate(string): # to print with index
    print(i,j)

## ZIP FUNCTION : to combines the two or more list
# it will only combine till both list have same number of value; if one has more then other then it will only make
# till both values are same

list1 = [1, 2, 3]
list2 = [4, 5, 6]

for j, i in zip(list1, list2):    
    print(j, i)
  

list1 = [1, 2, 3, 7, 8, 9]
list2 = [4, 5, 6]
for j, i in zip(list1, list2):
    print(j, i)


# IN OPERATOR:  to check element is in the list or not

print('x' in ['a', 'b', 'c', 'd'])

# MAX and MIN FUNCTION: to find out max and min value

list1 = list(range(10))
print(max(list1))
print(min(list1))

### random library: to generate random number

from random import shuffle
list1 = [1, 2, 3, 4, 5]
shuffle(list1)
print(list1)

from random import randint # to generate integer random number in between 0 to 100
num = randint(0, 100) 
print(num)

from random import random # to generate random decimal number in between 0 and 1 
num = random()
print(num)

## type function

a = int(input("number"))
print(type(a))

b = [1,2,3,4]  # list
c = (1,2,3,4)  #  tupple
d = {1,2,3,4}  # set
print(type(b))
print(type(c))
print(type(d))

'''