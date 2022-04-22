'''

# string formatting


a = "ramkarki"
b = len(a)
print("total length of a is : " + str(b))

c = a.upper() # to print the letter in capital letter
print("upper letter  " + str(c))

d = a.lower()  # to print the letter in small letter
print("lower letter " + str(d))

a = "ramkarki"
e = a.swapcase()  # to reverse the letter i.e. id input is small output is capital and vice versa
print(" swap of the word is " + str(e))

w = "ramram123"
f = w.isalpha()  # to check given string only contain alphabet or not
print(" given string is only alphabet ", f)

g = a.isalnum()  # to check string contains number or string or both
print(" string contains number or alphabet", g)

z = "123456"
h = z.isdigit()  # to check string contains number on;y or not
print("it contains number only ", h)

w = "ramram123"
i = w.replace("a", "u")
print(" the replaced letter of ramram123 is :  ", i)

a = "ramkarki"
j = a.index('k')  # to find the position of k
print(" the position of k in string", i)

la = " happy "
k = la.strip()  # to remove the white space before and after string
l = la.lstrip()  # to remove the left side white space 
m = la.rstrip()  # to remove the right side white space
print(" white strip is removed", k)

sen = " helllo madam how are you "
n = sen.split()  # to spliting the sen in different element and show them as array ; it is done according space
# sen = " helllo madam, how, are you "
# n = sen.split(,)  # split according to ,
print(" the splited words of string sen is : ", n)



age = 24 

print("My age is " + str(age) + " years")
print(" there are {0} days in {1} , {2}, {3}, {4}, {5}, {6} and {7} ".format(31, "january", "March", "May", "july", "August", "October", "December"))

print(""" january: {2}
february: {0}
march: {2}
april: {1}
""".format(28, 30, 31))

print("my age is %d years" % age)
print("my age is %d %s, %d %s" % (age, "years", 6, "months"))

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))  # i**2 = i square and i ** 3 = i cube
    # %2d and %4d gives the space before the integer

'''

## string format

x = 'ram'
y = 'karki'

z = 'My name is {} and my cast is {}. '.format(x, y)  # put variable serailly which you need first and last
print(z)

k = 'My cast is {1} and my name is {0} '.format(x, y)  # we can give indexing from 0 so that we can put variable at any place
print(k)