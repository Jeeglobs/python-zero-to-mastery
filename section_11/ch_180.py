# USEFUL MODULES

from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 7, 7]

# Counter creates a dictionary of how many times each item occurs in an iterable
print(Counter(li))

sentence = 'this is a sentence'
print(Counter(sentence))

dictionary = {
    'a': 1,
    'b': 2,
}
print(dictionary['a'])

# throws error b/c there is no key 'c'
# print(dictionary['c'])

# avoids error by assigning default value int
new_dictionary = defaultdict(int,
                             {
                                 'a': 1,
                                 'b': 2,
                             }
                             )

print(new_dictionary['c'])

# OrderedDict saves the order of the k/v pairs
d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d2 == d1)


'''
In the current version of Python,
dictionaries ARE ordered by default
you only need to use OrderedDict
if you are using older versions of Python
'''
