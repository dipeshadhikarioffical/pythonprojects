'''
algo for the project of rolling dice :

1. develop random no.
2. check the number
3. show the face
4. looping

'''
import random

print(" this is a dice simulator: ")
x = "y"
while x == "y":
    number = random.randint(1, 6)
    if number == 1:
        print("===============")
        print("{           }")
        print("{      0     }")
        print("{           }")
        print("===============")

    if number == 2:
        print("===============")
        print("{      0     }")
        print("{            }")
        print("{      0     }")
        print("===============")

    if number == 3:
        print("===============")
        print("{      0     }")
        print("{      0     }")
        print("{      0     }")
        print("===============")
    
    if number == 4:
        print("===============")
        print("{  0      0   }")
        print("{             }")
        print("{  0      0   }")
        print("===============")

    if number == 5:
        print("================")
        print("{  0       0   }")
        print("{      0       }")
        print("{  0        0  }")
        print("================")

    if number == 6:
        print("===============")
        print("{   0     0   }")
        print("{   0     0   }")
        print("{   0     0   }")
        print("===============")
    
    x = input(" press 'y' to roll dice  or press 'n' to exit: ")
    if x == "n":
        exit;



