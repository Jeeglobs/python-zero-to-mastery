# LIST COMPREHENSIONS

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# cleaner faster way of doing the above:

# list = [param for param in iterable]
your_list = [char for char in 'hello']

print(your_list)

# make a list of num 0 - 99
num_list = [num for num in range(0, 100)]

print(num_list)

# make num_list * 2
num_list2 = [num * 2 for num in range(0, 100)]

print(num_list2)

# num_list ** 2 but only even numbers
num_list3 = [num ** 2 for num in range(0, 100) if num % 2 == 0]

print(num_list3)
