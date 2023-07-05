# SET & DICTIONARY COMPREHENSION

# sets work the same as lists
my_set = {char for char in 'hello'}
my_set2 = {num for num in range(0, 100)}
my_set3 = {num ** 2 for num in range(0, 100)}
my_set4 = {num ** 2 for num in range(0, 100) if num % 2 == 0}

print(my_set)
print(my_set2)
print(my_set3)
print(my_set4)


# dictionaries
simple_dict = {
    'a': 1,
    'b': 2,
}

my_dict = {key: value ** 2 for key, value in simple_dict.items()}
my_dict2 = {key: value ** 2 for key,
            value in simple_dict.items() if value % 2 == 0}
my_dict3 = {num: num * 2 for num in [1, 2, 3]}

print(my_dict)
print(my_dict2)
print(my_dict3)
