'''

file = open('E:\\my_own_notes\\python notes\\file_filehandling.txt')

content = file.read()
print(content)
print(content)
#print(file.read(4)) # to read 4 character


file.seek(0) # to bring the cursor at front
print(file.read())

# to read line by line 
content = file.readlines()
print(content)

# to read single line
content = file.readline()
print(content)

''
r = read
w = write
r+ = read
w+ = create file and write
a = to add content in the file ''

with open('E:\\my_own_notes\\python notes\\file_filehandling.txt', mode='a') as file: # after writing file will be close auto

   file.write('helllo baby how are you?')
  
file = open('E:\\my_own_notes\\python notes\\file_filehandling.txt', mode='r')
print(file.read())
'''