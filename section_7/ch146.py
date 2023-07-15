# LAMBDA EXPRESSIONS

from functools import reduce

# lambda param: action(param)

my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    # print(acc, item)
    return acc + item


print(list(map(multiply_by2, my_list)))

# can get rid of multiply_by_2 and use lambda
print(list(map(lambda item: item * 2, my_list)))

# can get rid of only_odd and use lambda
print(list(filter(lambda item: item % 2 != 0, my_list)))

# can get rid of accumulator and use lambda
print(reduce(lambda acc, item: acc + item, my_list))
