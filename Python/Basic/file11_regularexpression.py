'''

import re  # to import regular expression

text = "hello i am dipesh > my full name is dipesh adhikari "

# to search the number of occurance of string 'dipesh'
''
match = re.search("dipesh", text)
if re.search('dipesh', text):
    print("match is found")
else:
    print("match is not found")


print("found at character ", match.start())

print(re.split('>', text))
#print(text.split('>'))

out = re.findall('dipesh', text)  # to show how much time 'dipesh' word comes in text string
print(out) 


text = "a......ab......abb......abbb.......aabbb"
out = re.findall('ab{2}', text)  #  ab{2} means single a and 2 b's must come 
print(out)  

### character sets

text = "this is a sample paragraph. do you like paragliding. no i like  paras ball"
out = re.findall('[pa]+', text)  # [pa]+  means that either 'a' or 'p' or 'pa' should come
print(out)

res = re.findall('para[sg]+', text)  # 'para[sg]+' means that after para , 's' or 'g' or 'sg' must come
print(res)


text = " hey boy,  you wann a play football with me? i want to play"
rest = re.findall('[^!,.]+', text)  # to print with out '!'  ',' '.'  mark to remove any thing you have to write after this symbol '^'. 
print(rest)

resu = re.findall('[^!,. ]+', text) # after !,. mark space is given to remove the space
print(resu)
''

## ranges..

text = " hey boy,   YOU wann a Play football 2 time with me? i want to play"

rest = re.findall('[a-z]+', text)  # to find lower case
print("rest", rest)

rest1 = re.findall('[A-Z]+', text)  # to find upper case
print("rest1", rest1)

rest2 = re.findall('[0-9]+', text)  # to find number
print("rest2", rest2)

rest3 = re.findall('[A-Z][a-z]+', text)  # to  find 1st letter capital and 2nd letter small
print("rest3", rest3)

rest4 = re.findall('[A-Za-z]+', text)  # to find capital and small means all
print("rest4", rest4)

'''