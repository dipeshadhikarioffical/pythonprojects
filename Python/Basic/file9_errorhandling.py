'''
def func(a, b):
    div = 0
    try:  # anything which can produce an error
        div = a / b
        return div
    except:  # handle the exception
        print("Exception caught")
    else:  # if no any error occur
        print("ALL is well ")
        return div
    finally: # this code run always either their is error or not
    print("always run")
   
    return False
a = int(input(" enter 1st num"))   
b = int(input(" enter 2nd num"))

div = func(a,b)
print("result", div) '''


