# FILTER()

my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


print(multiply_by2(my_list))

print(list(map(multiply_by2, my_list)))

print(list(filter(only_odd, my_list)))
