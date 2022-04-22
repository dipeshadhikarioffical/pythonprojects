'''

def func(name = 'hari'): # here hari is the default value
    print("hello", name)

func('ram')

## to check prime number or not using a function

def check_prime(num):
    flag = 0
    for i in range(2, num):
        if (num % i == 0):
            flag = 1
            break
    if (flag == 0):
        return True
    else:
        return False
result = check_prime(int(input(" enter a number: ")))
print(result)

# if we don't know how much user will give the number but we have to show the addition of all inputs
#func(10, 20, 30) it is wrong because we have only 2 variable


def func(**kwargs): #  kwargs is a variable and * is necessary
    print(kwargs)
    
func(surname='rai', name='sita')

def function(*sample, **dummy):
    print(sample)
    print(dummy)

function(10, 20, 30, food='apple')

### map function
#  map(function, iterable)

def cube(num):
    return num ** 3  
print(cube(3))

list1 = [1, 2, 3]
for i in map(cube, list1):
    print(i)

### filter function
#   filter(function, iterable)


def even(num):
    return num % 2 == 0
    
list2 = [1, 2, 3, 4, 5, 6]
print(list(filter(even, list2)))

## lamba function
list2 = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x:x**3, list2)))


x = lambda a, b: a + b
print(x(10, 20))  

## nested function


x = 100   #GLOBAL 

def sample(x):  #ENCLOSING FUNCTION
    
   
   
    def cube(): # LOCAL SCOPE
        print(x**3)
    cube()

    x = 200  # LOCAL ASSIGNMENT
    return  x
x = sample(x)
print("in global", x)

#   L : local scope
#   E  : Enclosing function
#   G  : global scope
#   B : Built in
#


'''