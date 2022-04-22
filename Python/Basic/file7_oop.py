

### class

class Bird:
    def __init__(self, color, wingspan):  # color, wings are data member
      self.color = color
      self.wingspan = wingspan
      # printing using class
      print("printing using class",self.wingspan)
      print("printing using class",self.color)

bird  = Bird('blue', wingspan = 10)   # Bird = name of class ||||  bird = name of object
# printing using object
print("printing using object", bird.wingspan)

print("printing using object",bird.color)
'''
class Rectangle:
    type = 'quadrilateral'
    def __init__(self, length, breadth=10):
        self.length = length
        self.breadth = breadth
        self.area = 0
        
    
    def get_area(self):
        self.area =  self.length * self.breadth

    def get_perimeter(self):
        return 2 * (self.length + self.breadth)


rect = Rectangle(20, 10)

area = rect.get_area()
print("area",area)

perimeter = rect.get_perimeter()
print("perimeter", perimeter)

def update_length(self, new_length):
    self.length = new_length

## 1st object
rect = Rectangle(20)
rect.get_area()
print(rect.area)

## 2nd object
rect2 = Rectangle(50)
rect2.get_area()
print(rect2.area)

### inheritance

class Quadrilateral:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        print("quadrilateral is created ")

    def get_type(self):
        return 'Qualilateral'

class Rectangle(Quadrilateral):  # using inheritance to bring the attribute of Quadrilaterals
    def __init__(self,length,breadth):
        Quadrilateral.__init__(self, length, breadth)
        print("rectangle is created ")

    def get_area(self):
        return self.length * self.breadth


class Square(Quadrilateral):  # using inheritance to bring the attribute of Quadrilaterals
    def __init__(self, length, breadth):
        self.length = self.breadth
        print("square is created ")

    def get_area(self):
        return self.length * self.breadth

    

rect = Rectangle(100, 50)
area = rect.get_area()
print("rectangle area", area)
print(rect.get_type())

square = Rectangle(100, 100)
area = square.get_area()
print("square area", area)


## polymorphism

class kali:
    def advantage(self):
        print("more power ful")

    def disadvantage(self):
        print("resource intensive")

class parrot:
    def advantage(self):
        print(" cute bird ")

    def disadvantage(self):
        print("small community")

kali = kali()
parrot = parrot()

for object in [kali, parrot]:
    print(type(object))
    object.advantage()
    object.disadvantage()

#### magic method

a = [1, 2, 3, 4, 5]
b = 'dipesh'
print(len(a))
print(len(b)) 

class Student:
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name
    ## to use built in function
    def __str__(seif): #magic method
        return "class str is called"

    def __len__(self):
        return len(self.name)
student = Student(12, 'ram')
print(str(student)) 


### privacy

class Private:
    def __init__(self, a, b):
        self._a = a
        self.b = b
        print(" private class is created")
        # self.__a = a # we can use double underscore to make private
        # but there is no any privacy in the python it can also be used using another function
    def sum(self):
        return self._a + self.b

priv = Private(10, 20)
print(priv._a)
    

    '''