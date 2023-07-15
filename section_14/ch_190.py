# REGULAR EXPRESSIONS

'''
regular expressions are not exclusive to Python
python comes with a regular expression module 're'
'''

import re

pattern = re.compile('this')
string = 'Search this inside of this text, please!'

# # prints True since 'Search' shows up in string
# print('Search' in string)

# returns a match object
print(re.search('this', string))

a = re.search('this', string)

# shows where 'this' shows up in string
print(a.span())
print(a.start())
print(a.end())

# returns the part of the string where there was a match
print(a.group())

# will return None if you search for something that is not there
print(re.search('nothing', string))

# # throws error if you group(None)
# b = re.search('nothing', string)
# print(b.group())

# pattern defined at top
c = pattern.search(string)
d = pattern.findall(string)
e = pattern.fullmatch(string)
f = pattern.match(string)

print(c)
print(d)
print(e)
print(f)
